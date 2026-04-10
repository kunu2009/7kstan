import json
import os
import re
import subprocess
from datetime import date, datetime, timedelta
from pathlib import Path
from urllib.parse import quote_plus

import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, request, send_from_directory
from voice_hooks import stt_available, tts_available

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
TODO_FILE = DATA_DIR / "todos.json"
STUDY_FILE = DATA_DIR / "study_state.json"
API_CATALOG_FILE = DATA_DIR / "api_catalog.json"
SETTINGS_FILE = DATA_DIR / "settings.json"

STAN_NAME = os.getenv("STAN_NAME", "Stan").strip() or "Stan"
GEMINI_MODEL = "gemini-1.5-flash"

SYSTEM_PROMPT = (
    f"You are {STAN_NAME}, a practical assistant for Kunal. "
    "Be direct, useful, and low-budget friendly. "
    "Prioritize study, productivity, and consistency. "
    "Give short actionable steps."
)

TOOL_ROUTER_PROMPT = (
    "You are a strict tool router. "
    "Return ONLY JSON with keys: action, api_id, params, reason. "
    "action must be 'api' or 'chat'. "
    "Choose 'api' only when an API call would directly answer user request. "
    "If unsure choose 'chat'. "
    "Do not include markdown or extra text."
)

app = Flask(__name__, static_folder="static")


def ensure_data_files() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not TODO_FILE.exists():
        TODO_FILE.write_text("[]\n", encoding="utf-8")
    if not STUDY_FILE.exists():
        STUDY_FILE.write_text(
            json.dumps(
                {
                    "last_study_date": None,
                    "streak_days": 0,
                    "total_sessions": 0,
                    "total_minutes": 0,
                    "subject_minutes": {},
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
    if not API_CATALOG_FILE.exists():
        API_CATALOG_FILE.write_text("[]\n", encoding="utf-8")
    if not SETTINGS_FILE.exists():
        SETTINGS_FILE.write_text(json.dumps({"gemini_api_key": ""}, indent=2) + "\n", encoding="utf-8")


def load_settings() -> dict:
    ensure_data_files()
    defaults = {"gemini_api_key": ""}
    try:
        raw = json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            return defaults
        merged = defaults | raw
        merged["gemini_api_key"] = str(merged.get("gemini_api_key", "")).strip()
        return merged
    except (json.JSONDecodeError, OSError):
        return defaults


def save_settings(settings: dict) -> None:
    ensure_data_files()
    SETTINGS_FILE.write_text(json.dumps(settings, indent=2) + "\n", encoding="utf-8")


def get_gemini_api_key() -> str:
    file_key = load_settings().get("gemini_api_key", "").strip()
    env_key = os.getenv("GEMINI_API_KEY", "").strip()
    return file_key or env_key


def set_gemini_api_key(api_key: str) -> None:
    settings = load_settings()
    settings["gemini_api_key"] = api_key.strip()
    save_settings(settings)


def load_api_catalog() -> list:
    ensure_data_files()
    try:
        catalog = json.loads(API_CATALOG_FILE.read_text(encoding="utf-8"))
        if isinstance(catalog, list):
            return catalog
        return []
    except (json.JSONDecodeError, OSError):
        return []


def _fill_url_template(template: str, params: dict) -> str:
    keys = set(re.findall(r"{([a-zA-Z0-9_]+)}", template))
    output = template
    for key in keys:
        value = str(params.get(key, "")).strip()
        output = output.replace("{" + key + "}", quote_plus(value))
    return output


def _fill_body_template(template_obj: dict, params: dict) -> dict:
    body = {}
    for key, value in template_obj.items():
        if isinstance(value, str):
            placeholders = re.findall(r"{([a-zA-Z0-9_]+)}", value)
            rendered = value
            for ph in placeholders:
                rendered = rendered.replace("{" + ph + "}", str(params.get(ph, "")).strip())
            body[key] = rendered
        else:
            body[key] = value
    return body


def execute_catalog_request(api_id: str, params: dict | None = None) -> dict:
    params = params or {}
    catalog = load_api_catalog()
    entry = next((item for item in catalog if item.get("id") == api_id), None)
    if not entry:
        return {"ok": False, "error": "API id not found in catalog."}

    method = str(entry.get("method", "GET")).upper()
    url = _fill_url_template(str(entry.get("url", "")), params)
    headers = {"User-Agent": f"{STAN_NAME}-toolbox/1.0"}
    headers.update(entry.get("headers", {}) or {})

    try:
        if method == "GET":
            response = requests.get(url, headers=headers, timeout=10)
        elif method == "POST_FORM":
            form_body = _fill_body_template(entry.get("form_body", {}) or {}, params)
            response = requests.post(url, data=form_body, headers=headers, timeout=10)
        elif method == "POST_JSON":
            json_body = _fill_body_template(entry.get("json_body", {}) or {}, params)
            response = requests.post(url, json=json_body, headers=headers, timeout=10)
        else:
            return {"ok": False, "error": f"Unsupported method: {method}"}

        content_type = (response.headers.get("content-type") or "").lower()
        if "application/json" in content_type:
            parsed = response.json()
            preview = json.dumps(parsed, indent=2)[:6000]
        else:
            preview = response.text[:6000]

        return {
            "ok": True,
            "status": response.status_code,
            "url": url,
            "method": method,
            "preview": preview,
        }
    except requests.RequestException as exc:
        return {"ok": False, "error": f"Request failed: {exc}"}


def _extract_json_block(text: str) -> str:
    stripped = (text or "").strip()
    if stripped.startswith("```"):
        lines = stripped.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        stripped = "\n".join(lines).strip()
    return stripped


def call_gemini_raw(prompt_text: str, *, temperature: float = 0.4, max_tokens: int = 280):
    gemini_api_key = get_gemini_api_key()
    if not gemini_api_key:
        return "", False

    payload = {
        "contents": [{"parts": [{"text": prompt_text}]}],
        "generationConfig": {
            "temperature": temperature,
            "maxOutputTokens": max_tokens,
        },
    }

    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{GEMINI_MODEL}:generateContent?key={gemini_api_key}"
    )

    try:
        response = requests.post(url, json=payload, timeout=18)
        if response.status_code >= 400:
            return "", False
        data = response.json()
        candidates = data.get("candidates", [])
        if not candidates:
            return "", False
        parts = candidates[0].get("content", {}).get("parts", [])
        if not parts:
            return "", False
        text = (parts[0].get("text") or "").strip()
        return text, bool(text)
    except requests.RequestException:
        return "", False


def choose_api_tool_with_gemini(user_message: str, history: list | None = None) -> dict | None:
    if not get_gemini_api_key():
        return None

    history = history or []
    recent = history[-4:]
    catalog = load_api_catalog()
    api_lines = []
    for item in catalog:
        api_lines.append(
            f"- {item.get('id')}: {item.get('use_case', '')}; url={item.get('url', '')}"
        )

    router_prompt = (
        f"{TOOL_ROUTER_PROMPT}\n\n"
        "Available APIs:\n"
        + "\n".join(api_lines)
        + "\n\nRecent chat:\n"
        + "\n".join(f"{m.get('role','user')}: {m.get('text','')}" for m in recent)
        + "\n\nUser message:\n"
        + user_message
        + "\n\n"
        "Return JSON example:\n"
        '{"action":"api","api_id":"open_meteo_forecast","params":{"lat":"19.0176","lon":"72.8562"},"reason":"user asked weather"}'
    )

    raw, ok = call_gemini_raw(router_prompt, temperature=0.1, max_tokens=220)
    if not ok:
        return None

    try:
        parsed = json.loads(_extract_json_block(raw))
    except json.JSONDecodeError:
        return None

    if not isinstance(parsed, dict):
        return None

    action = str(parsed.get("action", "chat")).lower().strip()
    if action != "api":
        return None

    api_id = str(parsed.get("api_id", "")).strip()
    params = parsed.get("params") or {}
    if not api_id or not isinstance(params, dict):
        return None

    return {"api_id": api_id, "params": params, "reason": parsed.get("reason", "")}


def summarize_tool_result(user_message: str, api_id: str, tool_result: dict) -> str:
    preview = str(tool_result.get("preview", ""))[:3500]
    prompt = (
        f"You are {STAN_NAME}. "
        "Respond naturally and concise. Explain the result clearly for user.\n\n"
        f"User asked: {user_message}\n"
        f"Tool used: {api_id}\n"
        f"HTTP status: {tool_result.get('status')}\n"
        f"Raw tool output:\n{preview}\n"
    )

    text, ok = call_gemini_raw(prompt, temperature=0.45, max_tokens=260)
    if ok and text:
        return text

    return (
        f"I used {api_id} and got status {tool_result.get('status')}.\n"
        f"Result preview:\n{preview[:900]}"
    )


def load_todos() -> list:
    ensure_data_files()
    try:
        return json.loads(TODO_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


def save_todos(todos: list) -> None:
    ensure_data_files()
    TODO_FILE.write_text(json.dumps(todos, indent=2), encoding="utf-8")


def load_study_state() -> dict:
    ensure_data_files()
    defaults = {
        "last_study_date": None,
        "streak_days": 0,
        "total_sessions": 0,
        "total_minutes": 0,
        "subject_minutes": {},
    }
    try:
        raw = json.loads(STUDY_FILE.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            return defaults
        merged = defaults | raw
        if not isinstance(merged.get("subject_minutes"), dict):
            merged["subject_minutes"] = {}
        return merged
    except (json.JSONDecodeError, OSError):
        return defaults


def save_study_state(state: dict) -> None:
    ensure_data_files()
    STUDY_FILE.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")


def build_study_plan(subject: str, minutes: int) -> str:
    warmup = max(5, round(minutes * 0.15))
    deep = max(15, round(minutes * 0.5))
    recall = max(10, round(minutes * 0.2))
    test = max(5, minutes - warmup - deep - recall)

    return (
        f"Study plan for {subject} ({minutes} min):\n"
        f"1) Warmup reading: {warmup} min\n"
        f"2) Deep focus block: {deep} min\n"
        f"3) Active recall (close notes): {recall} min\n"
        f"4) Quick self-test: {test} min\n"
        "5) Log completion with: /study done <subject> <minutes>"
    )


def get_revision_prompt(subject: str) -> str:
    prompts = {
        "history": "Give 5 causes, 5 effects, and 1 timeline for the chapter.",
        "english": "Read 1 passage, extract 10 key words, then summarize in 5 lines.",
        "hindi": "Revise vocabulary + 1 writing answer from memory.",
        "sanskrit": "Revise shabda-rupa and write 10 example sentences.",
        "political science": "Define 5 concepts and compare any 2 in a table.",
        "economics": "Solve 10 MCQs and explain each wrong answer.",
        "legal reasoning": "Read 10 principles and solve 15 practice questions.",
        "gk": "Revise current affairs for 20 minutes and quiz yourself.",
    }
    key = subject.strip().lower()
    default = "Do 25 minutes concept review + 15 minutes active recall + 10 MCQs."
    return prompts.get(key, default)


def mark_study_done(subject: str, minutes: int) -> str:
    state = load_study_state()

    today = date.today()
    today_str = today.isoformat()
    yesterday_str = (today - timedelta(days=1)).isoformat()

    last_date = state.get("last_study_date")
    streak = int(state.get("streak_days", 0))

    if last_date == today_str:
        new_streak = streak
    elif last_date == yesterday_str:
        new_streak = max(1, streak + 1)
    else:
        new_streak = 1

    state["last_study_date"] = today_str
    state["streak_days"] = new_streak
    state["total_sessions"] = int(state.get("total_sessions", 0)) + 1
    state["total_minutes"] = int(state.get("total_minutes", 0)) + minutes

    subject_map = state.get("subject_minutes", {})
    subject_key = subject.strip().lower()
    subject_map[subject_key] = int(subject_map.get(subject_key, 0)) + minutes
    state["subject_minutes"] = subject_map

    save_study_state(state)

    return (
        f"Logged study session: {subject} ({minutes} min).\n"
        f"Streak: {new_streak} day(s)\n"
        f"Total: {state['total_sessions']} sessions | {state['total_minutes']} minutes"
    )


def study_stats() -> str:
    state = load_study_state()
    subjects = state.get("subject_minutes", {})

    lines = [
        "Study stats:",
        f"Streak: {state.get('streak_days', 0)} day(s)",
        f"Total sessions: {state.get('total_sessions', 0)}",
        f"Total minutes: {state.get('total_minutes', 0)}",
    ]

    if subjects:
        top = sorted(subjects.items(), key=lambda x: x[1], reverse=True)[:5]
        lines.append("Top subjects:")
        for name, mins in top:
            lines.append(f"- {name}: {mins} min")
    else:
        lines.append("Top subjects: none yet")

    return "\n".join(lines)


def run_termux_command(command: str):
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=False,
            capture_output=True,
            text=True,
            timeout=6,
        )
        if result.returncode != 0:
            return None, result.stderr.strip() or "Command failed"
        return result.stdout.strip(), None
    except Exception as exc:
        return None, str(exc)


def handle_local_command(message: str):
    msg = message.strip()
    lower = msg.lower()

    if lower in {"/help", "help"}:
        return {
            "reply": (
                "Local commands:\n"
                "/help\n/time\n/battery\n/voice\n"
                "/todo add <task>\n/todo list\n/todo done <number>\n/todo remove <number>\n"
                "/study help\n/study plan <subject> <minutes>\n/study revise <subject>\n"
                "/study done <subject> <minutes>\n/study streak\n/study stats"
            ),
            "source": "local",
        }

    if lower in {"/time", "time", "date", "what time is it"}:
        now = datetime.now().strftime("%d %b %Y, %I:%M %p")
        return {"reply": f"Current time: {now}", "source": "local"}

    if lower in {"/battery", "battery", "battery status"}:
        output, err = run_termux_command("termux-battery-status")
        if output:
            try:
                data = json.loads(output)
                pct = data.get("percentage", "?")
                status = data.get("status", "unknown")
                temp = data.get("temperature", "?")
                return {
                    "reply": f"Battery: {pct}% | Status: {status} | Temp: {temp} C",
                    "source": "local",
                }
            except json.JSONDecodeError:
                return {"reply": f"Battery raw output: {output}", "source": "local"}
        return {
            "reply": "Battery command unavailable. Install Termux:API app and termux-api package.",
            "source": "local",
            "error": err,
        }

    if lower in {"/voice", "voice", "voice status"}:
        return {
            "reply": (
                f"Voice status | STT: {'ready' if stt_available() else 'not ready'} | "
                f"TTS: {'ready' if tts_available() else 'not ready'}"
            ),
            "source": "local",
        }

    if lower.startswith("/todo"):
        todos = load_todos()
        parts = msg.split(maxsplit=2)

        if len(parts) >= 2 and parts[1] == "list":
            if not todos:
                return {"reply": "Todo list is empty.", "source": "local"}
            lines = []
            for i, item in enumerate(todos, start=1):
                mark = "x" if item.get("done") else " "
                lines.append(f"{i}. [{mark}] {item.get('text', '')}")
            return {"reply": "\n".join(lines), "source": "local"}

        if len(parts) >= 3 and parts[1] == "add":
            task = parts[2].strip()
            if not task:
                return {"reply": "Usage: /todo add <task>", "source": "local"}
            todos.append({"text": task, "done": False})
            save_todos(todos)
            return {"reply": f"Added todo #{len(todos)}: {task}", "source": "local"}

        if len(parts) >= 3 and parts[1] in {"done", "remove"}:
            raw_index = parts[2].strip()
            if not raw_index.isdigit():
                return {
                    "reply": f"Usage: /todo {parts[1]} <number>",
                    "source": "local",
                }
            idx = int(raw_index) - 1
            if idx < 0 or idx >= len(todos):
                return {"reply": "Invalid todo number.", "source": "local"}

            if parts[1] == "done":
                todos[idx]["done"] = True
                save_todos(todos)
                return {
                    "reply": f"Marked todo #{idx + 1} as done.",
                    "source": "local",
                }

            removed = todos.pop(idx)
            save_todos(todos)
            return {
                "reply": f"Removed todo #{idx + 1}: {removed.get('text', '')}",
                "source": "local",
            }

        return {
            "reply": "Todo usage: /todo add <task> | /todo list | /todo done <number> | /todo remove <number>",
            "source": "local",
        }

    if lower.startswith("/study"):
        parts = msg.split()

        if len(parts) == 1 or (len(parts) >= 2 and parts[1] == "help"):
            return {
                "reply": (
                    "Study commands:\n"
                    "/study plan <subject> <minutes>\n"
                    "/study revise <subject>\n"
                    "/study done <subject> <minutes>\n"
                    "/study streak\n"
                    "/study stats"
                ),
                "source": "local",
            }

        if len(parts) >= 2 and parts[1] == "streak":
            state = load_study_state()
            return {
                "reply": f"Current study streak: {state.get('streak_days', 0)} day(s)",
                "source": "local",
            }

        if len(parts) >= 2 and parts[1] == "stats":
            return {"reply": study_stats(), "source": "local"}

        if len(parts) >= 3 and parts[1] == "revise":
            subject = " ".join(parts[2:]).strip()
            if not subject:
                return {"reply": "Usage: /study revise <subject>", "source": "local"}
            prompt = get_revision_prompt(subject)
            return {
                "reply": f"Revision drill for {subject}:\n{prompt}",
                "source": "local",
            }

        if len(parts) >= 4 and parts[1] in {"plan", "done"}:
            minutes_text = parts[-1]
            if not minutes_text.isdigit():
                return {
                    "reply": f"Usage: /study {parts[1]} <subject> <minutes>",
                    "source": "local",
                }
            minutes = int(minutes_text)
            if minutes < 10 or minutes > 240:
                return {
                    "reply": "Minutes must be between 10 and 240.",
                    "source": "local",
                }

            subject = " ".join(parts[2:-1]).strip()
            if not subject:
                return {
                    "reply": f"Usage: /study {parts[1]} <subject> <minutes>",
                    "source": "local",
                }

            if parts[1] == "plan":
                return {"reply": build_study_plan(subject, minutes), "source": "local"}

            return {"reply": mark_study_done(subject, minutes), "source": "local"}

        return {
            "reply": "Study usage: /study help | /study plan <subject> <minutes> | /study revise <subject> | /study done <subject> <minutes> | /study streak | /study stats",
            "source": "local",
        }

    return None


def call_gemini(user_message: str, history: list | None = None):
    gemini_api_key = get_gemini_api_key()
    if not gemini_api_key:
        return (
            "Gemini key missing. Add it in Stan settings or GEMINI_API_KEY in .env. I can still run local commands like /help.",
            "local",
        )

    history = history or []
    text_parts = [SYSTEM_PROMPT]
    for item in history[-6:]:
        role = item.get("role", "user")
        text = item.get("text", "")
        if text:
            text_parts.append(f"{role}: {text}")
    text_parts.append(f"user: {user_message}")

    payload = {
        "contents": [{"parts": [{"text": "\n".join(text_parts)}]}],
        "generationConfig": {
            "temperature": 0.6,
            "maxOutputTokens": 400,
        },
    }

    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{GEMINI_MODEL}:generateContent?key={gemini_api_key}"
    )

    try:
        response = requests.post(url, json=payload, timeout=18)
        if response.status_code >= 400:
            return (
                f"Gemini request failed ({response.status_code}). Try again in a moment.",
                "local",
            )

        data = response.json()
        candidates = data.get("candidates", [])
        if not candidates:
            return "No AI response received. Please retry.", "local"

        parts = candidates[0].get("content", {}).get("parts", [])
        if not parts:
            return "No text returned by Gemini.", "local"

        text = parts[0].get("text", "").strip()
        if not text:
            return "Empty response from Gemini.", "local"
        return text, "gemini"

    except requests.RequestException:
        return "Network issue while contacting Gemini. Check data connection.", "local"


@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/toolbox")
def toolbox():
    return send_from_directory(app.static_folder, "toolbox.html")


@app.route("/api/health")
def health():
    return jsonify({"ok": True, "name": STAN_NAME})


@app.route("/mascot")
def mascot():
    return send_from_directory(app.static_folder, "stan-mascot.jpeg")


@app.route("/api/settings", methods=["GET", "POST"])
def api_settings():
    if request.method == "GET":
        gemini_key = get_gemini_api_key()
        return jsonify(
            {
                "ok": True,
                "geminiConfigured": bool(gemini_key),
                "geminiKeyLast4": gemini_key[-4:] if len(gemini_key) >= 4 else "",
            }
        )

    payload = request.get_json(silent=True) or {}
    gemini_key = str(payload.get("gemini_api_key", "")).strip()
    set_gemini_api_key(gemini_key)
    return jsonify(
        {
            "ok": True,
            "geminiConfigured": bool(gemini_key),
            "geminiKeyLast4": gemini_key[-4:] if len(gemini_key) >= 4 else "",
        }
    )


@app.route("/api/catalog")
def api_catalog():
    return jsonify({"items": load_api_catalog()})


@app.route("/api/catalog/run", methods=["POST"])
def run_api_catalog_item():
    payload = request.get_json(silent=True) or {}
    api_id = (payload.get("id") or "").strip()
    params = payload.get("params") or {}

    if not api_id:
        return jsonify({"ok": False, "error": "Missing api id."}), 400
    if not isinstance(params, dict):
        return jsonify({"ok": False, "error": "Params must be an object."}), 400

    result = execute_catalog_request(api_id, params)
    status = 200 if result.get("ok") else 400
    return jsonify(result), status


@app.route("/api/chat", methods=["POST"])
def chat():
    payload = request.get_json(silent=True) or {}
    message = (payload.get("message") or "").strip()
    history = payload.get("history") or []

    if not message:
        return jsonify({"reply": "Message is empty.", "source": "local"}), 400

    local_result = handle_local_command(message)
    if local_result:
        return jsonify(local_result)

    tool_choice = choose_api_tool_with_gemini(message, history)
    if tool_choice:
        result = execute_catalog_request(tool_choice["api_id"], tool_choice["params"])
        if result.get("ok"):
            summary = summarize_tool_result(message, tool_choice["api_id"], result)
            return jsonify(
                {
                    "reply": summary,
                    "source": "tool+gemini",
                    "tool": {
                        "id": tool_choice["api_id"],
                        "reason": tool_choice.get("reason", ""),
                        "status": result.get("status"),
                    },
                }
            )
        return jsonify(
            {
                "reply": (
                    f"I tried using tool {tool_choice['api_id']} but it failed: "
                    f"{result.get('error', 'unknown error')}"
                ),
                "source": "tool",
            }
        )

    ai_reply, source = call_gemini(message, history)
    return jsonify({"reply": ai_reply, "source": source})


if __name__ == "__main__":
    ensure_data_files()
    app.run(host="0.0.0.0", port=5000, debug=False)

# Stan v1 Starter

A lightweight chat assistant for Termux on Redmi 9C.

## What is included

- Flask chat backend with local command dispatcher
- Gemini free-tier API fallback
- Local todo storage in JSON
- Mobile-friendly chat UI
- Browser voice input (mic button) on supported browsers
- Optional browser text-to-speech replies (TTS toggle)
- Voice extension hooks (Python stubs for future native Termux wiring)
- Separate API Hub GUI with categorized no-auth endpoint catalog
- Backend API runner for catalog entries with parameterized requests
- One-click workflow presets in API Hub (network check, nearby ATM, weather + AQI, threat check, study pack)
- Custom workflow builder in API Hub (save, load, run, delete)
- Expanded API catalog across jobs, health, games, transport, food, and open data

## Project layout

- app.py: backend server and command handling
- static/index.html: chat interface
- data/todos.json: local todo storage
- voice_hooks.py: future voice features
- termux-setup.md: exact setup commands
- stan-v1-blueprint.md: product and roadmap

## Quick start

1. Follow steps in termux-setup.md.
2. Add Gemini key in .env.
3. Run: python app.py
4. Open: `http://127.0.0.1:5000`
5. API Hub: `http://127.0.0.1:5000/toolbox`

## Phone quickstart

1. Install Termux from F-Droid, not from the Play Store version.
2. Install the Termux:API app if you want battery support.
3. Open Termux, go to the project folder, and start the virtual environment.
4. Run `python app.py` and keep Termux open while Stan is running.
5. Open `http://127.0.0.1:5000` in Chrome on the same phone.
6. Use `http://127.0.0.1:5000/toolbox` for the API Hub.
7. Tap Mic in Chrome for voice input if the browser supports it.
8. Turn on TTS if you want spoken replies.

## How to use on phone

- Type `/help` first to see local commands.
- Use `/time`, `/battery`, and `/voice` for quick device checks.
- Use `/todo add <task>` to capture reminders quickly.
- Use `/study plan <subject> <minutes>` to generate a study block.
- Use the API Hub when you want a separate tool dashboard instead of chat.
- Keep Gemini prompts short on mobile data.
- If the browser mic does not work, fall back to typing and TTS.

## Local commands

- /help
- /time
- /battery
- /voice
- /todo add `<task>`
- /todo list
- /todo done `<number>`
- /todo remove `<number>`
- /study help
- /study plan `<subject> <minutes>`
- /study revise `<subject>`
- /study done `<subject> <minutes>`
- /study streak
- /study stats

## Next implementation targets

- Native Termux STT/TTS wiring beyond browser voice
- Daily planner command presets for MH-CET and board subjects
- Mascot reaction layer in UI
- Favorites/pinned APIs in the API Hub
- Export/import for custom workflows
- API reliability labels for keep/review/remove endpoints
- In-app Gemini key settings save for phone use

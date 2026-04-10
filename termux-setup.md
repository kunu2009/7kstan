# Termux Setup (Stan v1)

## 1) Update and core packages

Run in Termux:

pkg update -y
pkg upgrade -y
pkg install -y python git termux-api

## 2) Project setup

cd ~/storage/shared
cd stan/stan-v1
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

## 3) Gemini API key

Create a .env file:

echo GEMINI_API_KEY=YOUR_KEY_HERE > .env

Optional name setting:

echo STAN_NAME=Stan >> .env

You can also skip the `.env` step and paste the key directly into Stan's in-app Gemini Settings panel after the server starts.

## 4) Start server

source .venv/bin/activate
python app.py

If server starts correctly, open browser on phone:

`http://127.0.0.1:5000`

API Hub (separate from chat):

`http://127.0.0.1:5000/toolbox`

## 5) Important notes

- termux-api app must also be installed from F-Droid for battery command support.
- If battery command fails, Stan still works and falls back gracefully.
- Keep Gemini usage short to save data on 1GB/day plans.

## 6) Quick test messages

- /help
- /time
- /battery
- /voice
- /todo add Revise legal reasoning chapter 1
- /todo list
- /study help
- /study plan history 45
- /study done history 45
- /study streak
- Make me a 45 minute study session for history

## 7) Voice test in browser

- Open Stan in Chrome on Android for best mic support.
- Tap Mic and speak a short command.
- Toggle TTS On if you want spoken replies.

## 8) Daily phone use

- Open Termux and start Stan with `python app.py`.
- Keep the server tab open while using the assistant.
- Use `http://127.0.0.1:5000` for chat.
- Use `http://127.0.0.1:5000/toolbox` for the API Hub.
- Start with `/help`, then try `/time`, `/battery`, and `/study help`.
- For quick notes, use `/todo add <task>`.
- If voice input fails, type your message and leave TTS on.

## 9) Next todo list

- Add native Termux STT/TTS support.
- Add pinned/favorite APIs in the API Hub.
- Add export/import for custom workflows.
- Add better health labels for APIs that need auth or rate-limit handling.

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

- Native Termux STT/TTS wiring (beyond browser voice)
- Daily planner command presets for MH-CET and board subjects
- Mascot reaction layer in UI

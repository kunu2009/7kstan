# Stan v1 Blueprint

## 1) Product Spec (One Page)

### Product Name
Stan v1 (Redmi 9C Operator Assistant)

### Target User
Kunal (student builder, mobile-first, low-data, low-budget constraints).

### Core Goal
A practical AI operator that helps you execute daily tasks through chat, with strong focus on study, productivity, and consistency.

### Platform and Constraints
- Device: Redmi 9C
- Runtime: Termux + Python
- Internet: limited daily data, must support offline basics
- Performance: low RAM and battery friendly

### Main User Loop
1. Open Stan.
2. Ask in natural language.
3. Stan either runs a local action or calls Gemini.
4. Stan returns clear next step and optional action button.
5. Progress gets saved (todos, session notes, routine tracking).

### v1 Must Deliver
- Chat UI with fast response.
- Gemini free-tier integration.
- Local command dispatcher for utility commands.
- Todo management from chat.
- Basic study helper behavior (focus plans, revision prompts).
- Clean mascot-inspired style.

### Non-Goals for v1
- Full Android system-level automation.
- Heavy voice pipeline with always-on wake word.
- Complex multi-agent workflow.

### Success Metrics (first 30 days)
- 7-day streak of daily usage.
- At least 3 tasks completed per day via Stan.
- 20+ study sessions logged.
- App startup under 3 seconds on device.

## 2) Feature Priority

### Must Have (v1.0)
- Chat interface (web UI served by Python).
- Gemini response fallback.
- Local commands: help, time, battery, todo add/list/done/remove.
- Lightweight local persistence (JSON file).
- Stable error handling and clear messages.

### Should Have (v1.1)
- Voice input button (push to talk).
- Text to speech replies.
- Study mode command set for MH-CET and board prep.
- Daily plan template and end-of-day review.

### Could Have (v1.2)
- Mascot reactions and mood states.
- Offline quote/focus coach mode.
- News, weather, dictionary tools.
- Export logs to markdown.

### Later (v2+)
- Advanced automation workflows.
- Launcher integration.
- Multi-app 7K ecosystem bridge.

## 3) Architecture

- Frontend: static HTML/CSS/JS chat page.
- Backend: Flask server in Termux.
- AI Layer: Gemini REST API.
- Local Action Layer: Python command dispatcher.
- Storage: local JSON (todos and small state).

## 4) Safety and Focus Rules

Stan should:
- Give practical, realistic steps.
- Keep answers concise and action-oriented.
- Avoid explicit or harmful guidance.
- Redirect health concerns to qualified professionals.
- Prefer low-cost options in all recommendations.

## 5) 14-Day Build Sequence

1. Day 1-2: setup + base chat UI + Gemini call.
2. Day 3-4: command dispatcher and todo persistence.
3. Day 5-6: study helper prompts and daily planner.
4. Day 7: stability fixes, logging, and cleanup.
5. Day 8-10: voice hooks and optional TTS.
6. Day 11-12: mascot style polish and UX cleanup.
7. Day 13-14: test on-device, optimize startup and memory.

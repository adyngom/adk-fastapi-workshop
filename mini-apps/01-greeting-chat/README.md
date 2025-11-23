# Greeting Chat - Module 3 Mini-App

**Purpose:** Production chat UI for greeting_agent
**Framework:** Next.js 14 + React + TypeScript
**Port:** 3001 (to avoid conflict with other apps)

---

## 🚀 Quick Start

```bash
# From mini-apps root
npm install  # Install all workspaces

# Run greeting-chat
npm run dev:greeting

# Or from this directory
cd mini-apps/01-greeting-chat
npm install
npm run dev
```

**Opens on:** http://localhost:3001

---

## 🔌 Backend Requirements

**Needs FastAPI running on port 8000:**

```bash
# From project root
cd /path/to/adk-fastapi-workshop
./.idx/start-services.sh
```

**Endpoint:** POST http://localhost:8000/api/agents/chat
**Payload:** `{ "message": "...", "agent": "greeting_agent" }`

---

## ✨ Features

- Chat interface (ChatGPT-style)
- Voice input (microphone button)
- Tool call visualization (expandable cards)
- Sample questions sidebar
- Connection status indicator
- Demo mode (works without backend)
- Mobile responsive
- Copy messages
- Clear chat

---

## 🎬 For Course Recording

**Result-First Hook (0:00-0:30):**

```
[Screen recording]

"Look at this - an AI chat with voice input.

[Click mic, say: 'What time is it?']
[Agent responds, shows tool call card]

You see that tool call? That's the agent using get_current_time.

[Type: 'Tell me about my company']
[Shows company info with tool call]

This is production-ready. Real UI, not debugging tools.
Here's how I built it..."

[Cut to code - start Module 3 tutorial]
```

---

## 🛠️ Troubleshooting

**"Cannot find module '@adk-course/shared'"**
- Run `npm install` from mini-apps root first
- Shared library must be installed

**CORS errors**
- Make sure FastAPI has CORS enabled for localhost:3001
- Or use the Next.js API route (app/api/chat/route.ts)

**Voice input not working**
- Only works in Chrome/Edge (not Firefox/Safari)
- Component handles this gracefully with alert

---

**Ready to run!** Just `npm install` and `npm run dev`. 🚀

# 🤖 Module 1: Understanding the Streaming Chatbot

> **Welcome!** You've just cloned the project and got everything running with `docker compose up`. Now let's explore what's happening behind the scenes when you chat with the AI.

---

## 🎯 What You'll Learn

- How WebSockets enable real-time streaming responses
- The journey of a message from browser to AI and back
- Where to make changes to customize the chatbot
- How to extend this architecture for your own projects

---

## 🚀 Quick Start: See It In Action

1. **Open the chat UI**: http://localhost
2. **Type a message**: "Explain quantum computing in simple terms"
3. **Watch the magic**: The response appears word-by-word as it's generated!

**Question for the group**: *Why does this feel faster than waiting for a complete response?*

---

## 🏗️ Architecture Overview

Our chatbot has **4 main components** working together:

```
┌─────────────┐
│   Browser   │  ← You interact here
│  (Port 80)  │
└──────┬──────┘
       │ WebSocket Connection
       ↓
┌─────────────┐
│    NGINX    │  ← Routes traffic
│  (Port 80)  │
└──────┬──────┘
       │ Proxy to Backend
       ↓
┌─────────────┐
│   FastAPI   │  ← Handles WebSocket
│  (Port 8000)│
└──────┬──────┘
       │ Streams chat
       ↓
┌─────────────┐
│Agent Manager│  ← Talks to AI
│  + Gemini   │
└─────────────┘
```

---

## 🌐 Component 1: The Frontend (What You See)

**File**: `frontend/index.html`

This is a simple single-page application with:
- A chat interface (messages + input box)
- WebSocket connection for real-time communication
- JavaScript to handle streaming responses

### Key Code Sections

#### Establishing the Connection (Line 102)
```javascript
// Create WebSocket connection with unique session ID
const sessionId = 'session_' + Date.now();
const wsUrl = `ws://localhost/ws/chat/${sessionId}`;
ws = new WebSocket(wsUrl);
```

**Workshop Tip**: *Each browser tab gets its own session ID, so you can have multiple conversations!*

#### Sending a Message (Line 147-154)
```javascript
function sendMessage() {
    const message = messageInput.value.trim();

    // Send JSON with message and agent name
    ws.send(JSON.stringify({
        message: message,
        agent: 'default'
    }));
}
```

#### Receiving Streaming Response (Line 118-126)
```javascript
ws.onmessage = (event) => {
    const data = JSON.parse(event.data);

    if (data.type === 'chunk') {
        // Append each word as it arrives!
        appendMessage(data.content, 'assistant', true);
    }
};
```

**Try This**: Open your browser DevTools → Network → WS (WebSockets) → Click the connection → Watch the messages stream in real-time!

---

## 🔀 Component 2: NGINX Proxy (The Traffic Cop)

**File**: `nginx.conf`

NGINX does two important jobs:
1. **Serves the HTML file** from port 80
2. **Upgrades HTTP → WebSocket** and forwards to FastAPI

### The WebSocket Magic (Lines 38-44)

```nginx
location /ws {
    proxy_pass http://api:8000;           # Send to FastAPI
    proxy_http_version 1.1;                # Use HTTP/1.1
    proxy_set_header Upgrade $http_upgrade;    # Enable WebSocket
    proxy_set_header Connection "Upgrade";     # Keep connection alive
}
```

**Why do we need NGINX?**
- Single port (80) for everything
- Production-ready reverse proxy
- Can easily add SSL, load balancing, etc.

**Workshop Discussion**: *What happens if we remove the Upgrade headers?*

---

## ⚡ Component 3: FastAPI Backend (The Coordinator)

**File**: `api/main.py` (Lines 75-104)

This is where the WebSocket connection is handled.

### The WebSocket Endpoint

```python
@app.websocket("/ws/chat/{session_id}")
async def websocket_chat(websocket: WebSocket, session_id: str):
    # 1. Accept the WebSocket connection
    await websocket.accept()

    # 2. Stay connected and listen for messages
    while True:
        # Receive message from frontend
        data = await websocket.receive_text()
        message_data = json.loads(data)

        # Stream response from Agent Manager
        async for chunk in agent_manager.stream_chat(
            session_id=session_id,
            message=message_data.get("message", ""),
            agent_name=message_data.get("agent", "default")
        ):
            # Send each chunk back immediately
            await websocket.send_json(chunk)
```

**Key Concepts**:
- `async/await`: Non-blocking code (other users can chat simultaneously)
- `while True`: Connection stays open until user closes browser
- `async for chunk`: Process streaming response piece by piece

**Try This**:
1. Open http://localhost:8000/docs
2. You'll see the REST API, but WebSockets aren't shown (they're not REST!)
3. The WebSocket endpoint lives at `ws://localhost/ws/chat/{session_id}`

---

## 🤖 Component 4: Agent Manager (The Brain)

**File**: `agents/manager.py` (Lines 45-100)

This is where we:
1. Maintain conversation history
2. Call the Google Gemini API
3. Stream the response back

### The Stream Chat Method

```python
async def stream_chat(self, session_id: str, message: str, agent_name: str):
    # 1. Get or create conversation history for this session
    if session_id not in self.sessions:
        self.sessions[session_id] = []

    # 2. Add the user's message to history
    self.sessions[session_id].append({
        "role": "user",
        "parts": [{"text": message}]
    })

    # 3. Call Gemini API with streaming enabled
    response = await self.client.aio.models.generate_content_stream(
        model="gemini-2.0-flash-exp",
        contents=self.sessions[session_id]  # Send full history
    )

    # 4. Stream chunks back as they arrive
    full_response = ""
    async for chunk in response:
        if chunk.text:
            full_response += chunk.text
            yield {
                "type": "chunk",
                "content": chunk.text,
                "agent": agent_name
            }

    # 5. Save the complete response to history
    self.sessions[session_id].append({
        "role": "model",
        "parts": [{"text": full_response}]
    })
```

**Important Details**:
- `yield`: Returns chunks immediately (streaming)
- History includes **both** user and AI messages (that's how the AI remembers context!)
- Sessions stored **in memory** (lost on restart - later we'll add Redis)

---

## 🔄 The Complete Journey of a Message

Let's trace what happens when you type "Hello":

```
┌─────────────────────────────────────────────────────────┐
│ 1. User types "Hello" and clicks Send                   │
└────────────────────┬────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────┐
│ 2. Frontend JavaScript                                  │
│    ws.send({"message": "Hello", "agent": "default"})   │
└────────────────────┬────────────────────────────────────┘
                     ↓ WebSocket: ws://localhost/ws/...
┌─────────────────────────────────────────────────────────┐
│ 3. NGINX receives WebSocket request                     │
│    Upgrades HTTP → WebSocket                            │
│    Proxies to http://api:8000/ws/chat/session_123      │
└────────────────────┬────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────┐
│ 4. FastAPI websocket_chat() receives message            │
│    Calls agent_manager.stream_chat(...)                 │
└────────────────────┬────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────┐
│ 5. Agent Manager                                         │
│    - Adds "Hello" to conversation history               │
│    - Calls Gemini API with history                      │
│    - Receives streaming response                        │
└────────────────────┬────────────────────────────────────┘
                     ↓ Streaming chunks: "Hi" → "!" → " How" → ...
┌─────────────────────────────────────────────────────────┐
│ 6. Each chunk flows back through the same path:         │
│    Agent Manager → FastAPI → NGINX → Browser           │
└────────────────────┬────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────┐
│ 7. Browser receives chunks                              │
│    Appends each word to the chat UI                     │
│    User sees: "Hi!" → "Hi! How" → "Hi! How can..." ✨   │
└─────────────────────────────────────────────────────────┘
```

**Total time**: ~100-500ms (feels instant!)

---

## 🛠️ Hands-On Exercises

### Exercise 1: Modify the UI
**File**: `frontend/index.html`

1. Change the header color (line 29): Try `#4338CA` (indigo)
2. Add a timestamp to messages
3. Add a "Clear Chat" button

### Exercise 2: Log the Conversation
**File**: `agents/manager.py`

Add logging to see what's being sent to the AI:

```python
async def stream_chat(self, session_id: str, message: str, agent_name: str):
    # Add this line after line 113
    logger.info(f"Session {session_id}: User said: {message}")

    # Add this line after line 139
    logger.info(f"Session {session_id}: AI responded: {full_response[:50]}...")
```

Then watch the logs:
```bash
docker compose logs -f api
```

### Exercise 3: Change the AI Model
**File**: `config/settings.py`

Try a different model (line 22):
```python
default_model: str = "gemini-1.5-pro"  # More powerful, slower
```

Restart and compare the responses!

---

## 📦 Key Technologies Explained

### WebSockets
- **What**: Persistent, bidirectional connection
- **Why**: Enables real-time streaming (not polling)
- **Alternative**: Server-Sent Events (SSE) - one-way only

### Async/Await
- **What**: Asynchronous programming in Python
- **Why**: Handle multiple users without blocking
- **Key Point**: FastAPI can handle 1000s of concurrent WebSocket connections

### Streaming
- **What**: Send response incrementally, not all at once
- **Why**: Better UX (feels 10x faster), lower memory usage
- **Gemini Support**: Native streaming API (`generate_content_stream`)

---

## 🎓 Understanding the Architecture Choices

### Why WebSocket instead of HTTP POST?
❌ **HTTP POST**:
- Send request → Wait → Get full response → Close connection
- New request for every message

✅ **WebSocket**:
- Open connection once → Send/receive many messages → Close when done
- Perfect for chat!

### Why In-Memory Sessions?
**Current**: `self.sessions = {}` (Python dictionary)

**Pros**:
- Simple
- Fast
- Great for workshops/prototypes

**Cons**:
- Lost on restart
- Not shared across multiple API instances

**Next Module Preview**: We'll add Redis for persistent sessions!

### Why NGINX?
**Could we skip it?** Yes, for development. But NGINX gives us:
- Static file serving (frontend)
- SSL termination (HTTPS)
- Load balancing (multiple API instances)
- Rate limiting
- Production-ready setup

---

## 🚀 Where to Go From Here

In the next modules, we'll extend this architecture:

### Module 2: Adding Tools & Function Calling
- Give the AI ability to search, calculate, etc.
- Integrate with MCP (Model Context Protocol)

### Module 3: Multi-Agent Conversations
- Create specialized agents (researcher, coder, reviewer)
- Agents collaborate to solve complex tasks

### Module 4: Persistent Storage
- Add Redis for session persistence
- Store conversation history in a database
- Add user authentication

### Module 5: Production Deployment
- Environment variables and secrets management
- Monitoring with Prometheus + Grafana
- Deploy to Google Cloud Run

---

## 🐛 Common Issues & Solutions

### WebSocket connection fails
**Symptom**: "Disconnected" in the UI

**Check**:
1. Is the API running? `docker compose ps`
2. Check API logs: `docker compose logs api`
3. Is NGINX running? `docker compose ps frontend`

### AI responses are slow
**Possible causes**:
1. API key not set (check `.env` file)
2. Network latency to Google API
3. Complex prompt (try a simpler question)

### Lost conversation history on refresh
**Expected behavior**: Sessions are in-memory only

**Solution**: We'll add Redis in Module 4

---

## 💡 Discussion Questions

1. **Latency**: Where does most of the time go in our request flow?
2. **Scaling**: What happens if 1000 users connect at once?
3. **Security**: What security considerations are missing?
4. **Cost**: How would you estimate API costs for this setup?

---

## 📚 Additional Resources

- [FastAPI WebSockets Docs](https://fastapi.tiangolo.com/advanced/websockets/)
- [Google Gemini API Guide](https://ai.google.dev/gemini-api/docs)
- [MDN WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)

---

## ✅ Module 1 Checklist

Before moving to Module 2, make sure you can:

- [ ] Explain the 4 main components of the architecture
- [ ] Trace the path of a message through the system
- [ ] Understand why we use WebSockets instead of HTTP
- [ ] Open DevTools and see WebSocket messages
- [ ] Modify the frontend and see changes
- [ ] Change the AI model in settings
- [ ] Read and understand the logs

---

**🎉 Congratulations!** You now understand how production-grade streaming chatbots work!

**Next**: [Module 2: Function Calling & Tools](./2-FUNCTION-CALLING.md)

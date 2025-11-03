# Streamlit + FastAPI Integration

**Purpose**: Build beautiful custom UIs for your ADK agents using Streamlit

---

## 🎯 Why Streamlit for Agent UIs?

**Streamlit Benefits**:
- ✅ **Fast development**: UI in pure Python (no HTML/CSS/JS)
- ✅ **Rich components**: Charts, tables, maps, file uploads
- ✅ **Data visualization**: Perfect for data-heavy agents
- ✅ **Reactive**: Auto-updates on user interaction
- ✅ **Works with FastAPI**: Easy backend integration

**Perfect For**:
- News analysis dashboards
- Data pipeline visualizations
- Competitive research comparisons
- Multi-modal agents (images, audio, video)
- Complex workflows with state

---

## 🏗️ Architecture: Streamlit + FastAPI + ADK

```
┌──────────────────────────────────────────────┐
│  STREAMLIT APP (port 8501)                   │
│  - Python-based UI                           │
│  - st.chat_input(), st.markdown()           │
│  - Data visualization components            │
└────────────────┬─────────────────────────────┘
                 │
                 │ HTTP/WebSocket
                 ↓
┌──────────────────────────────────────────────┐
│  FASTAPI BACKEND (port 8000)                 │
│  - AgentManager                              │
│  - /api/agents/chat (REST)                  │
│  - /ws/chat/{session} (WebSocket)           │
└────────────────┬─────────────────────────────┘
                 │
                 │ Runs
                 ↓
┌──────────────────────────────────────────────┐
│  ADK AGENTS (adk_agents/)                    │
│  - Agent definitions                         │
│  - Tools                                     │
│  - Multi-agent workflows                     │
└──────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
adk-fastapi-workshop/
├── api/                    # FastAPI backend
├── adk_agents/            # ADK agent definitions
└── streamlit_apps/        # Streamlit frontends (NEW)
     ├── generic_chat/     # Works with any agent
     ├── news_dashboard/   # Custom for news_pipeline
     └── research_compare/ # Custom for competitive_analysis
```

---

## 🚀 Quick Start: Generic Streamlit Chat

### Step 1: Create Streamlit App

**File**: `streamlit_apps/generic_chat/app.py`

```python
"""
Generic Streamlit Chat Interface
Works with any ADK agent via FastAPI backend
"""
import streamlit as st
import requests
import json

# Page config
st.set_page_config(
    page_title="ADK Agent Chat",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 ADK Agent Chat")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Agent selector
agents_response = requests.get("http://api:8000/api/agents/list")
agents = agents_response.json()

selected_agent = st.selectbox(
    "Select Agent",
    options=[agent["name"] for agent in agents],
    format_func=lambda name: next(a["description"] for a in agents if a["name"] == name)
)

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call FastAPI backend
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Use WebSocket for streaming (better) or REST for simple
        response = requests.post(
            "http://api:8000/api/agents/chat",
            json={
                "message": prompt,
                "agent": selected_agent,
                "session_id": st.session_state.get("session_id", "streamlit_session")
            }
        )

        if response.status_code == 200:
            full_response = response.json()["message"]
            message_placeholder.markdown(full_response)
        else:
            message_placeholder.error(f"Error: {response.status_code}")

    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
```

### Step 2: Requirements

**File**: `streamlit_apps/generic_chat/requirements.txt`

```
streamlit>=1.28.0
requests>=2.32.0
```

### Step 3: Add to Docker Compose

**File**: `docker-compose.yml` (add this service)

```yaml
  streamlit-chat:
    build:
      context: .
      dockerfile: Dockerfile.streamlit
    container_name: adk-workshop-streamlit
    ports:
      - "8501:8501"
    environment:
      - API_URL=http://api:8000
    volumes:
      - ./streamlit_apps:/app/streamlit_apps
    networks:
      - adk-network
    depends_on:
      - api
    command: streamlit run streamlit_apps/generic_chat/app.py --server.port 8501 --server.address 0.0.0.0
```

### Step 4: Create Dockerfile

**File**: `Dockerfile.streamlit`

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install Streamlit
COPY streamlit_apps/generic_chat/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy Streamlit apps
COPY streamlit_apps /app/streamlit_apps

# Expose Streamlit port
EXPOSE 8501

# Run via docker-compose command
```

### Step 5: Start and Test

```bash
docker compose up -d streamlit-chat

# Access: http://localhost:8501
```

---

## 🎨 Custom Agent Dashboard: News Pipeline

### Advanced Example with Data Visualization

**File**: `streamlit_apps/news_dashboard/app.py`

```python
"""
News Analysis Dashboard
Custom UI for news_pipeline agent
"""
import streamlit as st
import requests
import json
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="News Analysis", layout="wide")

st.title("📰 News Analysis Dashboard")

# Tabs for different views
tab1, tab2, tab3 = st.tabs(["Chat", "Sentiment Analysis", "Topic Trends"])

with tab1:
    # Chat interface
    if prompt := st.chat_input("Ask about news..."):
        response = requests.post(
            "http://api:8000/api/agents/chat",
            json={"message": prompt, "agent": "news_pipeline"}
        )

        if response.status_code == 200:
            result = response.json()["message"]
            st.markdown(result)

            # Parse structured response for visualization
            # (Assumes news_pipeline returns JSON-formatted analysis)
            try:
                data = json.loads(result)
                if "sentiment" in data:
                    with tab2:
                        # Sentiment chart
                        sentiment_data = pd.DataFrame(data["sentiment"])
                        fig = px.bar(sentiment_data, x="topic", y="score",
                                    title="Sentiment Scores by Topic")
                        st.plotly_chart(fig)
            except:
                pass  # Not structured data

with tab2:
    st.subheader("Sentiment Over Time")
    # Visualization code

with tab3:
    st.subheader("Trending Topics")
    # More visualization
```

**Benefits**:
- Rich data visualization
- Multiple views (tabs)
- Custom logic for agent-specific data
- Better UX for complex outputs

---

## 🔌 Integration Patterns

### Pattern 1: REST API (Simple)

**Use when**: Non-streaming, simple request/response

```python
import requests

response = requests.post(
    "http://api:8000/api/agents/chat",
    json={"message": user_input, "agent": agent_name}
)

result = response.json()
st.markdown(result["message"])
```

**Pros**: Simple, synchronous
**Cons**: No streaming, no real-time updates

---

### Pattern 2: WebSocket (Streaming)

**Use when**: Want to show agent thinking in real-time

```python
import streamlit as st
import websocket
import json
from threading import Thread

def connect_websocket():
    ws = websocket.WebSocketApp(
        f"ws://api:8000/ws/chat/{session_id}",
        on_message=on_message,
        on_error=on_error
    )
    ws.run_forever()

# Run WebSocket in background thread
thread = Thread(target=connect_websocket)
thread.start()

# Send message
ws.send(json.dumps({"message": user_input, "agent": agent_name}))
```

**Pros**: Real-time streaming, progressive response
**Cons**: More complex, requires threading

---

### Pattern 3: Server-Sent Events (Recommended for Streamlit)

**Use when**: Want streaming with simpler code

```python
import streamlit as st
import requests

# Enable streaming in Streamlit
message_placeholder = st.empty()
full_response = ""

# Stream from FastAPI
with requests.post(
    "http://api:8000/api/agents/chat-stream",  # New endpoint (to implement)
    json={"message": user_input, "agent": agent_name},
    stream=True
) as response:
    for chunk in response.iter_content(chunk_size=None, decode_unicode=True):
        full_response += chunk
        message_placeholder.markdown(full_response)
```

---

## 🎓 Complete Example: News Dashboard

See full implementation in `streamlit_apps/news_dashboard/`

**Features**:
- Real-time news analysis
- Sentiment visualization
- Source credibility scores
- Topic extraction
- Markdown + charts combined

**Run it**:
```bash
docker compose up streamlit-news

# Access: http://localhost:8502
```

---

## 🔧 Development Tips

### Tip 1: Hot Reload

Streamlit auto-reloads on file changes:
```bash
# Volume mount in docker-compose.yml
volumes:
  - ./streamlit_apps:/app/streamlit_apps
```

Just edit files, browser refreshes automatically!

---

### Tip 2: Streamlit Session State

Persist data across reruns:
```python
if "session_id" not in st.session_state:
    st.session_state.session_id = f"streamlit_{int(time.time())}"

# Use throughout app
session_id = st.session_state.session_id
```

---

### Tip 3: Error Handling

Always handle API errors gracefully:
```python
try:
    response = requests.post(...)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    st.error(f"Backend error: {e}")
except json.JSONDecodeError:
    st.error("Invalid response from backend")
```

---

### Tip 4: Loading States

Show users something is happening:
```python
with st.spinner("Analyzing news..."):
    response = requests.post(...)

# Or progress bar for multi-step agents
progress = st.progress(0)
for i, step in enumerate(steps):
    progress.progress((i + 1) / len(steps))
```

---

## 📊 When to Use Each Frontend

| Frontend | Best For | Complexity | Dev Time |
|----------|----------|------------|----------|
| **Custom HTML/JS** | Production apps, full control | High | Days |
| **Streamlit** | Dashboards, data viz, internal tools | Low | Hours |
| **ADK Web** | Development, debugging | None (built-in) | 0 min |

**Recommendation**:
- Development: ADK Web
- Internal tools/demos: Streamlit
- Production/public apps: Custom frontend

---

## 🚀 Deployment Considerations

### Development
```yaml
# docker-compose.yml
streamlit-chat:
  command: streamlit run app.py --server.port 8501
  volumes:
    - ./streamlit_apps:/app/streamlit_apps  # Hot reload
```

### Production
```yaml
# docker-compose.prod.yml
streamlit-chat:
  build: ./streamlit_apps/news_dashboard
  command: streamlit run app.py --server.port 8501 --server.address 0.0.0.0
  environment:
    - API_URL=https://api.yourdomain.com
  # No volume mount (baked in)
```

---

## 🔐 Security Notes

**Never**:
- ❌ Expose API keys in Streamlit code
- ❌ Allow Streamlit to call Gemini directly (bypass FastAPI)
- ❌ Store sensitive data in session_state

**Always**:
- ✅ Route through FastAPI backend
- ✅ Use environment variables for config
- ✅ Add authentication if exposing publicly
- ✅ Rate limit on FastAPI side

---

## 📚 Resources

- Streamlit docs: https://docs.streamlit.io
- Streamlit components: https://streamlit.io/components
- FastAPI + Streamlit examples: (see our examples)

---

**Next**: See `docs/PER_AGENT_FRONTENDS.md` for per-agent frontend architecture

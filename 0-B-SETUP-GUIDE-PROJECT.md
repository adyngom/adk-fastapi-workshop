# 🛠️ Project Setup Guide - Part 2

**Prerequisites**: Complete [Part 1: Google Cloud & API Key Setup](./0-SETUP-GUIDE.md) before proceeding.

## Step 1: Clone the Workshop Repository

### 1.1 Clone the Repo

Open your terminal and run:

```bash
git clone <repository-url>
cd adk-fastapi-workshop
```

*(Your instructor will provide the repository URL)*

### 1.2 Verify the Files

Check that you have these key files:

```bash
ls -la
```

You should see:
- `docker-compose.yml` ✅
- `.env.template` ✅
- `README.md` ✅
- `frontend/` directory ✅
- `api/` directory ✅

---

## Step 2: Configure Your Environment

### 2.1 Create Your `.env` File

Copy the template:

```bash
cp .env.template .env
```

### 2.2 Add Your API Key

Open `.env` in your code editor:

```bash
# Use your favorite editor
code .env          # VS Code
nano .env          # Terminal editor
```

### 2.3 Update the Configuration

Find this line:
```env
GOOGLE_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual API key from the previous setup guide:

```env
GOOGLE_API_KEY=AIzaSyC_your_actual_key_here
```

**Complete `.env` example**:
```env
# Google Cloud Project Client ID
GOOGLE_CLOUD_PROJECT=your-project-id

# Gemini API Configuration
GOOGLE_API_KEY=AIzaSyC_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Application Configuration
LOG_LEVEL=INFO
DEFAULT_MODEL=gemini-2.0-flash-exp

# Redis
REDIS_URL=redis://redis:6379

# MCP Server Configuration
MCP_ENABLED=false
MCP_SERVER_URL=http://mcp-server:3000

# CORS Configuration
# CORS_ORIGINS=http://localhost,http://127.0.0.1
```

### 2.4 Save the File

Save and close your editor.

**Security Check**:
- ✅ `.env` is listed in `.gitignore`
- ✅ Your API key will NOT be committed to Git
- ✅ Safe to develop locally

---

## Step 3: Start the Application

### 3.1 Make Sure Docker is Running

Check that Docker Desktop is running on your machine.

**Test Docker**:
```bash
docker --version
docker compose version
```

You should see version numbers (not errors).

### 3.2 Start All Services

From the project directory, run:

```bash
docker compose up
```

**What this does**:
- Downloads required Docker images (first time only)
- Starts Redis (in-memory database)
- Starts FastAPI backend (Python)
- Starts NGINX frontend (web server)

### 3.3 Watch the Startup Logs

You should see output like:

```
[+] Running 3/3
 ✓ Container adk-workshop-redis      Started
 ✓ Container adk-workshop-api        Started
 ✓ Container adk-workshop-frontend   Started
```

Then watch for this line:
```
adk-workshop-api  | INFO:     Application startup complete.
adk-workshop-api  | INFO:     Uvicorn running on http://0.0.0.0:8000
```

**This means you're ready!** 🎉

### 3.4 (Optional) Run in Background

To run containers in the background:

```bash
docker compose up -d
```

To view logs:
```bash
docker compose logs -f api
```

To stop:
```bash
docker compose down
```

---

## Step 4: Verify Everything Works

### 4.1 Test the Chat UI

1. **Open your browser**
2. **Navigate to**: http://localhost
3. **You should see**:
   - Title: "🤖 ADK Workshop Chat"
   - Status: "Connected" (in green)
   - Input box at the bottom

### 4.2 Test the Chatbot

1. **Type a message**: "Hello! Can you explain what you do?"
2. **Press Enter** or click **Send**
3. **Watch the response** appear word-by-word (streaming!)

✅ **If you see a streaming response, everything works!**

### 4.3 Check the API Documentation

1. **Open**: http://localhost:8000/docs
2. **You should see**: FastAPI interactive documentation
3. **Try the health endpoint**:
   - Click on `GET /api/health`
   - Click "Try it out"
   - Click "Execute"
   - You should get a 200 response: `{"status": "healthy"}`

### 4.4 Explore ADK Web Interface (Developer View)

1. **Open**: http://localhost/adk or http://localhost:3002
2. **You should see**: ADK Web Interface with tabs
3. **Test the interface**:
   - Send message: "Hello! I'm attending the ADK workshop"
   - Click **Events** tab (top of interface)
   - Watch events appear in real-time:
     - `agent_start`
     - `agent_response`
     - `agent_end`
   - Click on any event to expand and see details

✅ **If you see events populating, ADK Web is working!**

**What is ADK Web?**
- Developer debugging interface from Google
- See every step your agent takes
- Inspect requests, responses, and tool calls
- Perfect for understanding how agents work

---

## ⚠️ Troubleshooting

### Problem: "401 Unauthorized" Error

**Symptom**: Chat doesn't work, console shows "401 Unauthorized"

**Cause**: Invalid or missing API key

**Solution**:
1. Open `.env` and verify your API key:
   - Should start with `AIza`
   - No extra spaces or quotes
   - No line breaks

2. Get a fresh API key from https://aistudio.google.com/apikey

3. Update `.env` with the new key

4. Restart the API:
   ```bash
   docker compose restart api
   ```

---

### Problem: "Connection Error" in UI

**Symptom**: Status shows "Disconnected" or "Connection Error"

**Cause**: Backend not running or WebSocket connection failed

**Solution**:

1. Check if containers are running:
   ```bash
   docker compose ps
   ```
   All should show "Up" status

2. Check API logs for errors:
   ```bash
   docker compose logs api
   ```

3. Restart everything:
   ```bash
   docker compose down
   docker compose up
   ```

---

### Problem: Port Already in Use

**Symptom**: Error says "port is already allocated" (80 or 8000)

**Cause**: Another application is using the port

**Solution**:

**On Mac/Linux**:
```bash
# Find what's using port 80
sudo lsof -i :80

# Find what's using port 8000
sudo lsof -i :8000

# Kill the process (replace PID with actual process ID)
kill -9 PID
```

**On Windows**:
```powershell
# Find what's using the port (look at the last column for PID)
netstat -ano | findstr :8000

# Kill the process (replace <PID> with the actual number from above)
taskkill /PID <PID> /F

# Example: If PID is 1234
taskkill /PID 1234 /F
```

**Alternative**: Change ports in `docker-compose.yml` (not recommended for workshop)

---

### Problem: Docker Not Installed

**Symptom**: `docker: command not found`

**Solution**: Install Docker Desktop (requires Docker Desktop 4.0+)

- **Mac**: https://docs.docker.com/desktop/install/mac-install/ (Intel or Apple Silicon)
- **Windows**: https://docs.docker.com/desktop/install/windows-install/ (Windows 10/11 Pro,
Enterprise, or Education)
- **Linux**: https://docs.docker.com/desktop/install/linux-install/

---

### Problem: "Cannot connect to Docker daemon"

**Symptom**: Error about Docker daemon not running

**Solution**:
1. Open **Docker Desktop** application
2. Wait for it to fully start (whale icon in menu bar/system tray)
3. Try the command again

---

## 🧪 Pre-Workshop Checklist

Before the workshop starts, verify you can do all of these:

- [ ] Docker is installed and running
- [ ] Project is cloned to your machine
- [ ] `.env` file exists with your API key
- [ ] `docker compose up` starts all services successfully
- [ ] http://localhost shows the chat UI
- [ ] Chat UI status shows "Connected" (green)
- [ ] You can send a message and get a streaming response
- [ ] http://localhost:8000/docs shows API documentation
- [ ] http://localhost/adk shows ADK Web interface
- [ ] ADK Web Events tab shows agent activity
- [ ] No error messages in `docker compose logs`

---

## 🆘 Need Help?

If you're stuck:

1. **Check the troubleshooting section** above
2. **Ask in the workshop Slack/Discord** (if available)
3. **Arrive early to the workshop** for 1-on-1 help
4. **Email the instructor** with:
   - Error message (screenshot)
   - Output of `docker compose ps`
   - Output of `docker compose logs`

---

## 🎉 You're Ready!

Once you've completed all the steps and verified everything works, you're all set for the workshop!

**What to expect in the workshop**:
- Module 1: Understanding the Streaming Chatbot Architecture
- Module 2: Adding Tools & Function Calling
- Module 3: Multi-Agent Conversations
- Module 4: Persistent Storage with Redis
- Module 5: Production Deployment

**See you at the workshop!** 🚀

---

## 📚 Optional: Learn Docker Basics

If you're new to Docker, these concepts will help:

**Container**: Isolated environment that runs your app
**Image**: Blueprint for creating containers
**docker-compose.yml**: Configuration file for multi-container apps
**Volume**: Persistent storage for containers

**Useful commands**:
```bash
docker compose up        # Start services
docker compose down      # Stop and remove services
docker compose ps        # List running containers
docker compose logs api  # View API logs
docker compose restart api  # Restart API container
```

---

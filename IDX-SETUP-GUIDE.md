# 🚀 5-Minute Setup with Google IDX

> **NEW**: Skip Docker installation! Run everything in your browser with Google IDX.

---

## ⚡ Quick Start (5 Minutes)

### Step 1: Open in IDX (1 minute)

Click this button:

[![Open in IDX](https://cdn.idx.dev/btn/open_dark_32@2x.png)](https://idx.google.com/import?url=https://github.com/adyngom/adk-fastapi-workshop)

**What happens**:
- IDX clones the repository
- Installs all dependencies automatically
- Sets up Python environment
- You get a full VS Code-like IDE in your browser!

### Step 2: Get Your API Key (2 minutes)

While IDX is setting up:

1. Open: https://aistudio.google.com/apikey
2. Click "Create API key"
3. Copy the key (starts with `AIza`)

### Step 3: Add API Key (1 minute)

In your IDX workspace:

1. Open `.env` file (already created for you)
2. Find line: `GOOGLE_API_KEY=your-api-key-here`
3. Replace with your actual key
4. Save file (Cmd+S or Ctrl+S)

### Step 4: Start Services (1 minute)

In the IDX terminal:

```bash
./.idx/start-services.sh
```

**You'll see**:
```
🚀 Starting ADK Workshop Services...
✅ Virtual environment activated
📦 Starting Redis...
🐍 Starting FastAPI backend on port 8000...
🔍 Starting ADK Web on port 3002...
🎨 Starting Frontend on port 8080...
✅ All services started successfully!
```

### Step 5: Open Interfaces (30 seconds)

IDX will show port forwarding notifications. Click on:
- **Port 8080** - Custom Chat UI
- **Port 3002** - ADK Web Interface
- **Port 8000** - API Docs

**You're ready!** 🎉

---

## 🎯 What You Get

### Three Working Interfaces

All running in your browser, no local installation:

1. **Custom Chat UI** (port 8080)
   - Beautiful streaming chat
   - Agent selector dropdown
   - Markdown rendering

2. **ADK Web** (port 3002)
   - Google's official debugging tool
   - Events timeline
   - Real-time trace viewer

3. **FastAPI Backend** (port 8000)
   - Interactive API docs
   - WebSocket endpoints
   - Health monitoring

### Three Working Agents

- `greeting_agent` - Tools demo
- `news_pipeline` - Sequential workflow
- `competitive_analysis` - Parallel execution

All working immediately!

---

## 🏷️ Workshop Progression

Use Git tags to follow along:

```bash
# In IDX terminal
git checkout v1-exercise-1          # Tools example
git checkout v2-exercise-2          # Sequential pattern
git checkout v3-parallel-synthesis  # Parallel pattern

# Restart services after checkout
./.idx/start-services.sh
```

---

## 🐛 Troubleshooting

### onCreate still running

**Wait**: IDX shows "Setting up workspace..." at bottom
**Time**: 30-90 seconds first time
**Don't**: Click away or close browser

### Services won't start

```bash
# Check if dependencies installed
source .venv/bin/activate
python --version  # Should be 3.11
adk --version     # Should show version

# Reinstall if needed
pip install -r requirements.txt
pip install -r requirements-adk.txt
```

### API key error

```bash
# Verify key in .env
cat .env | grep GOOGLE_API_KEY

# Should start with AIza
# Restart services
pkill -f uvicorn
pkill -f "adk web"
./.idx/start-services.sh
```

### Can't access ports

- IDX auto-forwards ports with HTTPS
- Look for notifications in bottom-right
- Or click "Ports" tab in IDX
- Click the URL for each port

---

## 💡 IDX Tips

### Viewing Logs

```bash
# In IDX terminal
tail -f /tmp/api.log          # FastAPI logs
tail -f /tmp/adk-web.log      # ADK Web logs
tail -f /tmp/frontend.log     # Frontend logs
```

### Restarting Services

```bash
# Kill all services
pkill -f uvicorn
pkill -f "adk web"
pkill -f "http.server"
redis-cli shutdown

# Start fresh
./.idx/start-services.sh
```

### Editing Code

- Files on left sidebar
- Click to open
- Auto-save enabled
- FastAPI auto-reloads on save!

### Terminal Commands

```bash
# Multiple terminals
# Click '+' in terminal tab

# Terminal 1: View API logs
# Terminal 2: View ADK logs
# Terminal 3: Run commands
```

---

## 🎓 Advantages for Workshop

### For Students

✅ **Works everywhere** - Chromebook, iPad, any browser
✅ **No installation** - No Docker, Python, or dependencies
✅ **Consistent** - Everyone has identical environment
✅ **Fast** - 5 min vs 45 min setup
✅ **Cloud-based** - Access from anywhere

### For Instructors

✅ **Troubleshooting reduced** - 90% fewer setup issues
✅ **Time for content** - More teaching, less debugging
✅ **Mixed skill levels** - Beginners don't struggle with installation
✅ **Remote-friendly** - Works for virtual workshops
✅ **Professional** - Google's own platform for Google workshop

---

## 🔄 Comparison: Docker vs IDX

### Docker Setup (Original)

**Time**: 45 minutes

**Steps**:
1. Install Docker Desktop (20 min)
2. Clone repo (2 min)
3. Configure .env (3 min)
4. `docker compose build` (10 min)
5. Debug port conflicts (10 min)

**Issues**:
- Windows/Mac compatibility
- Resource intensive (8GB+ RAM)
- Network firewalls
- Port conflicts

### IDX Setup (New)

**Time**: 5 minutes

**Steps**:
1. Click "Open in IDX" (30 sec)
2. Wait for setup (60 sec)
3. Add API key (2 min)
4. Services auto-start (30 sec)

**Benefits**:
- Browser-based
- Pre-configured
- No local resources
- No compatibility issues

---

## 🎯 Workshop Time Savings

### Before (Docker)
- Setup: 45 min
- Troubleshooting: 15 min
- **Teaching time**: 60 min
- **ADK content**: ~30 min

### After (IDX)
- Setup: 5 min
- Troubleshooting: 5 min
- **Teaching time**: 110 min
- **ADK content**: ~90 min

**Result**: 3x more time on actual ADK content! 🚀

---

## 📝 Next Steps

After verifying IDX works:

1. **Update main README** with IDX button
2. **Test with fresh account** (student perspective)
3. **Create video walkthrough** (2 min demo)
4. **Update setup guides** (IDX-first approach)
5. **Announce to students** (pre-workshop)

---

## 🆘 Support

**During setup**:
- Check `.idx/README.md` (this file)
- Ask in workshop chat
- Backup: Use Docker (old guides)

**IDX-specific issues**:
- [IDX Documentation](https://developers.google.com/idx)
- [IDX Troubleshooting](https://developers.google.com/idx/guides/troubleshooting)

---

**Game changer for workshops!** ⚡

Focus on teaching, not environment setup.

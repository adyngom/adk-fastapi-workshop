# 🆘 IDX Setup Troubleshooting Guide

**Goal**: Get you from "stuck" to "coding" in under 5 minutes, no matter what went wrong.

---

## 🚨 When onCreate Fails

### Symptom: Workspace opened but no .venv folder

**This is the most common issue** - onCreate hook didn't run or failed silently.

**Quick Fix** (2 minutes):
```bash
# Run the manual setup script
./.idx/manual-setup.sh
```

This script:
- ✅ Creates virtual environment
- ✅ Installs all dependencies
- ✅ Sets up .env file
- ✅ Starts Redis
- ✅ Verifies everything is ready

**Then add your API key**:
```bash
# Edit .env and add: GOOGLE_API_KEY=your_key_here
# Get key from: https://aistudio.google.com/apikey
```

**Then start services**:
```bash
./.idx/start-services.sh
```

---

## 🚫 When onStart Fails

### Symptom: Preview shows "Error starting preview" or services not running

**Cause**: onStart hooks failed (missing venv, no API key, or command not found)

**Quick Fix** (30 seconds):
```bash
# If onCreate worked but services didn't start, just run:
./.idx/start-services.sh
```

**Common reasons onStart fails**:
- ❌ No .venv folder → Run `./.idx/manual-setup.sh` first
- ❌ No API key in .env → Add your key to `.env`
- ❌ Commands not found → Virtual environment not activated

**The onStart hooks will now tell you exactly what to do** if they fail.

---

## 🔐 When You Manually Cloned

### Symptom: Had to clone manually due to auth/permissions

**You're not stuck!** The manual setup script handles this:

```bash
# From project root
./.idx/manual-setup.sh
```

This is actually faster than waiting for onCreate in some cases.

---

## 📋 Step-by-Step Recovery

If the scripts don't work, here's the manual process:

### Step 1: Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate
```

**Verify**: `which python` should show `.venv/bin/python`

---

### Step 2: Install Dependencies
```bash
pip install --upgrade pip

# Install ADK first (avoids conflicts)
pip install -r requirements-adk.txt

# Then add FastAPI (without version pinning)
pip install fastapi uvicorn python-multipart websockets redis pydantic-settings
```

**Verify**: `adk --version` should show version number

**If fails**:
- Check Python version: `python --version` (need 3.11+)
- Check pip works: `pip --version`
- Try installing ADK separately: `pip install google-adk`

---

### Step 3: Configure Environment
```bash
# Create .env if missing
cp .env.template .env

# Edit and add your API key
# Get key from: https://aistudio.google.com/apikey
```

**Verify**: `cat .env | grep GOOGLE_API_KEY` should show your key

---

### Step 4: Start Services Manually

```bash
# Activate virtual environment
source .venv/bin/activate

# Export PYTHONPATH
export PYTHONPATH=$(pwd):$PYTHONPATH

# Start Redis (if available)
redis-server --daemonize yes --port 6379

# Start FastAPI (Terminal 1)
cd api
uvicorn main:app --host 0.0.0.0 --port 8000 --reload &

# Start ADK Web (Terminal 2)
cd adk_agents
adk web --host 0.0.0.0 --port 3002 &

# Start Frontend (Terminal 3)
cd frontend
python -m http.server 8080 &
```

---

## 🔍 Common Errors

### Error: "No module named 'api'"

**Cause**: PYTHONPATH not set

**Fix**:
```bash
export PYTHONPATH=$(pwd):$PYTHONPATH
# Then restart uvicorn
```

---

### Error: "adk: command not found"

**Cause**: Virtual environment not activated or ADK not installed

**Fix**:
```bash
source .venv/bin/activate
pip install google-adk
adk --version  # Verify
```

---

### Error: "Connection refused" on ports

**Cause**: Services not started or wrong ports

**Check what's running**:
```bash
lsof -i :8000  # FastAPI
lsof -i :3002  # ADK Web
lsof -i :8080  # Frontend
lsof -i :6379  # Redis
```

**If nothing shows**, services aren't running. Start them.

**If something shows**, services are running. Try accessing via IDX port forwarding.

---

### Error: "Invalid API key"

**Cause**: API key not set or incorrect

**Check**:
```bash
cat .env | grep GOOGLE_API_KEY
```

**Fix**:
1. Get new key from: https://aistudio.google.com/apikey
2. Edit .env
3. Replace with new key
4. Restart services

---

### Error: Redis connection failed

**Symptoms**: Session errors, WebSocket issues

**Check Redis**:
```bash
redis-cli ping
# Should return: PONG
```

**If Redis not running**:
```bash
redis-server --daemonize yes --port 6379
```

**If Redis not available**:
- IDX should have Redis pre-installed
- Check: `which redis-server`
- If missing, sessions won't persist (but agents still work)

---

## 🎯 Port Access in IDX

### Finding Your URLs

1. **Look for notifications** in bottom-right of IDX
   - "Port 8080 is available"
   - Click to open

2. **Use Ports panel**:
   - Click "View" → "Ports" (or bottom panel)
   - See all forwarded ports
   - Click "Open in Browser"

3. **Manual URL format**:
   ```
   https://{PORT}-idx-{PROJECT}-{HASH}.cluster{N}.idx.dev
   ```

### Expected Ports:
- **8080**: Custom chat UI (start here)
- **3002**: ADK Web interface (debugging)
- **8000**: FastAPI docs (API testing)

---

## 🧪 Verify Everything Works

### Quick Test Checklist:

```bash
# 1. Python environment
python --version
# Should be 3.11+

# 2. ADK installed
adk --version
# Should show version number

# 3. API key configured
cat .env | grep GOOGLE_API_KEY
# Should show key starting with AIza...

# 4. Services running
ps aux | grep -E "uvicorn|adk web|http.server"
# Should show 3 processes

# 5. Redis alive
redis-cli ping
# Should return PONG

# 6. Ports listening
lsof -i :8000 -i :3002 -i :8080
# Should show 3 listeners
```

---

## 📊 Time Expectations

| Task | Time | Cumulative |
|------|------|------------|
| Manual clone (if needed) | 30s | 30s |
| Run manual-setup.sh | 90s | 2min |
| Add API key | 30s | 2.5min |
| Start services | 10s | 2.5min |
| Access ports | 30s | 3min |
| Test first agent | 30s | 3.5min |

**Still under 5 minutes!** Even with onCreate failure.

---

## 🆘 Still Stuck?

### Nuclear Option: Fresh Start

```bash
# 1. Kill everything
pkill -f uvicorn
pkill -f "adk web"
pkill -f "http.server"

# 2. Clean environment
rm -rf .venv
rm .env

# 3. Run setup
./.idx/manual-setup.sh

# 4. Configure API key
# Edit .env and add GOOGLE_API_KEY

# 5. Start services
./.idx/start-services.sh
```

---

## 📝 Workshop Instructor Notes

### If Student Says "It's Not Working"

**Ask these questions**:
1. "Did onCreate finish?" → If no: manual-setup.sh
2. "Did you add API key?" → If no: Edit .env
3. "Do you see services running?" → If no: start-services.sh
4. "Can you access port 8080?" → If no: Check Ports panel

### Common Student Mistakes
- ❌ Forgot to activate .venv
- ❌ Didn't add API key
- ❌ Looking at wrong port
- ❌ Services not started

### Quick Student Commands

**Share this with stuck students**:
```bash
# If nothing works:
./.idx/manual-setup.sh
# Then add API key to .env
./.idx/start-services.sh
```

---

## 🎓 For TAs/Helpers

### Priority Order:
1. **Most common** (80%): onCreate didn't finish → manual-setup.sh
2. **Very common** (15%): API key not set → Edit .env
3. **Rare** (5%): Port access issues → Check Ports panel

### Don't Waste Time On:
- ❌ Explaining why onCreate failed
- ❌ Debugging Nix configuration
- ❌ Complex environment troubleshooting

### Just Do:
- ✅ Run manual-setup.sh
- ✅ Add API key
- ✅ Start services
- ✅ Move on to teaching

**Goal**: Get student to "Hello World" agent response in < 5 minutes, then keep moving.

---

## 🔄 Fallback: Docker

If IDX completely fails (network issues, IDX downtime, etc.):

```bash
# Clone locally
git clone https://github.com/adyngom/adk-fastapi-workshop.git
cd adk-fastapi-workshop

# Add API key
cp .env.template .env
# Edit .env

# Start with Docker
docker compose up --build
```

**Time**: 10-15 minutes (vs 5 minutes for IDX)

**But**: Still faster than individual local setup!

---

## ✅ Success Indicators

**You know it's working when**:
1. `adk --version` returns a version
2. `.env` has your API key
3. Port 8080 shows chat interface
4. Sending "Hello" gets a response
5. Agent selector shows 3 agents

**If all 5 work: You're ready to learn ADK!** 🚀

---

**Last Updated**: December 2025
**Next Review**: After first workshop with 25 students

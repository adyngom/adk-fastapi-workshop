# ⚡ ADK Workshop - Quick Start Card

**Goal**: From zero to first AI agent in 5 minutes

---

## 🎯 Two Paths to Success

### Path A: Happy Path (onCreate works)

1. **Click "Open in IDX"** button
2. **Wait** for onCreate to finish (~90 seconds)
3. **Edit .env** and add your API key
4. **Done!** Services start automatically

---

### Path B: Recovery Path (onCreate failed or manual clone)

1. **Run setup script**:
   ```bash
   ./.idx/manual-setup.sh
   ```
   ⏱️ Takes ~2 minutes

2. **Edit .env** and add your API key:
   ```bash
   # Get key from: https://aistudio.google.com/apikey
   # Add to .env: GOOGLE_API_KEY=your_key_here
   ```

3. **Start services**:
   ```bash
   ./.idx/start-services.sh
   ```
   ⏱️ Takes ~10 seconds

4. **Done!** Access the interfaces

---

## 🔑 Getting Your API Key

**1 minute setup**:

1. Go to: https://aistudio.google.com/apikey
2. Click "Create API key"
3. Copy the key (starts with `AIza...`)
4. Add to `.env` file:
   ```
   GOOGLE_API_KEY=AIzaYourActualKeyHere
   ```

---

## 🌐 Accessing the Interfaces

**Look for port notifications** (bottom-right of IDX):
- **Port 8080**: Click to open Custom Chat UI ← **Start here!**
- **Port 3002**: ADK Web debugging interface
- **Port 8000**: API documentation

Or use **Ports panel** (View → Ports):
- See all forwarded ports
- Click "Open in Browser" for each

---

## ✅ Quick Health Check

**Verify everything works**:

```bash
# 1. Python environment active?
python --version
# Should show: Python 3.11.x

# 2. ADK installed?
adk --version
# Should show version number

# 3. API key configured?
cat .env | grep GOOGLE_API_KEY
# Should show your key

# 4. Services running?
ps aux | grep -E "uvicorn|adk"
# Should show running processes

# 5. Test in browser
# Open port 8080, send "Hello" to greeting_agent
# Should get a friendly response
```

**All 5 pass? You're ready!** 🚀

---

## 🆘 Common Issues (1-minute fixes)

### Issue: "No .venv folder"
**Fix**:
```bash
./.idx/manual-setup.sh
```

### Issue: "Services won't start"
**Fix**:
```bash
# Kill everything
pkill -f uvicorn
pkill -f "adk web"

# Restart
./.idx/start-services.sh
```

### Issue: "Can't access ports"
**Fix**: Check Ports panel (View → Ports), click "Open in Browser"

### Issue: "Agent not responding"
**Fix**: Check API key in .env, make sure it starts with `AIza`

---

## 🎓 For TAs/Helpers

### Most Common Student Issue
**"onCreate didn't finish"** (10-20% of students)

**Solution** (say this verbatim):
> "No problem! Run this command: `./.idx/manual-setup.sh`"

**Recovery time**: 2 minutes

---

### Priority Checklist
When helping stuck students, check in order:

1. **[ ] .venv exists?** → If no: `manual-setup.sh`
2. **[ ] API key in .env?** → If no: Edit .env
3. **[ ] Services running?** → If no: `start-services.sh`
4. **[ ] Port 8080 accessible?** → If no: Check Ports panel

**90% of issues resolved by item #1**

---

### Don't Waste Time On:
- ❌ Why onCreate failed
- ❌ Debugging Nix configuration
- ❌ Alternative setup methods

### Just Do:
- ✅ Run manual-setup.sh
- ✅ Add API key
- ✅ Start services
- ✅ **Get back to teaching ADK!**

---

## 📋 Student Self-Help Commands

**Share these in chat for students to self-diagnose**:

```bash
# Complete recovery (if nothing works)
./.idx/manual-setup.sh && ./.idx/start-services.sh

# Just restart services
./.idx/start-services.sh

# Check what's running
ps aux | grep -E "uvicorn|adk web|http.server"

# View logs
tail -f /tmp/api.log
tail -f /tmp/adk-web.log
tail -f /tmp/frontend.log
```

---

## 🎯 Success Indicators

**Student is ready when**:
- ✅ Port 8080 shows chat interface
- ✅ Agent dropdown has 3 agents
- ✅ Status shows "Connected" (green)
- ✅ Sending "Hello" gets response
- ✅ Response streams in real-time

**If all 5 work: START WORKSHOP!** 🚀

---

## ⏱️ Time Expectations

| Scenario | Expected Time | Actual Time |
|----------|---------------|-------------|
| Path A (onCreate works) | 3 min | ___ min |
| Path B (manual-setup) | 5 min | ___ min |
| Troubleshooting (worst case) | 8 min | ___ min |

**Target**: 95% of students ready in < 5 minutes

---

## 📞 Need More Help?

- **Detailed guide**: `.idx/TROUBLESHOOTING.md`
- **IDX overview**: `.idx/README.md`
- **Workshop content**: `README.md` (main)

---

**Last Updated**: December 2025
**Tested with**: 25 students (upcoming)
**Success rate target**: 95%+ under 5 minutes

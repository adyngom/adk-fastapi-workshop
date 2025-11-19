# Pre-Workshop Setup Checklist

**ADK Workshop - Thursday**

**⏰ Complete this BEFORE the workshop** (takes 5 minutes)

---

## ✅ Step 1: Open in Google IDX (1 minute)

**Prerequisites:**
- Google account (free) - IDX requires Google login
- No GitHub account needed (repo is public)

Click this button to open the workshop in your browser:

[![Open in IDX](https://cdn.idx.dev/btn/open_dark_32@2x.png)](https://idx.google.com/import?url=https://github.com/adyngom/adk-fastapi-workshop)

**What happens**:
- Prompts you to sign in with Google (if not logged in)
- Opens Google IDX (browser-based development environment)
- Automatically clones the workshop repository
- Starts installing dependencies (watch the progress bar)

**If the button doesn't work**:
1. Go to https://idx.google.com
2. Sign in with your Google account
3. Click "New Workspace"
4. Choose "Clone from Git"
5. Paste: `https://github.com/adyngom/adk-fastapi-workshop`

---

## ✅ Step 2: Run Setup Script (2 minutes)

**In the IDX terminal** (bottom of screen), run:

```bash
./.idx/manual-setup.sh
```

**The script will**:
1. Create Python environment
2. Install Google ADK and dependencies (~90 seconds)
3. **Prompt you for API key** (next step)

---

## ✅ Step 3: Get Your Google API Key (1 minute)

When the script prompts for API key:

1. **Open this link** in new tab: https://aistudio.google.com/apikey
2. Click "Create API key"
3. **Copy the key** (starts with `AIza...`)
4. **Paste into the terminal** when prompted
5. Press Enter

The script validates and saves it automatically!

---

## ✅ Step 4: Start Services (30 seconds)

Still in the IDX terminal, run:

```bash
./.idx/start-services.sh
```

**You'll see**:
```
✅ All services started successfully!
FastAPI PID: XXXX
ADK Web PID: XXXX
Frontend PID: XXXX
```

---

## ✅ Step 5: Access the Workshop UI (30 seconds)

1. **Look for port notifications** (bottom-right) or click **"Ports"** panel (bottom)
2. **Find port 8501**
3. **Click "Open in Browser"**

**You should see**:
- "ADK Workshop Chat" interface
- Sidebar showing "Agents Loaded: 9"
- List of available agents:
  - greeting_agent (Step 1)
  - customer_service (Step 2)
  - content_pipeline (Step 3)
  - medical_authorization (Step 4)
  - financial_advisor (Step 5)
  - brand_intelligence (Step 6)
  - software_assistant (Step 7)
  - project_management (Step 8)
  - verified_recommendations (Step 9)

---

## ✅ Step 6: Test It Works (1 minute)

**In the Streamlit UI**:

1. **Agent should be selected**: "greeting_agent"
2. **Type**: "What time is it?"
3. **Click Send**
4. **Expected**: Shows current EST time

**If it works** - You're ready for Thursday! 🎉

---

## 🆘 Troubleshooting

### Issue: Setup script fails

**Solution**:
```bash
# Run it again (it's safe to re-run)
./.idx/manual-setup.sh
```

### Issue: "API key not found"

**Fix**:
```bash
# Edit .env file in IDX
# Add this line: GOOGLE_API_KEY=your_key_here
```

### Issue: Services won't start

**Try**:
```bash
# Kill old processes
pkill -f uvicorn
pkill -f "adk web"
pkill -f streamlit

# Start fresh
./.idx/start-services.sh
```

### Issue: Port 8501 shows blank screen

**Fix**:
```bash
# Make sure you created the Streamlit config
mkdir -p ~/.streamlit
cat > ~/.streamlit/config.toml << 'EOF'
[server]
enableCORS = false
enableXsrfProtection = false
serverAddress = "0.0.0.0"

[browser]
gatherUsageStats = false
EOF

# Restart Streamlit
pkill -f streamlit
streamlit run streamlit_apps/workshop_ui/app.py --server.port 8501 --server.address 0.0.0.0 &
```

---

## ✅ Confirmation

**Once you complete all steps**, reply to this email with:
- ✅ "Setup complete"
- Screenshot of the Streamlit UI showing the time response

**Or if you have issues**, reply with:
- What step you're stuck on
- Any error messages you see

---

## 📅 Workshop Day (Thursday)

**What to have ready**:
- IDX workspace open (from setup)
- Streamlit UI accessible (port 8501)

**We'll cover**:
- Foundation: Single agents with custom tools (Step 1)
- Real Workflows: Sequential multi-agent patterns (Steps 2-4)
- Intelligent Decision-Making: Parallel execution (Steps 5-6)
- Production Systems: MCP, orchestration, verification (Steps 7-9)
- BONUS: Built-in tools, multi-model strategies, deployment

**Time**: [Insert time]
**Duration**: 4 hours (9 agents total)

---

## 🔗 Quick Links

- **Setup help**: `.idx/QUICK-START.md` (in your IDX workspace)
- **Troubleshooting**: `.idx/TROUBLESHOOTING.md`
- **Questions**: [Your contact info]

---

**See you Thursday!** 🚀

If setup takes you more than 10 minutes or you get stuck, let me know ASAP so we can help before the workshop.

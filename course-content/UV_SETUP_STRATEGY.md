# UV Setup Strategy - Platform-Independent Course Setup

**Problem:** IDX might sunset, Docker has friction
**Solution:** UV by Astral - single tool, 10-100x faster than pip, works everywhere
**For:** Both ADK course and CS Concepts course

---

## 🎯 Why UV is Perfect for Your Courses

### **Problems Solved:**

**IDX Issues:**
- ✅ Platform dependency (Google might sunset)
- ✅ Requires Google account
- ✅ Browser-only (no local development)
- ✅ onCreate failures (we built manual-setup.sh to compensate)

**Docker Issues:**
- ✅ Intimidating for beginners
- ✅ Large downloads (images are GBs)
- ✅ Platform-specific issues (Mac vs Windows vs Linux)
- ✅ "Works on my machine" still happens

**Traditional pip/venv Issues:**
- ✅ Slow installations (minutes for ADK)
- ✅ Multiple tools (pip, venv, pip-tools)
- ✅ Version conflicts
- ✅ Environment confusion

### **UV Advantages:**

✅ **One tool:** Replaces pip, venv, pip-tools, pyenv
✅ **10-100x faster:** ADK installs in seconds, not minutes
✅ **Cross-platform:** Mac, Windows, Linux (no changes!)
✅ **Reproducible:** Lockfiles guarantee identical environments
✅ **Simple:** `uv sync` = everything working
✅ **No platform risk:** Open source, won't sunset

---

## 🚀 Student Setup (3 Minutes Total!)

### **Old Way (IDX/Docker):**
```bash
# IDX approach:
1. Click "Open in IDX" button
2. Wait for workspace to create (1-2 min)
3. Run .idx/manual-setup.sh (2-3 min)
4. Get API key
5. Run start-services.sh
Total: 5-8 minutes + Google account required

# Docker approach:
1. Install Docker Desktop (10-20 min)
2. Pull images (5-10 min)
3. docker-compose up
Total: 15-30 minutes + 2GB+ download
```

### **New Way (UV):**
```bash
# On Mac/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows:
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Then:
git clone https://github.com/adyngom/adk-fastapi-workshop
cd adk-fastapi-workshop
uv sync                    # Installs everything (10-30 seconds!)
uv run adk web            # Start ADK Web

Total: 3 minutes + no platform dependencies!
```

**10x faster setup than IDX!**

---

## 📋 Module 1 Recording Script Update

### **BEFORE (IDX-based):**

```
"Let's get your environment set up. We need Python 3.11+, a virtual environment,
and ADK installed.

First, create a virtual environment:
python -m venv .venv

Activate it:
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows

Install ADK:
pip install google-adk     # Takes 60-90 seconds

Verify:
adk --version
```

**Issues:**
- Platform-specific commands (Mac vs Windows)
- Slow pip install
- Multiple steps
- Students get confused with activation

---

### **AFTER (UV-based):**

```
"Let's get your environment set up. We're using UV - it's like pip and venv
combined into one super-fast tool.

First, install UV. On Mac or Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh

On Windows:
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

That's it - UV is installed. Takes 10 seconds.

Now, in your project directory:
uv sync

This installs ADK and all dependencies. Watch how fast this is...

[Shows completing in 10-20 seconds]

There you go! ADK is installed. That's it - one command.

To verify:
uv run adk --version

Perfect. You're ready to build agents."
```

**Benefits:**
- One install method (UV handles platform differences)
- One command (`uv sync`)
- 10x faster
- Students don't need to understand venv activation
- No confusion

---

## 📦 Course Repository Changes Needed

### **1. Add `pyproject.toml`** (UV's config file)

```toml
[project]
name = "adk-course"
version = "1.0.0"
description = "Ultimate AI Agents Masterclass"
requires-python = ">=3.11"
dependencies = [
    "google-adk>=1.18.0",
    "google-genai>=1.18.0",
    "fastapi>=0.115.0",
    "uvicorn[standard]>=0.31.0",
    "streamlit>=1.28.0",
    "python-dotenv>=1.0.1",
    "websockets>=15.0.1",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.3.3",
    "black>=24.10.0",
    "ruff>=0.7.0",
]

[tool.uv]
dev-dependencies = [
    "pytest>=8.3.3",
]
```

### **2. Add `uv.lock`** (Auto-generated)

```bash
uv lock  # Generates uv.lock file
```

**Students run:** `uv sync` → Identical environment instantly

---

### **3. Update Setup Instructions**

**New `QUICK_START.md`:**

```markdown
# Quick Start with UV (3 Minutes)

## Step 1: Install UV

**Mac/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Step 2: Clone and Setup

```bash
git clone https://github.com/adyngom/adk-fastapi-workshop
cd adk-fastapi-workshop
uv sync
```

## Step 3: Get API Key

1. Go to: https://aistudio.google.com/apikey
2. Create API key
3. Add to `.env`:
   ```
   GOOGLE_API_KEY=your_key_here
   ```

## Step 4: Run

```bash
uv run adk web
```

**That's it! Open localhost:3002**

Total time: 3 minutes
```

---

## 🎬 Recording Script Adjustments

### **Module 1: Environment Setup Section**

**NEW Script (30 seconds instead of 5 minutes!):**

```
SAY: "Okay, let's get your environment set up. We're using UV - it's the
     fastest way to install Python packages. Think of it as pip on steroids.

     Install UV with one command:
     [Show command for their OS]

     Then in your project directory:
     [Type: uv sync]

     Watch this...
     [Shows completing in 15 seconds]

     There you go! ADK and all dependencies installed. That's it.

     No virtual environments to activate, no pip install waiting, no platform
     differences. UV handles everything.

     Let's verify it worked:
     [Type: uv run adk --version]

     Perfect - version 1.18. We're ready to build agents.

     All right, so that's the setup. See how fast that was? Now let's talk
     about what makes ADK special..."
```

**Time saved:** 4-5 minutes from original pip/venv explanation!

---

## 💡 UV in Both Courses

### **ADK Course Benefits:**

**Module 1:** Faster setup (students stay engaged)
**Module 2:** Can skip venv complexity (UV handles it)
**Module 6:** Multiple projects easy (uv creates isolation)
**Module 9:** Deployment (uv.lock = reproducible prod environments)

**Student Experience:**
- 3-minute setup vs 10-15 minutes
- One tool to learn vs 4-5
- Works the same everywhere
- "It just works" feeling

---

### **CS Concepts Course Benefits:**

**Target audience:** Non-developers
**UV is PERFECT** for them:

- No need to understand virtual environments
- One command (`uv sync`)
- Fast = less frustration
- Cross-platform = no "my computer doesn't work"

**Example in Concept #6 (Loops):**

```
"Want to try this yourself? Install UV:
[one-line command]

Then:
uv run python loop_example.py

That's it. UV handles the environment automatically."
```

**Non-developers love this:** "I don't need to be a programmer to get this working"

---

## 📊 Platform Risk Comparison

| Platform | Risk | Setup Time | Friction | Maintenance |
|----------|------|------------|----------|-------------|
| **IDX** | ❌ HIGH (might sunset) | 5-8 min | Medium | Google-dependent |
| **Docker** | ✅ LOW | 15-30 min | HIGH | Container complexity |
| **pip/venv** | ✅ LOW | 10-15 min | Medium | Platform differences |
| **UV** | ✅ LOWEST | 3 min | LOW | "It just works" |

**UV is the winner for courses!**

---

## 🔄 Migration Strategy

### **What to Change in Course Materials:**

**1. Module 1 Recording Script:**
- ✅ Replace pip/venv section with UV (30 sec vs 5 min)
- ✅ Show one command: `uv sync`
- ✅ Emphasize speed (10-100x faster)

**2. Repository Structure:**
- ✅ Add `pyproject.toml` (UV config)
- ✅ Add `uv.lock` (reproducible environments)
- ✅ Keep requirements.txt for compatibility

**3. Student Setup Docs:**
- ✅ Update STUDENT_SETUP_CHECKLIST.md
- ✅ Update QUICK_START.md
- ✅ Remove IDX dependency

**4. All Module Scripts:**
- ✅ When running Python: `uv run python script.py`
- ✅ When running ADK: `uv run adk web`
- ✅ Consistent across all modules

---

## 🎯 Recommended Approach

### **Support Three Paths (Flexibility):**

**Path A: UV (Recommended - 90% of students)**
```
1. Install UV (one command)
2. uv sync (installs everything)
3. uv run adk web (start developing)
```
**Time:** 3 minutes
**Platform:** All (Mac, Windows, Linux)

**Path B: Docker (For advanced users who prefer containers)**
```
1. docker-compose up
```
**Time:** 5 minutes (after Docker installed)
**Platform:** All (but Docker install is slow)

**Path C: Traditional pip/venv (For enterprise with restrictions)**
```
1. python -m venv .venv
2. source .venv/bin/activate
3. pip install -r requirements.txt
```
**Time:** 10-15 minutes
**Platform:** All (but platform-specific activation)

**Focus on Path A in course. Mention B and C exist for specific needs.**

---

## 📝 Updated Quick Start (For Course)

### **Student Onboarding (Course Materials):**

**Module 1 Section: "Environment Setup"**

```
TITLE SLIDE: "3-Minute Setup with UV"

SAY: "We're using UV - the fastest Python package manager. It's going to make
     your life so much easier.

     On Mac or Linux, install UV:
     [Show: curl -LsSf https://astral.sh/uv/install.sh | sh]

     On Windows:
     [Show: powershell command]

     This installs UV. Takes about 10 seconds.

     Now clone the course repository:
     [Show: git clone https://github.com/adyngom/adk-course]

     Navigate into it:
     [Show: cd adk-course]

     And install everything:
     [Type: uv sync]

     Watch how fast this is...
     [Progress bar completes in 15 seconds]

     There you go! Python 3.11, ADK 1.18, FastAPI, Streamlit - everything
     installed in 15 seconds.

     With traditional pip, this would take 2-3 minutes. UV is 10x faster.

     Let's verify:
     [Type: uv run adk --version]

     Perfect - version 1.18. We're ready.

     Get your API key from aistudio.google.com, add it to .env, and we're
     building agents.

     That's the setup. See how simple UV makes this? Okay, let's talk about
     what makes ADK special..."
```

**Recording time:** 2 minutes vs 8 minutes with pip/venv explanation!

---

## 🎓 CS Concepts Course Integration

**UV is PERFECT for non-developers:**

### **Concept #6: Loops (Example)**

**Traditional Approach:**
```
"First, create a virtual environment... activate it... install dependencies..."
→ Non-developers give up here
```

**UV Approach:**
```
"Want to try this? Install UV with one command:
[copy-paste the curl command]

Then:
uv run python loop_example.py

That's it. UV handles the environment automatically. You don't need to
understand virtual environments - UV does that for you."
```

**Non-developer friendly!** No terminology, just works.

---

## 📊 Course Repository Structure with UV

```
adk-course/
├── pyproject.toml         # UV project config (NEW)
├── uv.lock               # Locked dependencies (NEW)
├── requirements.txt      # Backwards compatibility
├── .env.template         # API key template
├── adk_agents/          # All 9 agents
├── mini-apps/           # React UIs
├── course-content/      # Course materials
└── QUICK_START_UV.md    # New UV-based setup (NEW)
```

---

## ✅ Implementation Plan

### **Week 1 (Before Recording):**

**Day 1:**
- [ ] Create `pyproject.toml` for project
- [ ] Run `uv lock` to generate lockfile
- [ ] Test: `uv sync` installs everything correctly
- [ ] Verify: All agents work with `uv run adk web`

**Day 2:**
- [ ] Update Module 1 recording script (UV section)
- [ ] Create QUICK_START_UV.md
- [ ] Test on fresh machine (or VM)
- [ ] Verify 3-minute setup claim

**Day 3:**
- [ ] Update STUDENT_SETUP_CHECKLIST.md
- [ ] Make IDX optional (not required)
- [ ] Start recording Module 1 with UV!

---

## 🎬 Marketing Message Update

### **From:**
"Set up in 5 minutes with Google IDX"

### **To:**
"Set up in 3 minutes on any computer with UV"

**Better because:**
- No platform lock-in
- Works offline
- Faster
- More professional

---

## 💰 Business Impact

### **Course Perceived Value:**

**With IDX:**
- "Requires Google account"
- "Browser-only development"
- "What if IDX shuts down?"

**With UV:**
- "Works on any computer"
- "Professional developer workflow"
- "Future-proof"
- "10-100x faster installations"

**UV makes the course more valuable!**

---

## 🎯 Recommendation

### **SWITCH TO UV IMMEDIATELY**

**Before recording Module 1:**
1. Create pyproject.toml
2. Test UV setup (verify 3-minute claim)
3. Update Module 1 script (UV section)
4. Record with UV as primary path

**Benefits:**
- No IDX risk (platform-independent)
- Faster setup (better student experience)
- Simpler explanation (one tool vs many)
- Works for ADK AND CS Concepts courses

**Keep Docker as optional:**
- Some enterprises require containers
- Advanced users might prefer it
- But don't emphasize it in course

---

## 📋 Files to Create/Update

**NEW:**
- [ ] `pyproject.toml` (UV project config)
- [ ] `uv.lock` (generated by `uv lock`)
- [ ] `QUICK_START_UV.md` (3-minute setup guide)

**UPDATE:**
- [ ] Module 1 recording script (environment setup section)
- [ ] STUDENT_SETUP_CHECKLIST.md (UV as primary)
- [ ] README.md (UV installation)

**KEEP (but de-emphasize):**
- [ ] .idx/ directory (for those who used IDX workshop)
- [ ] docker-compose.yml (advanced option)

---

## ⏱️ Time Impact

**Setup time savings:** 5-8 minutes → 3 minutes (42% faster!)
**Installation speed:** 60-90 seconds → 10-15 seconds (6x faster!)
**Recording time saved:** 5 minutes per module (no need to explain venv!)

**Total across 14 modules:** 70 minutes saved in explanations
**Student satisfaction:** Higher (fewer setup headaches)

---

## ✅ Action Items for Next Session

1. **Create pyproject.toml for main repo**
2. **Test UV workflow end-to-end**
3. **Update Module 1 script (environment setup)**
4. **Create UV quick start guide**
5. **Start recording with UV as primary setup method**

**UV makes everything better - faster, simpler, platform-independent!** 🚀

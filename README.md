# 🚀 Building Production AI Agents with Google ADK

> **DevFest Atlanta 2025** - A hands-on workshop demonstrating ADK + FastAPI integration

[![ADK Version](https://img.shields.io/badge/ADK-v1.17.0-blue)](https://github.com/google/adk-python)
[![Workshop](https://img.shields.io/badge/Workshop-2%20hours-green)](https://devfest.gdg.org/)

---

## 🎯 What You'll Build

A production-ready AI agent system with **three interfaces**:

1. **Custom Chat UI** (http://localhost) - Beautiful user experience
2. **ADK Web Interface** (http://localhost/adk) - Google's debugging tools
3. **FastAPI Backend** (http://localhost:8000/docs) - API integration

**Three working agent examples**:
- ✅ Single agent with custom tools
- ✅ Sequential multi-agent workflow
- ✅ Parallel execution + synthesis

---

## ⚡ Quick Start

### Option 1: Google IDX (Recommended - 5 minutes) 🆕

**No installation needed!** Run everything in your browser.

[![Open in IDX](https://cdn.idx.dev/btn/open_dark_32@2x.png)](https://idx.google.com/import?url=https://github.com/adyngom/adk-fastapi-workshop)

#### Happy Path (onCreate works)
1. Click button above
2. Wait for setup (~60 seconds)
3. Add your API key to `.env`
4. Services start automatically!

#### Recovery Path (onCreate failed or manual clone)
```bash
# Run this if onCreate didn't complete:
./.idx/manual-setup.sh

# Then start services:
./.idx/start-services.sh
```

**Still under 5 minutes!** Even with onCreate failures.

**Resources**:
- 📖 [Quick Start Card](./.idx/QUICK-START.md) - One-page reference
- 🆘 [Troubleshooting Guide](./.idx/TROUBLESHOOTING.md) - Fix common issues
- 📚 [IDX Setup Details](./.idx/README.md) - Complete documentation

---

### Option 2: Local Docker (Traditional - 15 minutes)

**Prerequisites**:
- Docker Desktop installed and running
- Google Cloud account (free tier)
- Gemini API key from [AI Studio](https://aistudio.google.com/apikey)

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/adyngom/adk-fastapi-workshop.git
   cd adk-fastapi-workshop
   ```

2. **Configure environment**:
   ```bash
   cp .env.template .env
   # Edit .env and add your GOOGLE_API_KEY
   ```

3. **Start all services**:
   ```bash
   docker compose up -d
   ```

4. **Verify everything works**:
   - Custom UI: http://localhost ✅
   - ADK Web: http://localhost/adk ✅
   - API Docs: http://localhost:8000/docs ✅

**Detailed setup**: See [Setup Guide Part 1](./0-SETUP-GUIDE.md) and [Part 2](./0-B-SETUP-GUIDE-PROJECT.md)

---

## 🏷️ Workshop Checkpoints (Git Tags)

Learn progressively with working code at each stage:

| Tag | Description | What to Try |
|-----|-------------|-------------|
| `v0-starter-template` | Triple interface foundation | Explore all three interfaces |
| `v1-exercise-1` | Single agent + custom tools | Ask: "What time is it?" |
| `v2-exercise-2` | Sequential news pipeline | "Analyze AI news today" |
| `v3-parallel-synthesis` | Parallel competitive analysis | "Compare AI platforms" |

**Jump to any checkpoint**:
```bash
git checkout v2-exercise-2
docker compose restart adk-web
```

See [Workshop Checkpoints](./WORKSHOP_CHECKPOINTS.md) for details.

---

## 🏗️ Architecture

### Triple Interface Strategy

```
adk_agents/                     ← One agent definition
    ├── greeting_agent/
    ├── news_pipeline/
    └── competitive_analysis/
           ↓              ↓
    ADK Web         FastAPI
   (debugging)    (production)
           ↓              ↓
   localhost/adk    localhost
```

**Key insight**: Same agent works in both development (ADK Web) and production (FastAPI)!

### Docker Services

- **api**: FastAPI + WebSocket server (port 8000)
- **adk-web**: Google's ADK Web interface (port 3002)
- **frontend**: Custom chat UI via NGINX (port 80)
- **redis**: Session storage (port 6379)

---

## 📚 Working Agent Examples

### 1. greeting_agent (Single Agent + Tools)

**Location**: `adk_agents/greeting_agent/`

**Demonstrates**:
- Basic agent structure
- Custom Python function tools
- Tool calling and autonomous selection

**Custom Tools**:
```python
def get_workshop_info() -> dict:
    """Get workshop details"""
    return {...}

def get_current_time() -> dict:
    """Get current Atlanta time"""
    return {...}
```

**Try in ADK Web or Custom UI**:
```
"What workshop is this?"
"What time is it?"
"What agents are available?"
```

Watch the Events tab show `tool_call` and `tool_result`!

---

### 2. news_pipeline (Sequential Workflow)

**Location**: `adk_agents/news_pipeline/`

**Demonstrates**:
- SequentialAgent pattern
- State passing with output_key
- Placeholder syntax {key} in instructions

**Flow**:
```
news_gatherer (searches) → output: news_articles
    ↓
summarizer (reads {news_articles}) → output: summary
    ↓
sentiment_analyzer (reads {summary}) → output: analysis
```

**Try**:
```
"Analyze tech news from today"
```

---

### 3. competitive_analysis (Parallel + Synthesis)

**Location**: `adk_agents/competitive_analysis/`

**Demonstrates**:
- ParallelAgent for concurrent execution
- 2-3x performance improvement
- Synthesis pattern to combine results

**Flow**:
```
[competitor_a_analyst]
[competitor_b_analyst]  ← All run in parallel
[competitor_c_analyst]
        ↓
   synthesizer (combines all data)
```

**Performance**:
- Sequential: 30s × 3 = 90 seconds
- Parallel: 30s + synthesis = 40 seconds

**Try**:
```
"Compare AI platforms from Google, Microsoft, and Amazon"
```

---

## 🔍 Key Features

### For Students

✅ **Working code from day one** - No setup struggles
✅ **Progressive learning** - Git tags as checkpoints
✅ **Visual debugging** - ADK Web Events timeline
✅ **Production patterns** - FastAPI integration, Docker orchestration
✅ **Post-workshop exploration** - Complete examples to extend

### For Instructors

✅ **Proven architecture** - All code tested and working
✅ **Multiple teaching modes** - Show & tell, exploration, live coding
✅ **Recovery mechanism** - Git tags for catching up
✅ **Google-native tooling** - Official ADK Web interface
✅ **Real-world integration** - Not just toy examples

---

## 🛠️ Development Commands

### Managing Services

```bash
# Start all services
docker compose up -d

# Start with logs visible
docker compose up

# View logs
docker compose logs -f api        # API logs
docker compose logs -f adk-web    # ADK Web logs
docker compose logs --tail=50 api # Last 50 lines

# Restart specific service
docker compose restart adk-web
docker compose restart api

# Rebuild after dependency changes
docker compose build adk-web
docker compose up -d adk-web

# Stop everything
docker compose down

# Full cleanup (removes volumes)
docker compose down -v
```

### Accessing Services

```bash
# Check service status
docker compose ps

# Execute commands in containers
docker compose exec api python --version
docker compose exec adk-web ls adk_agents/

# View environment variables
docker compose exec api env | grep GOOGLE
```

---

## 📖 Project Structure

```
adk-fastapi-workshop/
├── adk_agents/              # ADK agent definitions (SINGLE SOURCE OF TRUTH)
│   ├── greeting_agent/      # v1: Single agent + tools
│   │   ├── agent.py        # Agent definition
│   │   ├── tools.py        # Custom Python tools
│   │   └── __init__.py
│   ├── news_pipeline/       # v2: Sequential pattern
│   │   ├── agent.py        # Pipeline coordinator
│   │   └── sub_agents/     # Pipeline agents
│   │       ├── news_gatherer/
│   │       ├── summarizer/
│   │       └── sentiment_analyzer/
│   └── competitive_analysis/ # v3: Parallel pattern
│       ├── agent.py         # Parallel + synthesis coordinator
│       └── sub_agents/      # Research + synthesis agents
│           ├── competitor_a/
│           ├── competitor_b/
│           ├── competitor_c/
│           └── synthesizer/
├── agents/                  # FastAPI integration layer
│   └── manager.py          # Loads ADK agents for FastAPI
├── api/                     # FastAPI application
│   ├── main.py             # WebSocket endpoints
│   ├── routes/             # REST endpoints
│   └── models/             # Pydantic schemas
├── frontend/                # Custom chat UI
│   └── index.html          # WebSocket client with markdown
├── config/                  # Application settings
│   └── settings.py         # Pydantic settings
├── docker-compose.yml       # Service orchestration
├── Dockerfile              # API container
├── Dockerfile.adk          # ADK Web container
├── requirements.txt        # FastAPI dependencies
└── requirements-adk.txt    # ADK dependencies
```

---

## 🎓 Workshop Materials

### Setup Guides
- [0-SETUP-GUIDE.md](./0-SETUP-GUIDE.md) - Google Cloud & API key
- [0-B-SETUP-GUIDE-PROJECT.md](./0-B-SETUP-GUIDE-PROJECT.md) - Project setup
- [WORKSHOP_CHECKPOINTS.md](./WORKSHOP_CHECKPOINTS.md) - Git tag guide

### Internal Documentation (docs/)
- Slide deck (22 slides, all code verified)
- ADK Web interface guide
- Architecture diagrams
- Teaching notes

---

## 🐛 Troubleshooting

### Services won't start

```bash
docker compose ps              # Check status
docker compose logs api        # View errors
docker compose down            # Stop all
docker compose up -d --build   # Rebuild and start
```

### API key errors

```bash
cat .env | grep GOOGLE_API_KEY  # Verify key
# Should start with AIza
docker compose restart api adk-web
```

### ADK Web shows "no agents"

- Verify agent.py has `root_agent` variable
- Check folder name matches agent name
- Restart: `docker compose restart adk-web`

### Port conflicts

```bash
# Port 80 or 8000 in use
sudo lsof -i :80        # Find process
sudo lsof -i :8000
# Or change ports in docker-compose.yml
```

---

## 📚 Learning Resources

### Official Google Resources
- [ADK Documentation](https://google.github.io/adk-docs/)
- [ADK Python Repo](https://github.com/google/adk-python)
- [ADK Samples](https://github.com/google/adk-samples)
- [Google Codelabs](https://codelabs.developers.google.com/) (search: ADK)

### Post-Workshop Learning
- Complete Google Codelabs at your own pace
- Explore ADK samples repository (25+ examples)
- DeepLearning.AI ADK course (voice agents)
- Join ADK community calls (monthly)

---

## 🎯 What Makes This Workshop Unique

### Not Just ADK, But Production Integration

Most ADK tutorials show:
- ✅ ADK Web interface only

This workshop shows:
- ✅ ADK Web (debugging)
- ✅ Custom Frontend (branded UX)
- ✅ FastAPI integration (real-world deployment)
- ✅ Docker orchestration (production-ready)

### Same Agent, Multiple Interfaces

Write once in `adk_agents/`, use everywhere:
- Develop & debug in ADK Web
- Deploy via FastAPI
- Serve through custom UI

**Single source of truth** = easier maintenance!

---

## 🚀 Extending the Workshop

### Add Your Own Agent

1. Create folder: `adk_agents/my_agent/`
2. Create `agent.py`:
   ```python
   from google.adk.agents import Agent

   root_agent = Agent(
       name="my_agent",
       model="gemini-2.0-flash",
       description="What it does",
       instruction="How it behaves"
   )
   ```
3. Add to manager: `agents/manager.py`
4. Restart: `docker compose restart adk-web api`

### Add Custom Tools

1. Create `tools.py` in agent folder
2. Write functions with docstrings
3. Import and add to agent's `tools=[]`
4. Agent uses them autonomously!

---

## 📜 License

Educational materials for workshop purposes.

**Based on**:
- [Google ADK](https://github.com/google/adk-python) - Apache 2.0
- Google Cloud Labs materials
- Community contributions

---

## 🙏 Acknowledgments

- Google ADK Team
- DevFest Atlanta organizers
- Workshop participants

---

## 📞 Support

- Workshop: Ask instructor or TAs
- Issues: [GitHub Issues](https://github.com/adyngom/adk-fastapi-workshop/issues)
- Community: [ADK Discussions](https://github.com/google/adk-python/discussions)

---

**Ready to build production AI agents?** 🚀

**Workshop**: October 31, 2025 | DevFest Atlanta | 2 hours

*Clone, explore, extend. Happy agent building!*

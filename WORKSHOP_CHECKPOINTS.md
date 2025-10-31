# 🏷️ Workshop Checkpoints

> **Never get lost!** This workshop uses Git tags as learning checkpoints. Jump to any stage instantly.

---

## 🎯 How This Works

Each Git tag represents a **complete, working state** of the project. If you fall behind during the workshop, just checkout the current tag and you're synchronized!

```bash
# Jump to any checkpoint
git checkout v2-multi-agent-system

# Restart services
docker compose restart adk-web

# You're caught up! ✅
```

---

## 📚 Available Checkpoints

### v0-starter-template (START HERE)

**What it is**: Complete working system with three interfaces

**Includes**:
- ✅ Custom chat UI (http://localhost)
- ✅ ADK Web debugging interface (http://localhost/adk)
- ✅ FastAPI backend (http://localhost:8000/docs)
- ✅ greeting_agent ready to explore

**Learn**: Architecture, streaming, WebSockets, Docker orchestration

**Try**: Send messages to all three interfaces, compare experiences

---

### v1-custom-tools

**What's new**: greeting_agent can now call Python functions

**Capabilities added**:
- `get_workshop_info()` - Workshop details
- `get_current_time()` - Current Atlanta time
- Tool calling visualization in Events tab

**Learn**: How agents use tools autonomously, function calling patterns

**Try**: Ask "What time is the workshop?" and watch tool execution in Events

---

### v2-multi-agent-system

**What's new**: Three specialized agents working together

**Agents**:
- `coordinator_agent` - Routes work to specialists
- `researcher_agent` - Searches web for information
- `writer_agent` - Creates content from research

**Learn**: Agent-as-a-tool pattern, specialization vs generalization

**Try**: Ask coordinator a question requiring research + writing

---

### v3-sequential-pipeline

**What's new**: News analysis pipeline with ordered execution

**Flow**: Gatherer → Summarizer → Sentiment Analyzer

**Learn**: Sequential workflows, state passing, output_key usage

**Try**: "Analyze tech news from today" and watch 3-step pipeline

---

### v4-parallel-synthesis

**What's new**: Concurrent agent execution + synthesis

**Performance**: 2-3x faster than sequential for independent tasks

**Learn**: When to parallelize, synthesis patterns, performance optimization

**Try**: "Compare three tech companies" and see concurrent execution

---

### v5-production-ready

**What's new**: Security, validation, monitoring

**Production features**:
- Input validation callbacks
- Output moderation
- Human-in-the-loop (HITL)
- Audit logging
- Monitoring integration

**Learn**: Production vs prototype, enterprise deployment, security

**Try**: Attempt sensitive operations, see HITL confirmation prompts

---

## 🚀 Quick Start

### During Workshop

```bash
# Instructor will say: "Everyone checkout v2..."
git checkout v2-multi-agent-system
docker compose restart adk-web

# When services are up, explore the new features
```

### After Workshop

```bash
# Start from beginning
git checkout v0-starter-template

# Progress at your own pace
git checkout v1-custom-tools
git checkout v2-multi-agent-system
# etc.

# Return to latest
git checkout main
```

---

## 🔍 Exploring Tags

### See What Changed

```bash
# View tag description
git show v2-multi-agent-system

# See file changes
git diff v1-custom-tools v2-multi-agent-system

# List all files in specific tag
git ls-tree -r v3-sequential-pipeline --name-only
```

### See All Checkpoints

```bash
# List tags
git tag -l

# List with descriptions
git tag -l -n5
```

---

## 💡 Pro Tips

**Falling behind?**
- Don't stress
- Checkout current tag
- Continue learning

**Want to experiment?**
```bash
# Create your own branch from any tag
git checkout v2-multi-agent-system
git checkout -b my-experiments
# Break things, learn, no consequences!
```

**After workshop**:
- Work through each tag
- Understand changes between tags
- Build confidence progressively

---

## 🎓 Learning Path

### Self-Paced (Post-Workshop)

**Day 1**: Explore v0-v2
- Understand architecture
- See tools in action
- Observe multi-agent collaboration

**Day 2**: Study v3-v4
- Learn workflow patterns
- Understand performance optimization
- Compare sequential vs parallel

**Day 3**: Implement v5
- Add security features
- Configure monitoring
- Prepare for production

**Week 1**: Build your own system
- Choose pattern that fits
- Implement your use case
- Deploy and iterate

---

## 🐛 Troubleshooting

### Tag Checkout Not Working

```bash
# Ensure clean state
git status

# Stash changes if needed
git stash

# Now checkout
git checkout v2-multi-agent-system

# Retrieve stashed changes (optional)
git stash pop
```

### Services Not Starting After Checkout

```bash
# Full restart
docker compose down
docker compose up -d

# Check logs
docker compose logs adk-web
```

### Not Sure Which Tag You're On

```bash
# Show current tag
git describe --tags

# Show all tags
git tag -l
```

---

## ✅ Workshop Success Criteria

After each checkpoint, verify:

**v0**: All three interfaces accessible and working
**v1**: Tool calls visible in ADK web Events
**v2**: Agent-to-agent communication in Events timeline
**v3**: Sequential execution with state building up
**v4**: Parallel execution with timing improvements
**v5**: Security callbacks and HITL working

---

## 📖 Additional Resources

- **Setup Guides**: See `0-SETUP-GUIDE.md` and `0-B-SETUP-GUIDE-PROJECT.md`
- **Review Checklist**: `REVIEW_CHECKLIST.md` (for TAs/instructors)
- **Questions?**: Ask instructor or check troubleshooting guides

---

**Remember**: These checkpoints are your safety net. Use them freely!

**Goal**: Learn at your pace, never fall behind, build confidence progressively.

🚀 **Happy building!**

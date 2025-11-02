# 🚀 Google IDX Configuration

This folder contains configuration for running the ADK FastAPI Workshop in Google IDX (Project IDX).

## ✨ Benefits of IDX

**5-minute setup** instead of 45 minutes!

| Feature | Local (Docker) | Google IDX |
|---------|---------------|------------|
| Setup time | 45 min | 5 min |
| Requirements | Docker, Git, API key | Just API key |
| Works on | Mac/Windows/Linux | Any browser |
| Team consistency | Different environments | Same for everyone |
| Workshop focus | 30 min on ADK | 90+ min on ADK |

---

## 📋 What's Included

### `dev.nix`
- Nix configuration for reproducible environment
- Python 3.11 with all dependencies
- Redis, NGINX pre-installed
- Auto-start scripts
- Port configurations

### `start-services.sh`
- Starts all services (API, ADK Web, Frontend)
- Health checks
- Logging setup
- PID tracking for easy shutdown

### `icon.png`
- Template icon for IDX workspace

---

## 🎯 How It Works

### When Student Opens in IDX

1. **Clone happens automatically** (via Open in IDX button)
2. **onCreate runs** (installs dependencies)
3. **onStart runs** (starts services)
4. **Student adds API key** (only manual step)
5. **Ready to code!** (< 5 minutes)

### Service Architecture in IDX

```
IDX Workspace
├── FastAPI (port 8000) - Backend API
├── ADK Web (port 3002) - Debugging UI
├── Frontend (port 8080) - Custom chat
└── Redis (port 6379) - Sessions
```

All accessible via IDX's port forwarding with HTTPS!

---

## 🔧 Customization

### Adding Packages

Edit `dev.nix`:
```nix
packages = [
  pkgs.python311
  pkgs.your-package-here
];
```

### Changing Ports

IDX auto-forwards ports, but you can customize in:
- `start-services.sh` - Update port numbers
- Frontend code - Update WebSocket URLs to use IDX domain

### Auto-Start Behavior

Edit `dev.nix` → `workspace.onStart`:
```nix
onStart = {
  custom-command = ''
    echo "Running custom setup..."
  '';
};
```

---

## 🐛 Troubleshooting

### Services not starting

```bash
# Check logs
tail -f /tmp/api.log
tail -f /tmp/adk-web.log
tail -f /tmp/frontend.log

# Manually restart
./.idx/start-services.sh
```

### Port conflicts

```bash
# Find what's using ports
lsof -i :8000
lsof -i :3002
lsof -i :8080

# Kill and restart
pkill -f uvicorn
pkill -f "adk web"
./.idx/start-services.sh
```

### API key not working

```bash
# Verify .env
cat .env | grep GOOGLE_API_KEY

# Should start with AIza
# Re-source environment
source .venv/bin/activate
```

---

## 📚 For Workshop Instructors

### Benefits

✅ **Consistent environment** - Everyone has identical setup
✅ **Fast onboarding** - Students ready in 5 minutes
✅ **No installation issues** - Works in browser
✅ **Focus on content** - Not troubleshooting Docker
✅ **Accessible** - Works on Chromebooks, tablets

### Setup Checklist

Before workshop:
- [ ] Test "Open in IDX" button
- [ ] Verify all services start correctly
- [ ] Test with fresh Google account
- [ ] Check port forwarding works
- [ ] Prepare backup local environment

During workshop:
- [ ] Share IDX template URL
- [ ] Guide through API key setup
- [ ] Verify everyone sees all 3 interfaces
- [ ] Have troubleshooting ready

---

## 🔗 Creating the Template

### 1. Make Repository Public Template

In GitHub settings:
- ✅ Enable "Template repository"
- ✅ Add topics: `google-idx`, `adk`, `workshop`

### 2. Add IDX Badge

In main README.md:
```markdown
[![Open in IDX](https://cdn.idx.dev/btn/open_dark_32@2x.png)](https://idx.google.com/import?url=https://github.com/adyngom/adk-fastapi-workshop)
```

### 3. Test Template

1. Click "Open in IDX" button
2. Wait for onCreate (30-60 seconds)
3. Add API key to .env
4. Verify all services running
5. Test all three interfaces

---

## 🎓 Student Experience

### With Docker (Old Way)
1. Install Docker (20 min)
2. Clone repo (2 min)
3. Configure .env (3 min)
4. Build images (10 min)
5. Debug issues (10 min)
**Total: ~45 minutes**

### With IDX (New Way)
1. Click "Open in IDX" (30 sec)
2. Wait for setup (60 sec)
3. Add API key to .env (2 min)
4. Services auto-start (30 sec)
5. Start learning! (immediate)
**Total: ~5 minutes**

---

## 🚀 Next Steps

After IDX setup working:

1. **Test with real workshop** (dry run)
2. **Create video walkthrough** (2 min setup demo)
3. **Update setup guides** (IDX-first, Docker as backup)
4. **Share with TAs** (get feedback)
5. **Announce to students** (pre-workshop email)

---

**Result**: More time teaching ADK, less time fighting environments! 🎉

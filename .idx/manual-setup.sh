#!/bin/bash

# =============================================================================
# IDX Manual Setup Script
# =============================================================================
# Use this if onCreate fails or you manually cloned the repo
# This is the "emergency recovery" path for 5-minute setup
# =============================================================================

set -e  # Exit on any error

echo "🔧 Starting ADK Workshop Manual Setup..."
echo ""

# =============================================================================
# Step 1: Detect Project Root
# =============================================================================
echo "📂 Step 1/5: Finding project directory..."

if [ -f "requirements.txt" ]; then
    PROJECT_ROOT=$(pwd)
    echo "✅ Found project at: $PROJECT_ROOT"
else
    echo "❌ ERROR: Can't find requirements.txt"
    echo "   Please run this script from the project root directory"
    exit 1
fi

# =============================================================================
# Step 2: Python Environment
# =============================================================================
echo ""
echo "🐍 Step 2/5: Setting up Python environment..."

# Check Python version
PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}' | cut -d. -f1,2)
echo "   Found Python $PYTHON_VERSION"

if [ ! -d ".venv" ]; then
    echo "   Creating virtual environment..."
    python -m venv .venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "   Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "   Upgrading pip..."
pip install --upgrade pip --quiet

# Install dependencies
# Note: requirements.txt has conflicts (ADK vs FastAPI Starlette versions)
# In IDX single environment, install requirements-adk.txt first, then add FastAPI deps
echo "   Installing ADK dependencies (~30 seconds)..."
pip install -r requirements-adk.txt --quiet

echo "   Installing FastAPI and supporting libraries (~30 seconds)..."
# Install FastAPI deps without version pinning to avoid conflicts with ADK
pip install fastapi uvicorn python-multipart websockets redis pydantic-settings --quiet

echo "✅ Python dependencies installed"

# Verify ADK installed
if command -v adk &> /dev/null; then
    ADK_VERSION=$(adk --version 2>&1 || echo "unknown")
    echo "   ADK version: $ADK_VERSION"
else
    echo "❌ ERROR: ADK not found after installation"
    exit 1
fi

# =============================================================================
# Step 3: Environment Configuration
# =============================================================================
echo ""
echo "⚙️  Step 3/5: Configuring environment..."

if [ ! -f ".env" ]; then
    echo "   Creating .env from template..."
    cp .env.template .env
    echo "✅ Created .env file"
    echo ""
    echo "⚠️  IMPORTANT: You need to add your API key!"
    echo "   1. Get key from: https://aistudio.google.com/apikey"
    echo "   2. Open .env file"
    echo "   3. Replace 'your_key_here' with actual key"
    echo ""
else
    echo "✅ .env file already exists"
fi

# Check if API key is set
if grep -q "your_key_here" .env 2>/dev/null; then
    echo "⚠️  WARNING: API key not yet configured"
    echo "   Edit .env and add your GOOGLE_API_KEY"
elif grep -q "GOOGLE_API_KEY=" .env 2>/dev/null; then
    echo "✅ API key appears to be configured"
else
    echo "⚠️  WARNING: Can't find GOOGLE_API_KEY in .env"
fi

# =============================================================================
# Step 4: Redis Check
# =============================================================================
echo ""
echo "🗄️  Step 4/5: Checking Redis..."

if command -v redis-server &> /dev/null; then
    echo "✅ Redis available"

    # Check if Redis is already running
    if pgrep -x "redis-server" > /dev/null; then
        echo "✅ Redis already running"
    else
        echo "   Starting Redis..."
        redis-server --daemonize yes --port 6379
        sleep 1
        if pgrep -x "redis-server" > /dev/null; then
            echo "✅ Redis started"
        else
            echo "⚠️  WARNING: Redis failed to start"
            echo "   Services may not work correctly"
        fi
    fi
else
    echo "⚠️  WARNING: Redis not found"
    echo "   Session management may not work"
fi

# =============================================================================
# Step 5: Service Readiness
# =============================================================================
echo ""
echo "🚀 Step 5/5: Checking service readiness..."

# Check required directories
DIRS=("api" "adk_agents" "frontend")
for dir in "${DIRS[@]}"; do
    if [ -d "$dir" ]; then
        echo "✅ $dir/ exists"
    else
        echo "❌ ERROR: Missing $dir/ directory"
        exit 1
    fi
done

# Check critical files
FILES=("api/main.py" "adk_agents/greeting_agent/agent.py" "frontend/index.html")
for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file exists"
    else
        echo "❌ ERROR: Missing $file"
        exit 1
    fi
done

# =============================================================================
# Summary
# =============================================================================
echo ""
echo "═══════════════════════════════════════════════════════════"
echo "✅ Setup Complete!"
echo "═══════════════════════════════════════════════════════════"
echo ""
echo "📝 Next Steps:"
echo ""
echo "1. Make sure your API key is in .env:"
echo "   - Edit: .env"
echo "   - Add: GOOGLE_API_KEY=your_actual_key"
echo ""
echo "2. Start all services:"
echo "   ./.idx/start-services.sh"
echo ""
echo "3. Access the interfaces:"
echo "   - Custom UI: Port 8080 (frontend)"
echo "   - ADK Web: Port 3002 (debugging)"
echo "   - API Docs: Port 8000/docs (backend)"
echo ""
echo "═══════════════════════════════════════════════════════════"
echo ""

# =============================================================================
# Health Check Info
# =============================================================================
echo "🔍 Quick Health Check Commands:"
echo ""
echo "   Check Python: python --version"
echo "   Check ADK: adk --version"
echo "   Check API key: cat .env | grep GOOGLE_API_KEY"
echo "   Check Redis: redis-cli ping"
echo "   View logs: tail -f /tmp/*.log"
echo ""
echo "Need help? See .idx/TROUBLESHOOTING.md"
echo ""

#!/bin/bash
# IDX Workshop Services Startup Script
# Starts all services needed for the ADK workshop in Google IDX

set -e

echo "🚀 Starting ADK Workshop Services..."

# Activate virtual environment
if [ -d ".venv" ]; then
    source .venv/bin/activate
    echo "✅ Virtual environment activated"
else
    echo "❌ Virtual environment not found. Run onCreate tasks first."
    exit 1
fi

# Check for API key
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found. Creating from template..."
    cp .env.template .env
    echo "📝 Please add your GOOGLE_API_KEY to .env file"
    exit 1
fi

# Verify API key is set
if ! grep -q "GOOGLE_API_KEY=AIza" .env; then
    echo "⚠️  GOOGLE_API_KEY not configured in .env"
    echo "Please add your API key from https://aistudio.google.com/apikey"
    exit 1
fi

# Start Redis
echo "📦 Starting Redis..."
redis-server --daemonize yes --port 6379 2>/dev/null || echo "Redis already running"
sleep 1

# Start FastAPI Backend
echo "🐍 Starting FastAPI backend on port 8000..."
# Set PYTHONPATH to include project root (get absolute path)
PROJECT_ROOT=$(pwd)
export PYTHONPATH=$PROJECT_ROOT:$PYTHONPATH
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload > /tmp/api.log 2>&1 &
API_PID=$!
echo "   FastAPI PID: $API_PID"
echo "   PYTHONPATH: $PYTHONPATH"
sleep 2

# Start ADK Web Interface
echo "🔍 Starting ADK Web on port 3002..."
cd adk_agents
adk web --host 0.0.0.0 --port 3002 > /tmp/adk-web.log 2>&1 &
ADK_PID=$!
echo "   ADK Web PID: $ADK_PID"
cd ..
sleep 2

# Start Frontend Server
echo "🎨 Starting Frontend on port 8080..."
cd frontend
python -m http.server 8080 > /tmp/frontend.log 2>&1 &
FRONTEND_PID=$!
echo "   Frontend PID: $FRONTEND_PID"
cd ..

echo ""
echo "✅ All services started successfully!"
echo ""
echo "📍 Access your interfaces:"
echo "   Custom UI:  https://\${YOUR_IDX_URL}:8080"
echo "   ADK Web:    https://\${YOUR_IDX_URL}:3002"
echo "   API Docs:   https://\${YOUR_IDX_URL}:8000/docs"
echo ""
echo "📝 Service PIDs:"
echo "   FastAPI: $API_PID"
echo "   ADK Web: $ADK_PID"
echo "   Frontend: $FRONTEND_PID"
echo ""
echo "📊 View logs:"
echo "   tail -f /tmp/api.log"
echo "   tail -f /tmp/adk-web.log"
echo "   tail -f /tmp/frontend.log"
echo ""
echo "🛑 Stop services:"
echo "   kill $API_PID $ADK_PID $FRONTEND_PID"
echo "   redis-cli shutdown"

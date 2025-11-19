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

# Use absolute path to uvicorn from venv
UVICORN_PATH=.venv/bin/uvicorn
if [ ! -f "$UVICORN_PATH" ]; then
    echo "❌ ERROR: uvicorn not found in .venv"
    exit 1
fi

$UVICORN_PATH api.main:app --host 0.0.0.0 --port 8000 --reload > /tmp/api.log 2>&1 &
API_PID=$!
echo "   FastAPI PID: $API_PID"
echo "   PYTHONPATH: $PYTHONPATH"
sleep 2

# Start ADK Web Interface
echo "🔍 Starting ADK Web on port 3002..."

# Use absolute path to adk from venv
ADK_PATH=.venv/bin/adk
if [ ! -f "$ADK_PATH" ]; then
    echo "❌ ERROR: adk not found in .venv"
    exit 1
fi

cd adk_agents
../$ADK_PATH web --host 0.0.0.0 --port 3002 > /tmp/adk-web.log 2>&1 &
ADK_PID=$!
echo "   ADK Web PID: $ADK_PID"
cd ..
sleep 2

# Start Streamlit Workshop UI
echo "🎨 Starting Streamlit Workshop UI on port 8501..."
streamlit run streamlit_apps/workshop_ui/app.py --server.port 8501 --server.address 0.0.0.0 > /tmp/streamlit.log 2>&1 &
STREAMLIT_PID=$!
echo "   Streamlit PID: $STREAMLIT_PID"

echo ""
echo "✅ All services started successfully!"
echo ""
echo "📍 Access your interfaces:"
echo "   🎯 Streamlit UI: Port 8501 (Primary - Start here!)"
echo "   🔍 ADK Web:      Port 3002 (Debugging)"
echo "   📚 API Docs:     Port 8000 (FastAPI - Optional)"
echo ""
echo "📝 Service PIDs:"
echo "   Streamlit: $STREAMLIT_PID"
echo "   ADK Web: $ADK_PID"
echo "   FastAPI: $API_PID (Optional)"
echo ""
echo "📊 View logs:"
echo "   tail -f /tmp/streamlit.log"
echo "   tail -f /tmp/adk-web.log"
echo "   tail -f /tmp/api.log"
echo ""
echo "🛑 Stop services:"
echo "   kill $STREAMLIT_PID $ADK_PID $API_PID"
echo "   redis-cli shutdown"

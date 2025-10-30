# Google ADK + FastAPI Workshop

Welcome! This is a full-stack starter kit for building agentic AI applications using Google's Agent Development Kit (ADK) and FastAPI.

This repository contains a complete, runnable environment managed by Docker Compose.

## 🚀 Student Quick Start

Your setup is two commands away.

### Prerequisites

1.  **Git:** [Install Git](https://git-scm.com/downloads)
2.  **Docker Desktop:** [Install Docker Desktop](https://www.docker.com/products/docker-desktop/) (This handles Mac, Windows, and Linux)

### Setup Instructions

1.  **Clone the Repository:**
    ```bash
    git clone <your-repo-url>
    cd adk-fastapi-workshop
    ```

2.  **Configure Environment:**
    ```bash
    # Create your environment file from the template
    cp .env.template .env
    ```
    Now, open the `.env` file and add your **`GOOGLE_API_KEY`**.

3.  **Run the Application:**
    ```bash
    docker compose up --build
    ```
    This command will build the Docker images and start all services (API, frontend, and database).

4.  **You're Ready!**
    * **Frontend Demo:** Open [http://localhost](http://localhost)
    * **API Docs:** Open [http://localhost/docs](http://localhost/docs)
    * **API Health:** Open [http://localhost/api/health](http://localhost/api/health)

---

## 📁 Project Structure
adk-fastapi-workshop/
├── agents/                    # ADK agent definitions
│   ├── examples/              # Example agents
│   └── manager.py             # Agent orchestration
├── api/                       # FastAPI application
│   ├── routes/                # API endpoints
│   ├── models/                # Pydantic models
│   └── main.py                # FastAPI app
├── config/                    # Configuration (settings.py)
├── frontend/                  # Simple HTML/JS frontend
├── mcp/                       # Stub MCP server
├── tests/                     # Pytest tests
├── tools/                     # Custom tools
│   ├── custom/                # Your tools
│   └── mcp/                   # MCP client
├── Dockerfile                 # Main API Dockerfile
├── Dockerfile.mcp             # MCP Server Dockerfile
├── docker-compose.yml         # Defines all services
├── nginx.conf                 # NGINX proxy config
├── requirements.txt           # Python dependencies
└── README.md                  # This file

## 🛠️ Key Services (in Docker Compose)

* **`frontend` (NGINX):** The public-facing service. Serves the `frontend/index.html` file and acts as a proxy, directing traffic to the correct backend service.
    * `http://localhost` -> Serves the frontend
    * `http://localhost/api/*` -> Forwards to the `api` service
    * `http://localhost/ws/*` -> Forwards to the `api` service (WebSocket)
* **`api` (FastAPI):** The Python backend. This is where `api/main.py` runs, along with your `AgentManager`. It's not exposed publicly, only through NGINX.
* **`redis` (Redis):** In-memory data store, perfect for caching or managing user sessions.
* **`mcp-server` (FastAPI):** A separate, optional stub server that demonstrates the Model Context Protocol (MCP) for tool discovery. (Profile: `mcp`)
* **`prometheus` / `grafana`:** Optional monitoring stack. (Profile: `monitoring`)

## 🎓 Workshop Development

Your goal is to modify the files in the `agents/`, `api/`, and `tools/` directories.

Because the project is running with **live-reload volumes**, you can **edit your Python files locally**, and the FastAPI server will **automatically restart inside Docker** to apply your changes.

### Optional: Running MCP / Monitoring

If you want to run the optional services, use the `--profile` flag:

```bash
# Run main app + MCP server
docker compose --profile mcp up --build

# Run main app + monitoring
docker compose --profile monitoring up --build

# Run everything
docker compose --profile mcp --profile monitoring up --build

```

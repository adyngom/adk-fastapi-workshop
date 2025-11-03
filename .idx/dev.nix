# Google IDX Configuration for ADK FastAPI Workshop
# Provides a fully configured development environment in the browser

{ pkgs, ... }: {

  # Channel for package versions
  channel = "stable-24.05";

  # Packages available in the environment
  packages = [
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.python311Packages.virtualenv
    pkgs.redis
    pkgs.nginx
    pkgs.curl
    pkgs.git
  ];

  # Environment variables
  env = {
    PYTHON_VERSION = "3.11";
    PYTHONUNBUFFERED = "1";
    # Note: GOOGLE_API_KEY should be set via IDX secrets
  };

  # IDX-specific settings
  idx = {
    # Extensions to install
    extensions = [
      "ms-python.python"
      "ms-python.vscode-pylance"
      "ms-python.debugpy"
    ];

    # Workspace configuration
    workspace = {
      # Auto-install Python dependencies on workspace load
      # Note: If this fails, students can run ./.idx/manual-setup.sh
      onCreate = {
        install-deps = ''
          set -e  # Exit on error
          echo "🔧 Setting up Python environment..."

          python -m venv .venv || {
            echo "❌ Failed to create virtual environment"
            echo "💡 Run: ./.idx/manual-setup.sh"
            exit 1
          }

          source .venv/bin/activate

          pip install --upgrade pip --quiet || {
            echo "⚠️ pip upgrade failed, continuing..."
          }

          pip install -r requirements.txt --quiet || {
            echo "❌ Failed to install requirements.txt"
            echo "💡 Run: ./.idx/manual-setup.sh"
            exit 1
          }

          pip install -r requirements-adk.txt --quiet || {
            echo "❌ Failed to install ADK requirements"
            echo "💡 Run: ./.idx/manual-setup.sh"
            exit 1
          }

          echo "✅ Dependencies installed successfully"
        '';

        # Create .env from template if not exists
        setup-env = ''
          if [ ! -f .env ]; then
            cp .env.template .env
            echo "📝 Created .env file from template"
            echo "⚠️  IMPORTANT: Add your GOOGLE_API_KEY to .env"
            echo "   Get key: https://aistudio.google.com/apikey"
          else
            echo "✅ .env file already exists"
          fi
        '';

        # Show recovery instructions if onCreate fails
        show-recovery = ''
          echo ""
          echo "═══════════════════════════════════════════════════════"
          echo "🚀 ADK Workshop Setup"
          echo "═══════════════════════════════════════════════════════"
          echo ""
          echo "If onCreate didn't complete, run:"
          echo "  ./.idx/manual-setup.sh"
          echo ""
          echo "Then start services:"
          echo "  ./.idx/start-services.sh"
          echo ""
          echo "Need help? See: .idx/TROUBLESHOOTING.md"
          echo "═══════════════════════════════════════════════════════"
          echo ""
        '';
      };

      # Commands to run when workspace starts
      onStart = {
        # Start Redis in background
        start-redis = ''
          redis-server --daemonize yes --port 6379
        '';

        # Start FastAPI backend
        start-api = ''
          source .venv/bin/activate
          cd api
          uvicorn main:app --host 0.0.0.0 --port 8000 --reload &
        '';

        # Start ADK Web interface (in adk_agents directory)
        start-adk-web = ''
          source .venv/bin/activate
          cd adk_agents
          adk web --host 0.0.0.0 --port 3002 &
        '';

        # Serve frontend with Python's simple HTTP server
        start-frontend = ''
          cd frontend
          python -m http.server 8080 &
        '';
      };
    };

    # Preview configuration
    previews = {
      enable = true;
      previews = {
        web = {
          command = ["echo" "Services starting..."];
          manager = "web";
          env = {
            PORT = "8080";
          };
        };
      };
    };
  };
}

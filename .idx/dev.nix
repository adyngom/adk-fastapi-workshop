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
      # Open welcome file and show setup instructions
      # Manual setup is the PRIMARY path (reliable, interactive API key)
      onCreate = {
        default.openFiles = ["STUDENT_SETUP_CHECKLIST.md"];

        show-welcome = ''
          echo ""
          echo "╔════════════════════════════════════════════════════════╗"
          echo "║                                                        ║"
          echo "║       🚀 Welcome to ADK + FastAPI Workshop! 🚀         ║"
          echo "║                                                        ║"
          echo "╚════════════════════════════════════════════════════════╝"
          echo ""
          echo "📋 Quick Setup (5 minutes total):"
          echo ""
          echo "   1️⃣  Run setup script:"
          echo "      ./.idx/manual-setup.sh"
          echo ""
          echo "   2️⃣  Run start script:"
          echo "      ./.idx/start-services.sh"
          echo ""
          echo "   3️⃣  Access Streamlit UI (port 8501)"
          echo ""
          echo "📖 See STUDENT_SETUP_CHECKLIST.md (now open) for details"
          echo ""
          echo "════════════════════════════════════════════════════════"
          echo ""
        '';
      };

      # Commands to run when workspace starts
      onStart = {
        # Show reminder if setup not complete
        check-setup = ''
          if [ ! -d ".venv" ]; then
            echo ""
            echo "⚠️  Setup not complete yet!"
            echo ""
            echo "Run these 2 commands:"
            echo "  1. ./.idx/manual-setup.sh"
            echo "  2. ./.idx/start-services.sh"
            echo ""
          fi
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

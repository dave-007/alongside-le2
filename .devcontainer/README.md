# DevContainer Configuration

DevContainer for Alongside Learning Environment - Azure AI and LLM development on Ubuntu 24.04 LTS.

## Features

### Base
- **Ubuntu 24.04 LTS** - `mcr.microsoft.com/devcontainers/base:ubuntu-24.04`

### Languages & Tools
- **Python 3.11** | **Node.js LTS** | **TypeScript**
- **Git** | **GitHub CLI** | **Azure CLI** | **Docker-in-Docker**
- **Zsh with Oh My Zsh** | Common utilities (curl, wget, vim, jq, tree, htop)

### Python Packages
`azure-ai-textanalytics` | `azure-cognitiveservices-speech` | `openai` | `langchain` | `transformers` | `pytest` | `pytest-asyncio` | `black` | `pylint`

### VS Code Extensions
Python, Pylance, Jupyter, Azure Functions, Azure CLI, Copilot, Docker, Prettier, ESLint

## Getting Started

1. Open repository in VS Code
2. Click "Reopen in Container" (or F1 → "Dev Containers: Reopen in Container")
3. Wait 5-10 minutes for first build
4. Authenticate:
   ```bash
   az login
   gh auth login
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   python scripts/check_authentication.py
   python scripts/post_auth_setup.py
   ```

## Directory Structure
```
.devcontainer/
├── devcontainer.json    # Main config
├── post-create.sh       # Setup script
└── README.md

scripts/
├── check_authentication.py
└── post_auth_setup.py

tests/
└── test_authentication.py
```

## Customization

### Add Python Packages
Edit `.devcontainer/post-create.sh`:
```bash
pip install your-package-name
```

### Add VS Code Extensions
Edit `.devcontainer/devcontainer.json`:
```json
"extensions": ["existing.extension", "your.new-extension"]
```

### Port Forwarding
Default: `8000`, `3000`, `5000`, `8080`
Add more in `devcontainer.json` under `forwardPorts`

### Mounted Volumes
- `~/.azure` → `/home/vscode/.azure` (cached)
- `~/.ssh` → `/home/vscode/.ssh-localhost` (read-only)

## Testing
```bash
pytest tests/ -v                       # All tests
pytest tests/test_authentication.py    # Specific test
```

## Troubleshooting

**Container fails to start:**
- Ensure Docker Desktop is running (4GB RAM min, 8GB recommended)
- Rebuild: F1 → "Dev Containers: Rebuild Container"

**Authentication issues:**
- Run `python scripts/check_authentication.py`
- Azure: `az account clear` then `az login`
- GitHub: `gh auth logout` then `gh auth login`

**Package conflicts:**
- Rebuild container or `pip install --upgrade package-name`

## Resources
- [DevContainers](https://containers.dev/) | [VS Code DevContainers](https://code.visualstudio.com/docs/devcontainers/containers)
- [DevContainers Features](https://containers.dev/features)
- [Azure CLI](https://docs.microsoft.com/cli/azure/) | [GitHub CLI](https://cli.github.com/manual/)

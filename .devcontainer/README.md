# DevContainer Configuration

This directory contains the DevContainer configuration for the Alongside Learning Environment, optimized for Azure AI and LLM development.

## Overview

This DevContainer is based on **Ubuntu 24.04 LTS** (the latest Ubuntu LTS release) and includes popular tools and features commonly used by the community.

## Features

### Base Image
- **Ubuntu 24.04 LTS** - Latest long-term support release
- Microsoft's official DevContainer base image: `mcr.microsoft.com/devcontainers/base:ubuntu-24.04`

### Included Tools & Features

#### Programming Languages
- **Python 3.11** - Latest stable Python with pip and development tools
- **Node.js LTS** - Latest LTS version with npm and node-gyp dependencies
- **TypeScript** - TypeScript compiler and ts-node

#### Version Control & Collaboration
- **Git** - Latest version
- **GitHub CLI (gh)** - For GitHub operations from the terminal

#### Cloud & Container Tools
- **Azure CLI** - For managing Azure resources
- **Docker-in-Docker** - For building and running containers within the devcontainer

#### Development Utilities
- **Zsh with Oh My Zsh** - Enhanced shell with themes and plugins
- **Common utilities** - curl, wget, vim, jq, tree, htop

### Python Packages

Pre-installed Python packages for Azure AI and LLM development:
- `azure-ai-textanalytics` - Azure Text Analytics
- `azure-cognitiveservices-speech` - Azure Speech Services
- `openai` - OpenAI API client (works with Azure OpenAI)
- `langchain` - Framework for LLM applications
- `transformers` - Hugging Face transformers library
- `pytest` & `pytest-asyncio` - Testing frameworks
- `black` & `pylint` - Code formatting and linting

### VS Code Extensions

Automatically installed extensions:
- Python development: Python, Pylance, Jupyter
- Azure tools: Azure Functions, Azure CLI
- GitHub tools: Copilot, Copilot Chat
- Docker support
- Code formatting: Prettier, ESLint

## Getting Started

### Prerequisites
- [Visual Studio Code](https://code.visualstudio.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Dev Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### Opening the DevContainer

1. Open this repository in VS Code
2. When prompted, click "Reopen in Container"
   - Or use Command Palette (F1) → "Dev Containers: Reopen in Container"
3. Wait for the container to build and start (first time takes 5-10 minutes)
4. The `post-create.sh` script will run automatically to set up the environment

### Post-Creation Setup

After the container is created, you'll need to authenticate with services:

#### 1. Azure CLI Authentication
```bash
az login
```
Follow the browser prompts to authenticate.

#### 2. GitHub CLI Authentication
```bash
gh auth login
```
Choose your preferred authentication method.

#### 3. Git Configuration (if not already set)
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

#### 4. Verify Authentication
```bash
python scripts/check_authentication.py
```

#### 5. Run Post-Authentication Setup
```bash
python scripts/post_auth_setup.py
```

## Directory Structure

```
.devcontainer/
├── devcontainer.json       # Main DevContainer configuration
├── post-create.sh          # Post-creation setup script
└── README.md              # This file

scripts/
├── check_authentication.py # Verify authentication status
└── post_auth_setup.py     # Post-authentication setup

tests/
└── test_authentication.py # Tests for authentication scripts

samples/
└── azure_ai_example.py    # Sample Azure AI usage examples
```

## Customization

### Adding More Python Packages

Edit `.devcontainer/post-create.sh` and add packages to the pip install command:
```bash
pip install your-package-name
```

### Adding VS Code Extensions

Edit `.devcontainer/devcontainer.json` under `customizations.vscode.extensions`:
```json
"extensions": [
    "existing.extension",
    "your.new-extension"
]
```

### Port Forwarding

The following ports are automatically forwarded:
- `8000` - Python Server
- `3000` - Node Server  
- `5000` - Flask Server
- `8080` - General purpose

Add more in `devcontainer.json` under `forwardPorts`.

## Mounted Volumes

The following local directories are mounted in the container:
- `~/.azure` → `/home/vscode/.azure` (Azure CLI credentials, cached)
- `~/.ssh` → `/home/vscode/.ssh-localhost` (SSH keys, read-only)

## Authentication Scripts

### check_authentication.py

Verifies that you're authenticated with:
- Azure CLI (`az`)
- GitHub CLI (`gh`)
- Git configuration

Run with:
```bash
python scripts/check_authentication.py
```

Returns exit code 0 if all checks pass, 1 otherwise.

### post_auth_setup.py

Runs after authentication to:
- List Azure subscriptions
- Verify GitHub access
- Create sample workspace directories
- Generate helpful documentation

Run with:
```bash
python scripts/post_auth_setup.py
```

## Testing

Run tests with:
```bash
pytest tests/ -v
```

Or run specific test file:
```bash
pytest tests/test_authentication.py -v
```

## Troubleshooting

### Container fails to start
- Ensure Docker Desktop is running
- Check Docker has enough resources (4GB RAM minimum, 8GB recommended)
- Try rebuilding: Command Palette → "Dev Containers: Rebuild Container"

### Authentication issues
- Run `python scripts/check_authentication.py` to diagnose
- For Azure: Try `az account clear` then `az login` again
- For GitHub: Try `gh auth logout` then `gh auth login` again

### Python package conflicts
- Rebuild the container to get a fresh environment
- Or manually update packages: `pip install --upgrade package-name`

## Popular Community Features

This DevContainer uses features from the official DevContainers Features repository, which are:
- **Maintained by Microsoft and the community**
- **Widely adopted** across thousands of projects
- **Regularly updated** for security and compatibility
- **Well-documented** with extensive examples

All features are from the official `ghcr.io/devcontainers/features/*` namespace.

## Resources

- [DevContainers Documentation](https://containers.dev/)
- [VS Code DevContainers](https://code.visualstudio.com/docs/devcontainers/containers)
- [DevContainers Features](https://containers.dev/features)
- [Azure CLI Documentation](https://docs.microsoft.com/cli/azure/)
- [GitHub CLI Documentation](https://cli.github.com/manual/)

## License

This configuration is part of the Alongside Learning Environment project.

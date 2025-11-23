# Alongside LE2 Setup Guide

Complete guide to setting up and using the Alongside Learning Environment 2 devcontainer.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Initial Setup](#initial-setup)
3. [First-Time Configuration](#first-time-configuration)
4. [Verification](#verification)
5. [Common Tasks](#common-tasks)
6. [Troubleshooting](#troubleshooting)

## Prerequisites

Before you begin, ensure you have:

### Required Software

- **Visual Studio Code**: [Download](https://code.visualstudio.com/)
- **Docker Desktop**: [Download](https://www.docker.com/products/docker-desktop)
  - Windows: Docker Desktop with WSL 2 backend
  - macOS: Docker Desktop
  - Linux: Docker Engine

### VS Code Extensions

Install the Dev Containers extension:
```
ext install ms-vscode-remote.remote-containers
```

### System Requirements

- **RAM**: Minimum 8GB, recommended 16GB+
- **Disk Space**: At least 10GB free
- **Internet**: Required for downloading dependencies

## Initial Setup

### 1. Clone the Repository

```bash
git clone https://github.com/dave-007/alongside-le2.git
cd alongside-le2
```

### 2. Open in VS Code

```bash
code .
```

### 3. Reopen in Container

When prompted by VS Code:
- Click **"Reopen in Container"**

Or manually:
- Press `F1` (Command Palette)
- Type: `Dev Containers: Reopen in Container`
- Press Enter

### 4. Wait for Build

The first build will take 5-15 minutes depending on your internet connection. The container will:
- Pull the Ubuntu base image
- Install Python 3.11
- Install .NET 8.0 SDK
- Install Azure CLI
- Install all Python libraries
- Install LLM and Fabric tools
- Configure the development environment

## First-Time Configuration

### Step 1: Run Verification Script

```bash
./verify_setup.sh
```

This will check that all tools are installed correctly.

### Step 2: Configure Environment Variables

Copy the example environment file:
```bash
cp .env.example .env
```

Edit `.env` and add your API keys:
```bash
nano .env  # or use VS Code to edit
```

### Step 3: Login to Azure

```bash
# Interactive login
az login

# Or use device code for remote sessions
az login --use-device-code
```

Verify your login:
```bash
az account show
az account list --output table
```

### Step 4: Configure LLM

Set up your LLM API keys:

```bash
# OpenAI
llm keys set openai
# Enter your key when prompted: sk-...

# Anthropic (Claude)
llm keys set anthropic
# Enter your key when prompted: sk-ant-...
```

Test LLM:
```bash
llm "Hello! Are you working?"
```

### Step 5: Setup Fabric

Initialize Fabric:
```bash
fabric --setup
```

Update Fabric patterns:
```bash
fabric --update
```

List available patterns:
```bash
fabric --listpatterns
```

## Verification

### Quick Test

Run all verification checks:
```bash
./verify_setup.sh
```

### Manual Verification

Test each tool individually:

```bash
# Python
python --version
pip --version

# .NET
dotnet --version

# Azure CLI
az --version
az account show

# LLM
llm --version
llm models

# Fabric
fabric --version
fabric --listpatterns

# Python libraries
python -c "import openai; print('OpenAI:', openai.__version__)"
python -c "import langchain; print('LangChain:', langchain.__version__)"
python -c "import azure.ai.ml; print('Azure ML: OK')"
```

## Common Tasks

### Running Examples

```bash
# Azure AI example
python examples/azure_ai_example.py

# LLM example
python examples/llm_example.py

# LangChain example
python examples/langchain_example.py
```

### Using LLM from Command Line

```bash
# Simple prompt
llm "Explain Docker in one sentence"

# With specific model
llm -m gpt-4 "Write a Python function to reverse a string"

# Pipe content
cat README.md | llm "Summarize this"

# Continue conversation
llm "What is machine learning?"
llm --continue "Can you give an example?"
```

### Using Fabric

```bash
# Summarize content
cat article.txt | fabric --pattern summarize

# Extract key ideas
echo "Your text here" | fabric --pattern extract_wisdom

# Analyze claims
fabric --pattern analyze_claims < document.txt
```

### Working with Azure AI

See `examples/azure_ai_example.py` for complete examples.

### Creating Python Projects

```bash
# Create virtual environment
python -m venv myproject_env
source myproject_env/bin/activate

# Install project dependencies
pip install -r requirements.txt

# Deactivate when done
deactivate
```

### Creating .NET Projects

```bash
# Console application
dotnet new console -n MyApp
cd MyApp
dotnet run

# Web API
dotnet new webapi -n MyApi
cd MyApi
dotnet run
```

### Using Jupyter Notebooks

```bash
# Start Jupyter Lab
jupyter lab --ip=0.0.0.0 --no-browser

# Or classic Jupyter
jupyter notebook --ip=0.0.0.0 --no-browser
```

Access at: http://localhost:8888

## Troubleshooting

### Container Build Fails

**Issue**: Container fails to build

**Solutions**:
```bash
# Ensure Docker is running
docker ps

# Rebuild container
# In VS Code: F1 → "Dev Containers: Rebuild Container"

# Clear Docker cache if needed
docker system prune -a
```

### LLM Command Not Found

**Issue**: `bash: llm: command not found`

**Solution**:
```bash
pip install --force-reinstall llm
hash -r  # Refresh bash command cache
llm --version
```

### Fabric Command Not Found

**Issue**: `bash: fabric: command not found`

**Solution**:
```bash
# Check if it's in PATH
echo $PATH | grep .local/bin

# Reinstall
pipx reinstall fabric

# Or add to PATH manually
export PATH="$HOME/.local/bin:$PATH"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```

### Azure Login Issues

**Issue**: Cannot login to Azure

**Solutions**:
```bash
# Try device code flow
az login --use-device-code

# Clear Azure cache
rm -rf ~/.azure

# Try again
az login
```

### Permission Denied Errors

**Issue**: Permission denied when running commands

**Solution**:
```bash
# Make script executable
chmod +x verify_setup.sh

# Or run with sudo for system-level commands
sudo apt-get update
```

### Python Package Import Errors

**Issue**: `ModuleNotFoundError` when importing packages

**Solutions**:
```bash
# Verify package is installed
pip list | grep package-name

# Reinstall package
pip install --force-reinstall package-name

# Check Python path
python -c "import sys; print('\n'.join(sys.path))"
```

### Docker Desktop Not Running

**Issue**: Cannot connect to Docker daemon

**Solution**:
- Open Docker Desktop application
- Wait for it to fully start
- Check Docker icon in system tray (should show green)
- Restart Docker Desktop if needed

### Out of Memory Errors

**Issue**: Container runs out of memory

**Solution**:
- Increase Docker memory allocation:
  - Docker Desktop → Settings → Resources
  - Increase Memory to 8GB or more
  - Click "Apply & Restart"

### Port Already in Use

**Issue**: Port conflicts when starting services

**Solution**:
```bash
# Find what's using the port
lsof -i :8888

# Kill the process
kill -9 <PID>

# Or use a different port
jupyter lab --port=8889
```

## Getting Help

### Resources

- **Documentation**:
  - [DevContainer README](.devcontainer/README.md)
  - [Quick Start Guide](.devcontainer/QUICK_START.md)
  - [Examples](examples/README.md)

- **External Documentation**:
  - [LLM Documentation](https://llm.datasette.io/)
  - [Fabric GitHub](https://github.com/danielmiessler/fabric)
  - [Azure AI Services](https://learn.microsoft.com/azure/ai-services/)
  - [LangChain Docs](https://python.langchain.com/)

### Support

- **GitHub Issues**: Report bugs or request features
- **Discussions**: Ask questions and share ideas
- **Contributing**: See [CONTRIBUTING.md](CONTRIBUTING.md)

## Next Steps

Once setup is complete:

1. ✅ Run `./verify_setup.sh`
2. ✅ Configure API keys in `.env`
3. ✅ Login to Azure with `az login`
4. ✅ Test LLM with `llm "Hello!"`
5. ✅ Setup Fabric with `fabric --setup`
6. ✅ Run examples in `examples/` directory
7. ✅ Read [Quick Start Guide](.devcontainer/QUICK_START.md)
8. ✅ Start building your AI applications!

## Tips for Success

- **Save your work**: Files in `/workspace` persist between container restarts
- **Use .env**: Never commit API keys to git
- **Virtual environments**: Use venv for project-specific dependencies
- **Regular updates**: Rebuild container periodically for updates
- **Check logs**: Use `docker logs` to diagnose container issues
- **Backup config**: Save your `.env` and custom configurations

Happy coding! 🚀

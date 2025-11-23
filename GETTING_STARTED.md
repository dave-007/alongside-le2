# Getting Started with Alongside Learning Environment

Welcome! This guide will help you set up and start using the Alongside Learning Environment for Azure AI and LLM development.

## 🎯 Prerequisites

Before you begin, make sure you have:

1. **Visual Studio Code** - [Download here](https://code.visualstudio.com/)
2. **Docker Desktop** - [Download here](https://www.docker.com/products/docker-desktop)
   - Minimum: 4GB RAM allocated to Docker
   - Recommended: 8GB RAM
3. **Dev Containers Extension** - Install from [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

## 📋 Step-by-Step Setup

### Step 1: Clone and Open the Repository

```bash
# Clone the repository
git clone https://github.com/dave-007/alongside-le2.git
cd alongside-le2

# Open in VS Code
code .
```

### Step 2: Launch DevContainer

When you open the repository in VS Code, you'll see a notification:

> "Folder contains a Dev Container configuration file. Reopen folder to develop in a container"

Click **"Reopen in Container"**

Alternatively, you can:
- Press `F1` or `Ctrl+Shift+P` (Cmd+Shift+P on Mac)
- Type "Dev Containers: Reopen in Container"
- Press Enter

**First Launch Note:** The initial build takes 5-10 minutes as it downloads the Ubuntu 24.04 image and installs all tools.

### Step 3: Wait for Setup to Complete

You'll see progress notifications as the container:
1. Builds the base image
2. Installs features (Python, Node.js, Azure CLI, etc.)
3. Runs the post-create script
4. Sets up the development environment

### Step 4: Authenticate with Services

Once the container is ready, open a new terminal in VS Code and authenticate:

#### Azure CLI
```bash
az login
```
- A browser window will open
- Sign in with your Azure account
- Return to VS Code after successful login

#### GitHub CLI
```bash
gh auth login
```
- Follow the prompts
- Choose your preferred authentication method (browser or token)
- Complete authentication

#### Git Configuration (if needed)
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 5: Verify Authentication

Run the authentication check script:

```bash
python scripts/check_authentication.py
```

You should see:
```
🔐 Checking Authentication Status...

✅ Azure CLI: Authenticated as: your@email.com
✅ GitHub CLI: Authenticated with GitHub
✅ Git Configuration: Configured as: Your Name <your@email.com>

============================================================
✅ All authentication checks passed!
You are ready to use the development environment.
```

### Step 6: Run Post-Authentication Setup

```bash
python scripts/post_auth_setup.py
```

This will:
- List your Azure subscriptions
- Verify GitHub access
- Create sample workspace directories
- Generate helpful documentation

### Step 7: Explore Examples

Try running the sample code:

```bash
python samples/azure_ai_example.py
```

This demonstrates how to use various Azure AI services.

## 🧪 Running Tests

Verify everything is working by running the test suite:

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_authentication.py -v

# Run with coverage
pytest tests/ --cov=scripts --cov-report=html
```

## 📁 Understanding the Project Structure

```
alongside-le2/
│
├── .devcontainer/              # DevContainer configuration
│   ├── devcontainer.json       # Container settings and features
│   ├── post-create.sh          # Post-creation setup script
│   └── README.md              # DevContainer documentation
│
├── scripts/                    # Utility scripts
│   ├── check_authentication.py # Verify authentication status
│   └── post_auth_setup.py     # Post-authentication setup
│
├── tests/                      # Test suite
│   └── test_authentication.py # Authentication tests
│
├── samples/                    # Example code
│   └── azure_ai_example.py    # Azure AI examples
│
├── workspace/                  # Your workspace (created on setup)
│   ├── notebooks/             # Jupyter notebooks
│   ├── data/                  # Data files
│   ├── models/                # Model artifacts
│   └── scripts/               # Custom scripts
│
├── README.md                   # Main documentation
├── GETTING_STARTED.md         # This file
├── requirements.txt           # Python dependencies
└── pytest.ini                 # Pytest configuration
```

## 🚀 What's Next?

Now that your environment is set up, you can:

### 1. Explore Azure AI Services

```bash
# Check your Azure subscriptions
az account list --output table

# List available Azure AI services
az cognitiveservices account list --output table
```

### 2. Create a Jupyter Notebook

```bash
# Install Jupyter (if not already installed)
pip install jupyter

# Start Jupyter
jupyter notebook workspace/notebooks/
```

### 3. Experiment with LLMs

The environment includes:
- **OpenAI SDK** - For Azure OpenAI or OpenAI API
- **LangChain** - Framework for building LLM applications
- **Transformers** - Hugging Face models

### 4. Build Your First AI Application

Create a new Python file in `workspace/scripts/`:

```python
# workspace/scripts/my_first_ai_app.py
import openai
import os

# Configure Azure OpenAI
openai.api_type = "azure"
openai.api_base = os.getenv('AZURE_OPENAI_ENDPOINT')
openai.api_key = os.getenv('AZURE_OPENAI_KEY')
openai.api_version = "2023-05-15"

# Your code here...
```

## 🔧 Common Tasks

### Add Python Packages

```bash
# Install a package
pip install package-name

# Add to requirements.txt
echo "package-name>=1.0.0" >> requirements.txt

# Install all requirements
pip install -r requirements.txt
```

### Add VS Code Extensions

Edit `.devcontainer/devcontainer.json` and add to the `extensions` array:

```json
"extensions": [
    "existing.extension",
    "your-publisher.your-extension"
]
```

Then rebuild the container: `Dev Containers: Rebuild Container`

### Forward Additional Ports

Edit `.devcontainer/devcontainer.json` and add to `forwardPorts`:

```json
"forwardPorts": [8000, 8080, 3000, 5000, 9000]
```

## ❓ Troubleshooting

### Container Won't Start

1. **Check Docker is running:**
   ```bash
   docker ps
   ```

2. **Check Docker resources:**
   - Open Docker Desktop
   - Go to Settings → Resources
   - Ensure at least 4GB RAM is allocated

3. **Rebuild the container:**
   - `F1` → "Dev Containers: Rebuild Container"

### Authentication Issues

**Azure CLI:**
```bash
# Clear existing login
az account clear

# Login again
az login
```

**GitHub CLI:**
```bash
# Logout
gh auth logout

# Login again
gh auth login
```

### Python Package Conflicts

```bash
# Create a fresh virtual environment
python -m venv fresh-env
source fresh-env/bin/activate  # or `fresh-env\Scripts\activate` on Windows

# Install packages
pip install -r requirements.txt
```

### Port Already in Use

If a port is already in use on your host machine:

1. Edit `.devcontainer/devcontainer.json`
2. Change the port number in `forwardPorts`
3. Rebuild the container

## 📚 Additional Resources

### Documentation
- [DevContainer Documentation](.devcontainer/README.md)
- [Azure AI Services](https://docs.microsoft.com/azure/ai-services/)
- [Azure CLI Reference](https://docs.microsoft.com/cli/azure/)
- [GitHub CLI Manual](https://cli.github.com/manual/)

### Tutorials
- [Azure OpenAI Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart)
- [LangChain Tutorials](https://python.langchain.com/docs/tutorials/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)

### Community
- [DevContainers on GitHub](https://github.com/devcontainers)
- [VS Code DevContainers](https://code.visualstudio.com/docs/devcontainers/containers)

## 🎉 You're Ready!

Your Alongside Learning Environment is now set up and ready to use. Start exploring Azure AI, building LLM applications, and creating amazing projects!

Need help? Check the documentation or open an issue on GitHub.

Happy coding! 🚀

# Alongside Learning Environment (LE2)

A fully-equipped development environment for working with Azure AI, LLMs, and more. Built on Ubuntu 24.04 LTS with popular community-maintained tools.

## 🚀 Quick Start

### Using DevContainers (Recommended)

1. **Prerequisites:**
   - [VS Code](https://code.visualstudio.com/)
   - [Docker Desktop](https://www.docker.com/products/docker-desktop)
   - [Dev Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

2. **Open in DevContainer:**
   - Clone this repository
   - Open in VS Code
   - Click "Reopen in Container" when prompted
   - Wait for initial setup (5-10 minutes first time)

3. **Authenticate:**
   ```bash
   # Authenticate with Azure
   az login
   
   # Authenticate with GitHub
   gh auth login
   
   # Verify authentication
   python scripts/check_authentication.py
   
   # Run post-authentication setup
   python scripts/post_auth_setup.py
   ```

## 📦 What's Included

### Development Environment
- **Ubuntu 24.04 LTS** - Latest long-term support release
- **Python 3.11** - With pip and development tools
- **Node.js LTS** - Latest LTS with npm
- **Docker-in-Docker** - Build containers within the devcontainer

### Cloud & AI Tools
- **Azure CLI** - Manage Azure resources
- **GitHub CLI** - GitHub operations from terminal
- **Azure AI SDKs** - Text Analytics, Speech Services
- **OpenAI** - Azure OpenAI integration
- **LangChain** - Framework for LLM applications
- **Transformers** - Hugging Face models

### Development Tools
- **Git** with Oh My Zsh
- **VS Code Extensions** - Python, Jupyter, Azure, GitHub Copilot
- **Testing** - pytest with async support
- **Formatting** - black, pylint, prettier, eslint

## 📁 Project Structure

```
.
├── .devcontainer/          # DevContainer configuration
│   ├── devcontainer.json   # Main configuration
│   ├── post-create.sh      # Setup script
│   └── README.md           # DevContainer documentation
├── scripts/                # Utility scripts
│   ├── check_authentication.py  # Verify auth status
│   └── post_auth_setup.py       # Post-auth setup
├── tests/                  # Test suite
│   └── test_authentication.py   # Authentication tests
└── samples/                # Example code
    └── azure_ai_example.py      # Azure AI examples
```

## 🔐 Authentication Scripts

### Check Authentication Status
Verify you're authenticated with all required services:
```bash
python scripts/check_authentication.py
```

Checks:
- ✅ Azure CLI authentication
- ✅ GitHub CLI authentication
- ✅ Git configuration

### Post-Authentication Setup
Run after authenticating to set up your environment:
```bash
python scripts/post_auth_setup.py
```

This will:
- List your Azure subscriptions
- Verify GitHub access
- Create sample workspace directories
- Generate helpful documentation

## 🧪 Testing

Run all tests:
```bash
pytest tests/ -v
```

Run specific tests:
```bash
pytest tests/test_authentication.py -v
```

## 📚 Examples

See the `samples/` directory for example code:

- `azure_ai_example.py` - Examples of using Azure AI services

## 🛠️ Customization

See [.devcontainer/README.md](.devcontainer/README.md) for details on:
- Adding Python packages
- Installing VS Code extensions
- Configuring port forwarding
- Mounting additional volumes

## 📖 Documentation

- [DevContainer Configuration](.devcontainer/README.md) - Detailed DevContainer setup
- [Azure AI Documentation](https://docs.microsoft.com/azure/ai-services/)
- [OpenAI API](https://platform.openai.com/docs)
- [LangChain](https://python.langchain.com/)

## 🤝 Contributing

This environment uses:
- **Official DevContainers Features** from Microsoft and the community
- **Popular, well-maintained tools** with active communities
- **Latest Ubuntu LTS** for stability and security

## 📝 License

This project is part of the Alongside Learning Environment.

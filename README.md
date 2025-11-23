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
# Alongside LE2

Alongside Learning Environment 2 - A fully equipped development container for working with Azure AI, LLMs, Python, .NET, and powerful AI tools.

## Features

This repository provides a comprehensive devcontainer that includes:

- **Latest Ubuntu LTS** base system
- **Python 3.11+** with extensive AI/ML libraries
- **.NET 8.0 SDK** for C# development
- **Azure CLI** and Azure AI SDKs
- **Simon Willison's LLM** tool ([llm.datasette.io](https://llm.datasette.io/))
- **Daniel Miessler's Fabric** ([github.com/danielmiessler/fabric](https://github.com/danielmiessler/fabric))
- **LangChain** framework for LLM applications
- **OpenAI, Anthropic, and Azure AI integrations**
- **Data science libraries** (pandas, numpy, scikit-learn, matplotlib)
- **Development tools** (pytest, black, pylint, mypy)

## Getting Started

### Prerequisites

- [Visual Studio Code](https://code.visualstudio.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) for VS Code

### Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/dave-007/alongside-le2.git
   cd alongside-le2
   ```

2. **Open in VS Code**:
   ```bash
   code .
   ```

3. **Reopen in Container**:
   - Click "Reopen in Container" when prompted
   - Or use Command Palette (F1) → "Dev Containers: Reopen in Container"

4. **Wait for the container to build** (first time may take 5-10 minutes)

5. **Verify installation**:
   ```bash
   python --version
   dotnet --version
   az --version
   llm --version
   fabric --version
   ```

## What's Inside

### Azure AI Tools
- Azure ML SDK
- Azure Cognitive Services (Text Analytics, Speech, Form Recognizer)
- Azure AI Inference and Projects
- Prompt Flow for workflow management

### LLM Tools
- **LLM CLI**: Command-line tool for interacting with various LLMs
- **Fabric**: AI-powered pattern library for common tasks
- **LangChain**: Framework for building LLM applications
- **OpenAI & Anthropic APIs**: Direct API access

### Development Environment
- Pre-configured VS Code extensions (Python, C#, Azure, GitHub Copilot)
- Code formatting and linting tools
- Testing frameworks
- Jupyter notebook support

## Documentation

For detailed information about the devcontainer setup, usage examples, and troubleshooting, see the [DevContainer README](.devcontainer/README.md).

## Contributing

This is a learning environment repository. Feel free to customize the devcontainer for your specific needs.

## License

MIT License - See LICENSE file for details

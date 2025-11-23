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

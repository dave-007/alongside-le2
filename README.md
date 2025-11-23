# Alongside Learning Environment (LE2)

A DevContainer environment for Azure AI, LLMs, Python, .NET, and AI development tools.

## Quick Start

### Prerequisites
- [VS Code](https://code.visualstudio.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Dev Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### Setup
1. Clone and open in VS Code: `git clone https://github.com/dave-007/alongside-le2.git && code alongside-le2`
2. Click "Reopen in Container" when prompted (5-10 min first time)
3. Authenticate:
   ```bash
   az login
   gh auth login
   python scripts/check_authentication.py
   python scripts/post_auth_setup.py
   ```

## What's Included

### Environment
- **Ubuntu 24.04 LTS** | **Python 3.11** | **Node.js LTS** | **.NET 8.0 SDK** | **Docker-in-Docker**

### AI/ML Tools
- **Azure**: CLI, AI SDKs (Text Analytics, Speech, Form Recognizer), ML SDK, Prompt Flow
- **LLMs**: LangChain, OpenAI, Anthropic, Transformers
- **CLI Tools**: [LLM](https://llm.datasette.io/), [Fabric](https://github.com/danielmiessler/fabric)
- **Data Science**: pandas, numpy, scikit-learn, matplotlib

### Development
- **Git** with Oh My Zsh | **VS Code Extensions**: Python, C#, Azure, GitHub Copilot
- **Testing**: pytest | **Formatting**: black, pylint, prettier, eslint | **Jupyter** support

## Project Structure
```
├── .devcontainer/       # DevContainer configuration
├── scripts/             # check_authentication.py, post_auth_setup.py
├── tests/               # Test suite
└── samples/             # Example code
```

## Testing
```bash
pytest tests/ -v                      # All tests
pytest tests/test_authentication.py  # Specific tests
```

## Documentation
- [DevContainer Setup](.devcontainer/README.md)
- [Examples](examples/README.md)
- [Azure AI Docs](https://docs.microsoft.com/azure/ai-services/)
- [LangChain Docs](https://python.langchain.com/)

## License
MIT License - See LICENSE file

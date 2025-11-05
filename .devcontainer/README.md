# Alongside LE2 DevContainer

This devcontainer provides a complete development environment for working with AI, Azure, Python, and .NET.

## What's Included

### Base System
- **Ubuntu Latest**: Latest Ubuntu LTS as the base operating system
- **Non-root user**: `vscode` user for secure development

### Programming Languages & Runtimes
- **Python 3.11+**: Latest Python with pip and virtual environment support
- **.NET 8.0 SDK**: Latest .NET SDK for C# development

### Azure Tools
- **Azure CLI**: Command-line interface for Azure services
- **Azure AI SDKs**:
  - `azure-ai-ml`: Azure Machine Learning SDK
  - `azure-ai-textanalytics`: Text Analytics API
  - `azure-ai-formrecognizer`: Form Recognizer API
  - `azure-cognitiveservices-speech`: Speech Services SDK
  - `azure-ai-inference`: Azure AI Inference SDK
  - `azure-ai-projects`: Azure AI Projects SDK
  - `azure-identity`: Azure authentication
  - `azure-storage-blob`: Blob storage
  - `azure-keyvault-secrets`: Key Vault integration
- **Prompt Flow**: Azure AI workflow tool

### AI/LLM Tools

#### Simon Willison's LLM
- **LLM CLI**: https://llm.datasette.io/
- Pre-installed plugins:
  - `llm-gpt4all`: Local LLM support
  - `llm-claude-3`: Claude 3 API access
  - `llm-gemini`: Google Gemini API access

#### Daniel Miessler's Fabric
- **Fabric**: https://github.com/danielmiessler/fabric
- Installed via pipx for clean isolation
- Configuration directory: `~/.config/fabric`

### Python Libraries

#### AI/ML Libraries
- `openai`: OpenAI API client
- `anthropic`: Anthropic (Claude) API client
- `langchain`: LLM application framework
- `langchain-openai`: LangChain OpenAI integration
- `langchain-community`: Community integrations

#### Data Science
- `numpy`: Numerical computing
- `pandas`: Data manipulation and analysis
- `scikit-learn`: Machine learning algorithms
- `matplotlib`: Data visualization
- `seaborn`: Statistical data visualization
- `jupyter`: Jupyter notebooks
- `ipykernel`: IPython kernel for Jupyter

#### Development Tools
- `black`: Code formatter
- `pylint`: Code linter
- `flake8`: Style guide enforcement
- `pytest`: Testing framework
- `mypy`: Static type checker

#### Utilities
- `requests`: HTTP library
- `python-dotenv`: Environment variable management
- `pyyaml`: YAML parser
- `click`: Command-line interface creation

### VS Code Extensions

Pre-configured extensions:
- Python support (with Pylance)
- C# / .NET support
- Azure Functions
- Azure Resource Groups
- GitHub Copilot
- GitHub Copilot Chat

## Getting Started

### Prerequisites
- Visual Studio Code with the "Dev Containers" extension
- Docker Desktop installed and running

### Opening the DevContainer

1. Clone this repository
2. Open the folder in VS Code
3. When prompted, click "Reopen in Container"
   - Or use Command Palette (F1) → "Dev Containers: Reopen in Container"

### First-Time Setup

After the container builds and starts:

1. **Azure Login**:
   ```bash
   az login
   ```

2. **Configure LLM** (Simon Willison's tool):
   ```bash
   # Set OpenAI API key (example)
   llm keys set openai
   
   # Test LLM
   llm "What is the capital of France?"
   ```

3. **Configure Fabric** (Daniel Miessler's tool):
   ```bash
   # Setup Fabric
   fabric --setup
   
   # Update patterns
   fabric --update
   ```

4. **Test installations**:
   ```bash
   python --version
   dotnet --version
   az --version
   llm --version
   fabric --version
   ```

## Usage Examples

### Using LLM
```bash
# Simple prompt
llm "Explain quantum computing"

# Use a specific model
llm -m gpt-4 "Write a haiku about AI"

# Pipe content
cat myfile.txt | llm "Summarize this"
```

### Using Fabric
```bash
# Extract wisdom from content
echo "Your text here" | fabric --pattern extract_wisdom

# Summarize content
cat article.txt | fabric --pattern summarize

# Create AI-powered analysis
fabric --pattern analyze_claims < document.txt
```

### Using Azure AI
```python
from azure.ai.textanalytics import TextAnalyticsClient
from azure.identity import DefaultAzureCredential

# Authenticate and use Azure services
credential = DefaultAzureCredential()
client = TextAnalyticsClient(endpoint="<your-endpoint>", credential=credential)
```

### Using LangChain with Azure
```python
from langchain_openai import AzureChatOpenAI
from azure.identity import DefaultAzureCredential

# Initialize Azure OpenAI
llm = AzureChatOpenAI(
    azure_deployment="<deployment-name>",
    api_version="2024-02-01"
)
```

## Customization

### Adding Python Packages
```bash
pip install <package-name>
```

### Adding .NET Packages
```bash
dotnet add package <package-name>
```

### Adding LLM Plugins
```bash
llm install <plugin-name>
```

## Troubleshooting

### Container won't build
- Ensure Docker Desktop is running
- Check your internet connection
- Try rebuilding: Command Palette → "Dev Containers: Rebuild Container"

### Permission issues
- The container uses a non-root `vscode` user by default
- Use `sudo` for system-level commands if needed

### Azure CLI login issues
- Run `az login --use-device-code` for alternative authentication
- Check your Azure subscription: `az account show`

## Resources

- [Simon Willison's LLM Documentation](https://llm.datasette.io/)
- [Daniel Miessler's Fabric GitHub](https://github.com/danielmiessler/fabric)
- [Azure AI Documentation](https://learn.microsoft.com/en-us/azure/ai-services/)
- [LangChain Documentation](https://python.langchain.com/)
- [VS Code Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers)

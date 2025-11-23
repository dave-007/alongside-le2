# Examples

Example scripts demonstrating devcontainer tools.

## Available Examples

### Azure AI (`azure_ai_example.py`)
Azure Cognitive Services text analytics demo.
```bash
export AZURE_TEXT_ANALYTICS_ENDPOINT="https://your-resource.cognitiveservices.azure.com/"
az login
python examples/azure_ai_example.py
```

### LLM (`llm_example.py`)
Simon Willison's LLM CLI tool usage.
```bash
llm keys set openai
python examples/llm_example.py
# Or: llm "What is Python?"
```

### LangChain (`langchain_example.py`)
LangChain framework for LLM applications.
```bash
# Create .env with API keys
python examples/langchain_example.py
```

## Quick Setup

### Environment Variables (.env)
```bash
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_TEXT_ANALYTICS_ENDPOINT=https://your-resource.cognitiveservices.azure.com/
```

### Authentication
```bash
az login                    # Azure
gh auth login              # GitHub
```

### Test Tools
```bash
llm "Hello!"                     # LLM
echo "Test" | fabric --pattern summarize  # Fabric
az account show                   # Azure CLI
```

## Resources
- [LLM](https://llm.datasette.io/) | [Fabric](https://github.com/danielmiessler/fabric)
- [LangChain](https://python.langchain.com/) | [Azure AI](https://learn.microsoft.com/azure/ai-services/)

## Tips
- Use virtual environments: `python -m venv venv && source venv/bin/activate`
- Store secrets in environment variables or Azure Key Vault
- Never commit secrets to git
- Monitor API costs and use cheaper models for testing

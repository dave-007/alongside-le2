# Examples

This directory contains example scripts demonstrating how to use the tools included in the devcontainer.

## Available Examples

### 1. Azure AI Example (`azure_ai_example.py`)

Demonstrates how to use Azure Cognitive Services, specifically Text Analytics for sentiment analysis.

**Setup:**
```bash
# Set your Azure Text Analytics endpoint
export AZURE_TEXT_ANALYTICS_ENDPOINT="https://your-resource.cognitiveservices.azure.com/"

# Login to Azure
az login
```

**Run:**
```bash
python examples/azure_ai_example.py
```

### 2. LLM Example (`llm_example.py`)

Shows how to use Simon Willison's LLM CLI tool programmatically and from the command line.

**Setup:**
```bash
# Install LLM (already included in devcontainer)
pip install llm

# Set API keys
llm keys set openai
llm keys set anthropic
```

**Run:**
```bash
python examples/llm_example.py

# Or use LLM directly from command line
llm "What is Python?"
echo "Hello world" | llm "Translate to Spanish"
```

### 3. LangChain Example (`langchain_example.py`)

Demonstrates LangChain framework usage for building LLM applications.

**Setup:**
```bash
# Create a .env file with your API keys
cat > .env << EOF
OPENAI_API_KEY=your_openai_key
AZURE_OPENAI_API_KEY=your_azure_key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4
EOF
```

**Run:**
```bash
python examples/langchain_example.py
```

## Common Setup Steps

### 1. Environment Variables

Create a `.env` file in the workspace root:

```bash
# OpenAI
OPENAI_API_KEY=sk-...

# Anthropic (Claude)
ANTHROPIC_API_KEY=sk-ant-...

# Azure OpenAI
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4
AZURE_OPENAI_API_VERSION=2024-02-01

# Azure Cognitive Services
AZURE_TEXT_ANALYTICS_ENDPOINT=https://your-resource.cognitiveservices.azure.com/
AZURE_TEXT_ANALYTICS_KEY=...
```

### 2. Azure Authentication

```bash
# Interactive login
az login

# Device code login (for remote/headless)
az login --use-device-code

# Service principal login
az login --service-principal -u <app-id> -p <password> --tenant <tenant-id>
```

### 3. Testing Tools

```bash
# Test LLM
llm "Hello!"

# Test Fabric
echo "Test" | fabric --pattern summarize

# Test Azure CLI
az account show

# Test Python
python --version

# Test .NET
dotnet --version
```

## Running Examples Without API Keys

All examples are designed to run without API keys and will show you:
- What commands to use
- How to structure your code
- Expected outputs

To actually call the APIs, you'll need to:
1. Set up the appropriate API keys
2. Remove or modify the example code that skips API calls

## Additional Resources

- **LLM Documentation**: https://llm.datasette.io/
- **Fabric GitHub**: https://github.com/danielmiessler/fabric
- **LangChain Docs**: https://python.langchain.com/
- **Azure AI Services**: https://learn.microsoft.com/azure/ai-services/
- **Azure SDK for Python**: https://learn.microsoft.com/python/api/overview/azure/

## Creating Your Own Examples

Feel free to add your own examples to this directory. Suggested topics:

- Azure Machine Learning integration
- Prompt Flow workflows
- Custom LLM chains
- RAG (Retrieval-Augmented Generation) implementations
- Multi-agent systems
- Fine-tuning examples
- Evaluation and testing patterns

## Tips

1. **Use virtual environments** for project-specific dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. **Store secrets securely**:
   - Use environment variables
   - Use Azure Key Vault
   - Never commit secrets to git

3. **Test incrementally**:
   - Start with simple examples
   - Add complexity gradually
   - Use print statements for debugging

4. **Monitor costs**:
   - Track API usage
   - Use cheaper models for testing
   - Implement rate limiting

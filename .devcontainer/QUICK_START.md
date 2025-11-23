# Quick Start Guide

## Initial Setup (First Time)

After opening the devcontainer for the first time:

### 1. Login to Azure
```bash
az login
```

### 2. Configure LLM (Simon Willison's tool)

Set up your API keys:
```bash
# For OpenAI
llm keys set openai
# Enter your API key when prompted

# For Anthropic Claude
llm keys set anthropic
# Enter your API key when prompted
```

Test LLM:
```bash
# Simple test
llm "Hello! Can you confirm you're working?"

# Test with a specific model
llm -m gpt-4 "Write a haiku about coding"

# Test with local models (no API key needed)
llm -m ggml-gpt4all-j "Tell me about AI"
```

### 3. Configure Fabric (Daniel Miessler's tool)

```bash
# Initial setup
fabric --setup

# Update patterns to latest
fabric --update

# List available patterns
fabric --listpatterns
```

## Common Commands

### LLM Examples

```bash
# Ask a question
llm "What are the best practices for Python async programming?"

# Pipe content to LLM
cat README.md | llm "Summarize this document"

# Save and reuse prompts
llm "Explain quantum computing" --save quantum_explanation.txt

# Use system prompts
llm -s "You are a Python expert" "How do I use decorators?"

# Continue a conversation
llm "What is machine learning?"
llm --continue "Can you give me an example in Python?"
```

### Fabric Examples

```bash
# Extract wisdom from an article
curl https://example.com/article | fabric --pattern extract_wisdom

# Summarize content
cat document.txt | fabric --pattern summarize

# Create a summary
echo "Long text here..." | fabric --pattern create_summary

# Extract key ideas
fabric --pattern extract_ideas < input.txt

# Analyze claims
fabric --pattern analyze_claims < article.md

# Create essay outline
echo "Topic: AI Ethics" | fabric --pattern create_essay_outline
```

### Azure AI Examples

#### Text Analytics
```python
from azure.ai.textanalytics import TextAnalyticsClient
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
endpoint = "https://<your-resource>.cognitiveservices.azure.com/"

client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

documents = ["I love this product!", "This is terrible."]
response = client.analyze_sentiment(documents=documents)

for doc in response:
    print(f"Sentiment: {doc.sentiment}")
```

#### Azure OpenAI
```python
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key="YOUR_API_KEY",
    api_version="2024-02-01",
    azure_endpoint="https://<your-resource>.openai.azure.com"
)

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)

print(response.choices[0].message.content)
```

### LangChain Examples

```python
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

# Create a simple chain
llm = ChatOpenAI(model="gpt-3.5-turbo")
prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}")
chain = prompt | llm | StrOutputParser()

# Use the chain
result = chain.invoke({"topic": "programming"})
print(result)
```

## Tips & Tricks

### Environment Variables
Create a `.env` file in your workspace:
```bash
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
AZURE_OPENAI_API_KEY=your_key_here
AZURE_OPENAI_ENDPOINT=your_endpoint_here
```

Load in Python:
```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
```

### Jupyter Notebooks
```bash
# Start Jupyter
jupyter notebook --ip=0.0.0.0 --no-browser

# Or use JupyterLab
jupyter lab --ip=0.0.0.0 --no-browser
```

### Python Virtual Environments
```bash
# Create a venv
python -m venv myenv

# Activate
source myenv/bin/activate

# Deactivate
deactivate
```

### .NET Projects
```bash
# Create a new console app
dotnet new console -n MyApp

# Create a new web API
dotnet new webapi -n MyApi

# Run the project
dotnet run
```

## Troubleshooting

### LLM Command Not Found
```bash
# Reinstall LLM
pip install --force-reinstall llm

# Check installation
which llm
llm --version
```

### Fabric Command Not Found
```bash
# Check PATH
echo $PATH | grep .local/bin

# Reinstall Fabric
pipx reinstall fabric

# Check installation
which fabric
fabric --version
```

### Azure Login Issues
```bash
# Use device code flow
az login --use-device-code

# Check current account
az account show

# List subscriptions
az account list --output table

# Set subscription
az account set --subscription "Your Subscription Name"
```

### Python Package Issues
```bash
# Upgrade pip
pip install --upgrade pip

# Clear pip cache
pip cache purge

# Reinstall package
pip install --force-reinstall <package-name>
```

## Resources

- [LLM Documentation](https://llm.datasette.io/en/stable/)
- [LLM Plugins](https://llm.datasette.io/en/stable/plugins/directory.html)
- [Fabric Documentation](https://github.com/danielmiessler/fabric)
- [Fabric Patterns](https://github.com/danielmiessler/fabric/tree/main/patterns)
- [Azure AI Services](https://learn.microsoft.com/en-us/azure/ai-services/)
- [LangChain Docs](https://python.langchain.com/docs/get_started/introduction)
- [OpenAI Python SDK](https://github.com/openai/openai-python)

#!/usr/bin/env python3
"""
Sample Azure AI Example
This demonstrates using Azure AI services after authentication.
"""

import os
from typing import Optional


def check_azure_credentials() -> bool:
    """
    Check if Azure credentials are available.
    
    Returns:
        True if credentials are configured, False otherwise
    """
    # Check for common Azure credential environment variables
    creds = [
        'AZURE_SUBSCRIPTION_ID',
        'AZURE_TENANT_ID',
        'AZURE_CLIENT_ID',
    ]
    
    has_any_cred = any(os.getenv(var) for var in creds)
    
    if has_any_cred:
        print("✅ Azure credentials found in environment")
        return True
    
    # Check if Azure CLI is authenticated
    import subprocess
    try:
        result = subprocess.run(
            ['az', 'account', 'show'],
            capture_output=True,
            timeout=5
        )
        if result.returncode == 0:
            print("✅ Authenticated with Azure CLI")
            return True
    except:
        pass
    
    print("⚠️  No Azure credentials found")
    print("Please authenticate with: az login")
    return False


def example_text_analytics():
    """
    Example of using Azure Text Analytics (requires authentication).
    """
    print("\n📝 Azure Text Analytics Example")
    print("="*60)
    
    if not check_azure_credentials():
        print("Skipping - authentication required")
        return
    
    print("""
To use Azure Text Analytics, you would:

1. Install the SDK: pip install azure-ai-textanalytics
2. Set up your credentials:
   - Endpoint: AZURE_TEXT_ANALYTICS_ENDPOINT
   - Key: AZURE_TEXT_ANALYTICS_KEY
3. Create a client and analyze text

Example code:
    from azure.ai.textanalytics import TextAnalyticsClient
    from azure.core.credentials import AzureKeyCredential
    
    endpoint = os.getenv('AZURE_TEXT_ANALYTICS_ENDPOINT')
    key = os.getenv('AZURE_TEXT_ANALYTICS_KEY')
    
    client = TextAnalyticsClient(endpoint, AzureKeyCredential(key))
    
    documents = ["I love using Azure AI services!"]
    response = client.analyze_sentiment(documents)
    
    for doc in response:
        print(f"Sentiment: {doc.sentiment}")
        print(f"Confidence scores: {doc.confidence_scores}")
""")


def example_openai_integration():
    """
    Example of using OpenAI with Azure (requires authentication).
    """
    print("\n🤖 Azure OpenAI Example")
    print("="*60)
    
    if not check_azure_credentials():
        print("Skipping - authentication required")
        return
    
    print("""
To use Azure OpenAI, you would:

1. Install the SDK: pip install openai
2. Set up your credentials:
   - Endpoint: AZURE_OPENAI_ENDPOINT
   - Key: AZURE_OPENAI_KEY
   - Deployment: AZURE_OPENAI_DEPLOYMENT
3. Create a client and make requests

Example code:
    import openai
    import os
    
    openai.api_type = "azure"
    openai.api_base = os.getenv('AZURE_OPENAI_ENDPOINT')
    openai.api_key = os.getenv('AZURE_OPENAI_KEY')
    openai.api_version = "2023-05-15"
    
    response = openai.ChatCompletion.create(
        engine=os.getenv('AZURE_OPENAI_DEPLOYMENT'),
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello!"}
        ]
    )
    
    print(response.choices[0].message.content)
""")


def example_langchain_usage():
    """
    Example of using LangChain with Azure (requires authentication).
    """
    print("\n🔗 LangChain with Azure Example")
    print("="*60)
    
    print("""
To use LangChain with Azure OpenAI, you would:

1. Install the SDK: pip install langchain openai
2. Set up your Azure OpenAI credentials
3. Create a LangChain agent

Example code:
    from langchain.llms import AzureOpenAI
    from langchain.chains import LLMChain
    from langchain.prompts import PromptTemplate
    
    llm = AzureOpenAI(
        deployment_name=os.getenv('AZURE_OPENAI_DEPLOYMENT'),
        model_name="gpt-35-turbo",
    )
    
    template = "Tell me a {adjective} joke about {subject}."
    prompt = PromptTemplate(
        input_variables=["adjective", "subject"],
        template=template,
    )
    
    chain = LLMChain(llm=llm, prompt=prompt)
    
    result = chain.run(adjective="funny", subject="AI")
    print(result)
""")


def main():
    """Main function to run all examples."""
    print("🚀 Azure AI & LLM Examples")
    print("="*60)
    print("\nThis file demonstrates how to use Azure AI services")
    print("after authenticating with Azure CLI.\n")
    
    example_text_analytics()
    example_openai_integration()
    example_langchain_usage()
    
    print("\n" + "="*60)
    print("✅ Examples completed!")
    print("\nNext steps:")
    print("1. Authenticate: az login")
    print("2. Set up your Azure resources")
    print("3. Configure environment variables for your services")
    print("4. Start building with Azure AI!")


if __name__ == "__main__":
    main()

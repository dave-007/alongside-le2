"""
Azure AI Services Example

This script demonstrates how to use Azure AI services in the devcontainer.
Make sure to set your Azure credentials before running.
"""

from azure.identity import DefaultAzureCredential
from azure.ai.textanalytics import TextAnalyticsClient
import os


def analyze_sentiment(endpoint: str, texts: list[str]):
    """
    Analyze sentiment of text using Azure Text Analytics.
    
    Args:
        endpoint: Your Azure Cognitive Services endpoint
        texts: List of texts to analyze
    """
    try:
        # Authenticate using default Azure credential
        credential = DefaultAzureCredential()
        client = TextAnalyticsClient(endpoint=endpoint, credential=credential)
        
        # Analyze sentiment
        response = client.analyze_sentiment(documents=texts, show_opinion_mining=True)
        
        print("Sentiment Analysis Results:")
        print("-" * 50)
        
        for idx, doc in enumerate(response):
            if not doc.is_error:
                print(f"\nText {idx + 1}: {texts[idx][:50]}...")
                print(f"Sentiment: {doc.sentiment}")
                print(f"Confidence Scores:")
                print(f"  Positive: {doc.confidence_scores.positive:.2f}")
                print(f"  Neutral: {doc.confidence_scores.neutral:.2f}")
                print(f"  Negative: {doc.confidence_scores.negative:.2f}")
            else:
                print(f"\nText {idx + 1}: Error - {doc.error}")
                
    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure you've set up Azure credentials:")
        print("  az login")


def main():
    # Get endpoint from environment variable or use placeholder
    endpoint = os.getenv("AZURE_TEXT_ANALYTICS_ENDPOINT", 
                        "https://YOUR-RESOURCE.cognitiveservices.azure.com/")
    
    # Sample texts
    texts = [
        "I love working with Azure AI services! They're amazing.",
        "This is a neutral statement about technology.",
        "I'm disappointed with the results. This needs improvement."
    ]
    
    print("Azure AI Text Analytics Example")
    print("=" * 50)
    
    if "YOUR-RESOURCE" in endpoint:
        print("\n⚠️  Please set AZURE_TEXT_ANALYTICS_ENDPOINT environment variable")
        print("   export AZURE_TEXT_ANALYTICS_ENDPOINT='https://your-resource.cognitiveservices.azure.com/'")
        print("\nUsing sample output for demonstration...")
        print("\nSentiment Analysis Results:")
        print("-" * 50)
        for idx, text in enumerate(texts):
            print(f"\nText {idx + 1}: {text}")
            print("Sentiment: [Would show actual sentiment]")
    else:
        analyze_sentiment(endpoint, texts)


if __name__ == "__main__":
    main()

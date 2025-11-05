"""
LangChain Example

This script demonstrates how to use LangChain with various LLM providers.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def langchain_basic_example():
    """Basic LangChain example with OpenAI."""
    print("\n1. Basic LangChain Chain")
    print("-" * 50)
    
    try:
        from langchain_openai import ChatOpenAI
        from langchain.prompts import ChatPromptTemplate
        from langchain.schema.output_parser import StrOutputParser
        
        # Check if API key is set
        if not os.getenv("OPENAI_API_KEY"):
            print("⚠️  OPENAI_API_KEY not set")
            print("   Set it in .env file or environment")
            return
        
        # Create a simple chain
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
        prompt = ChatPromptTemplate.from_template(
            "Tell me a {adjective} joke about {topic}"
        )
        output_parser = StrOutputParser()
        
        # Combine into a chain using LCEL (LangChain Expression Language)
        chain = prompt | llm | output_parser
        
        # Invoke the chain
        print("\nChain structure: Prompt → LLM → Parser")
        print("Input: adjective='funny', topic='programming'")
        print("\n(Skipping actual API call to avoid usage)")
        print("Expected output: A funny programming joke")
        
    except ImportError as e:
        print(f"⚠️  Missing dependency: {e}")
    except Exception as e:
        print(f"Error: {e}")


def langchain_azure_example():
    """LangChain with Azure OpenAI."""
    print("\n2. LangChain with Azure OpenAI")
    print("-" * 50)
    
    try:
        from langchain_openai import AzureChatOpenAI
        
        # Check for Azure credentials
        required_vars = [
            "AZURE_OPENAI_API_KEY",
            "AZURE_OPENAI_ENDPOINT",
            "AZURE_OPENAI_DEPLOYMENT_NAME"
        ]
        
        missing = [var for var in required_vars if not os.getenv(var)]
        
        if missing:
            print(f"⚠️  Missing environment variables: {', '.join(missing)}")
            print("\nSet in .env file:")
            print("AZURE_OPENAI_API_KEY=your_key")
            print("AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com")
            print("AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4")
            return
        
        llm = AzureChatOpenAI(
            azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
            api_version="2024-02-01",
            temperature=0.7
        )
        
        print("✅ Azure OpenAI configured")
        print("(Skipping actual API call)")
        
    except ImportError as e:
        print(f"⚠️  Missing dependency: {e}")
    except Exception as e:
        print(f"Error: {e}")


def langchain_retrieval_example():
    """LangChain Retrieval-Augmented Generation (RAG) example."""
    print("\n3. LangChain RAG Pattern")
    print("-" * 50)
    
    print("""
RAG (Retrieval-Augmented Generation) pattern:

1. Load documents
   from langchain.document_loaders import TextLoader
   loader = TextLoader("document.txt")
   documents = loader.load()

2. Split into chunks
   from langchain.text_splitter import RecursiveCharacterTextSplitter
   splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
   chunks = splitter.split_documents(documents)

3. Create embeddings and vector store
   from langchain_openai import OpenAIEmbeddings
   from langchain.vectorstores import FAISS
   
   embeddings = OpenAIEmbeddings()
   vectorstore = FAISS.from_documents(chunks, embeddings)

4. Create retrieval chain
   from langchain.chains import RetrievalQA
   
   qa_chain = RetrievalQA.from_chain_type(
       llm=ChatOpenAI(),
       retriever=vectorstore.as_retriever()
   )

5. Query your documents
   result = qa_chain.invoke("What is this document about?")
    """)


def langchain_agent_example():
    """LangChain Agent example."""
    print("\n4. LangChain Agents")
    print("-" * 50)
    
    print("""
LangChain Agents can use tools to solve problems:

from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain.tools import Tool

# Define tools
def calculate(expression: str) -> str:
    return str(eval(expression))

tools = [
    Tool(
        name="Calculator",
        func=calculate,
        description="Useful for math calculations"
    )
]

# Create agent
llm = ChatOpenAI(model="gpt-4")
agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)

# Use agent
result = agent_executor.invoke({"input": "What is 25 * 4 + 10?"})
    """)


def main():
    print("LangChain Examples")
    print("=" * 50)
    
    print("\nLangChain is a framework for developing LLM applications.")
    print("It provides tools for:")
    print("  • Chaining LLM calls")
    print("  • Retrieval-Augmented Generation (RAG)")
    print("  • Agents with tool usage")
    print("  • Memory and state management")
    
    langchain_basic_example()
    langchain_azure_example()
    langchain_retrieval_example()
    langchain_agent_example()
    
    print("\n" + "=" * 50)
    print("For more examples, visit:")
    print("https://python.langchain.com/docs/get_started/introduction")


if __name__ == "__main__":
    main()

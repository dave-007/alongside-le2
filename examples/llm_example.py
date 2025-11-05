"""
LLM (Simon Willison's tool) Example

This script demonstrates how to use the LLM CLI tool programmatically.
"""

import subprocess
import os


def run_llm_command(prompt: str, model: str = None, system: str = None) -> str:
    """
    Run an LLM command and return the output.
    
    Args:
        prompt: The prompt to send to the LLM
        model: Optional model name (e.g., 'gpt-4', 'claude-3-opus')
        system: Optional system prompt
        
    Returns:
        The LLM response as a string
    """
    cmd = ["llm"]
    
    if model:
        cmd.extend(["-m", model])
    
    if system:
        cmd.extend(["-s", system])
    
    cmd.append(prompt)
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"Error: {result.stderr}"
            
    except subprocess.TimeoutExpired:
        return "Error: Command timed out"
    except FileNotFoundError:
        return "Error: LLM command not found. Make sure it's installed."
    except Exception as e:
        return f"Error: {e}"


def check_llm_installation():
    """Check if LLM is installed and configured."""
    try:
        result = subprocess.run(
            ["llm", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0
    except:
        return False


def main():
    print("LLM CLI Tool Example")
    print("=" * 50)
    
    # Check if LLM is installed
    if not check_llm_installation():
        print("\n⚠️  LLM is not installed or not in PATH")
        print("   Install with: pip install llm")
        return
    
    print("\n✅ LLM is installed")
    
    # Example 1: Simple prompt
    print("\n1. Simple Question:")
    print("-" * 50)
    prompt = "What is Python in one sentence?"
    print(f"Prompt: {prompt}")
    print(f"\nNote: Run 'llm \"{prompt}\"' in terminal to see actual response")
    print("(Skipping actual LLM call in example to avoid API usage)")
    
    # Example 2: With system prompt
    print("\n2. With System Prompt:")
    print("-" * 50)
    print("System: You are a Python expert")
    print("Prompt: Explain list comprehensions")
    print("\nCommand: llm -s 'You are a Python expert' 'Explain list comprehensions'")
    
    # Example 3: Piping content
    print("\n3. Piping Content:")
    print("-" * 50)
    print("Command: cat README.md | llm 'Summarize this document'")
    
    # Example 4: Using specific models
    print("\n4. Using Specific Models:")
    print("-" * 50)
    print("Command: llm -m gpt-4 'Your prompt here'")
    print("Command: llm -m claude-3-opus 'Your prompt here'")
    
    # Example 5: Listing models
    print("\n5. Available Models:")
    print("-" * 50)
    print("Command: llm models")
    
    # Example 6: Setting API keys
    print("\n6. Configuration:")
    print("-" * 50)
    print("Set OpenAI key: llm keys set openai")
    print("Set Anthropic key: llm keys set anthropic")
    
    print("\n" + "=" * 50)
    print("For more examples, visit: https://llm.datasette.io/")


if __name__ == "__main__":
    main()

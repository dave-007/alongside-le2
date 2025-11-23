#!/usr/bin/env python3
"""
Post-Authentication Setup Script
This script runs after user authentication to set up the environment.
"""

import subprocess
import sys
import os
from pathlib import Path


def run_command(command: list, description: str) -> bool:
    """
    Run a shell command and return success status.
    
    Args:
        command: Command to run as list
        description: Description of what the command does
        
    Returns:
        True if successful, False otherwise
    """
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            print(f"  ✅ Success")
            if result.stdout.strip():
                print(f"  Output: {result.stdout.strip()[:100]}")
            return True
        else:
            print(f"  ❌ Failed: {result.stderr.strip()[:100]}")
            return False
    except subprocess.TimeoutExpired:
        print(f"  ⏱️  Command timed out")
        return False
    except Exception as e:
        print(f"  ❌ Error: {str(e)}")
        return False


def setup_azure_resources() -> bool:
    """
    Set up Azure resources after authentication.
    
    Returns:
        True if successful, False otherwise
    """
    print("\n📦 Setting up Azure resources...")
    
    # List Azure subscriptions
    success = run_command(
        ['az', 'account', 'list', '--output', 'table'],
        "Listing Azure subscriptions"
    )
    
    if not success:
        return False
    
    # Show current subscription
    run_command(
        ['az', 'account', 'show', '--output', 'table'],
        "Showing current Azure subscription"
    )
    
    return True


def setup_github_config() -> bool:
    """
    Set up GitHub configuration after authentication.
    
    Returns:
        True if successful, False otherwise
    """
    print("\n🐙 Setting up GitHub configuration...")
    
    # Get current user
    success = run_command(
        ['gh', 'api', 'user', '--jq', '.login'],
        "Getting GitHub user info"
    )
    
    if not success:
        return False
    
    return True


def create_sample_workspace() -> bool:
    """
    Create sample workspace directories and files.
    
    Returns:
        True if successful, False otherwise
    """
    print("\n📁 Creating sample workspace...")
    
    workspace_dirs = [
        'workspace/notebooks',
        'workspace/data',
        'workspace/models',
        'workspace/scripts'
    ]
    
    for dir_path in workspace_dirs:
        path = Path(dir_path)
        path.mkdir(parents=True, exist_ok=True)
        print(f"  ✅ Created: {dir_path}")
    
    # Create a sample README
    readme_path = Path('workspace/README.md')
    if not readme_path.exists():
        readme_content = """# Workspace

This is your personal workspace for the Alongside Learning Environment.

## Directory Structure

- `notebooks/`: Jupyter notebooks for experiments
- `data/`: Data files and datasets
- `models/`: Trained models and model artifacts
- `scripts/`: Custom scripts and utilities

## Getting Started

1. Make sure you're authenticated with Azure and GitHub
2. Run `python scripts/check_authentication.py` to verify
3. Start experimenting with Azure AI and LLMs!

## Resources

- Azure AI Documentation: https://docs.microsoft.com/azure/ai-services/
- OpenAI API: https://platform.openai.com/docs
- LangChain: https://python.langchain.com/
"""
        readme_path.write_text(readme_content)
        print(f"  ✅ Created: {readme_path}")
    
    return True


def main() -> int:
    """
    Main function to run post-authentication setup.
    
    Returns:
        Exit code (0 if successful, 1 otherwise)
    """
    print("🚀 Post-Authentication Setup\n")
    print("="*60)
    
    # First, verify authentication
    print("\n🔐 Verifying authentication...")
    auth_check = subprocess.run(
        [sys.executable, 'scripts/check_authentication.py'],
        capture_output=True
    )
    
    if auth_check.returncode != 0:
        print("⚠️  Authentication verification failed!")
        print("Please run scripts/check_authentication.py for details.")
        return 1
    
    print("✅ Authentication verified!")
    
    # Run setup tasks
    tasks = [
        ("Azure Resources", setup_azure_resources),
        ("GitHub Configuration", setup_github_config),
        ("Sample Workspace", create_sample_workspace)
    ]
    
    failed_tasks = []
    
    for task_name, task_func in tasks:
        try:
            if not task_func():
                failed_tasks.append(task_name)
        except Exception as e:
            print(f"❌ Error in {task_name}: {str(e)}")
            failed_tasks.append(task_name)
    
    print("\n" + "="*60)
    
    if failed_tasks:
        print(f"⚠️  Setup completed with {len(failed_tasks)} failed task(s):")
        for task in failed_tasks:
            print(f"  - {task}")
        return 1
    else:
        print("✅ Post-authentication setup completed successfully!")
        print("\nYour environment is ready to use. Happy coding! 🎉")
        return 0


if __name__ == "__main__":
    sys.exit(main())

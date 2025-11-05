#!/usr/bin/env python3
"""
Authentication Check Script
This script checks if the user is authenticated with various services.
"""

import subprocess
import sys
import json
from typing import Dict, Tuple


def check_azure_auth() -> Tuple[bool, str]:
    """
    Check if user is authenticated with Azure CLI.
    
    Returns:
        Tuple of (is_authenticated, message)
    """
    try:
        result = subprocess.run(
            ['az', 'account', 'show'],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            account_info = json.loads(result.stdout)
            user = account_info.get('user', {}).get('name', 'Unknown')
            return True, f"Authenticated as: {user}"
        else:
            return False, "Not authenticated. Run 'az login' to authenticate."
    except FileNotFoundError:
        return False, "Azure CLI not installed"
    except subprocess.TimeoutExpired:
        return False, "Authentication check timed out"
    except json.JSONDecodeError:
        return False, "Could not parse Azure CLI output"
    except Exception as e:
        return False, f"Error checking authentication: {str(e)}"


def check_github_auth() -> Tuple[bool, str]:
    """
    Check if user is authenticated with GitHub CLI.
    
    Returns:
        Tuple of (is_authenticated, message)
    """
    try:
        result = subprocess.run(
            ['gh', 'auth', 'status'],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            # Parse the output to get username
            output = result.stdout + result.stderr
            if "Logged in to github.com" in output:
                # Extract username from output
                for line in output.split('\n'):
                    if 'account' in line.lower():
                        return True, f"Authenticated: {line.strip()}"
                return True, "Authenticated with GitHub"
            else:
                return False, "Not authenticated. Run 'gh auth login' to authenticate."
        else:
            return False, "Not authenticated. Run 'gh auth login' to authenticate."
    except FileNotFoundError:
        return False, "GitHub CLI not installed"
    except subprocess.TimeoutExpired:
        return False, "Authentication check timed out"
    except Exception as e:
        return False, f"Error checking authentication: {str(e)}"


def check_git_config() -> Tuple[bool, str]:
    """
    Check if Git is configured with user information.
    
    Returns:
        Tuple of (is_configured, message)
    """
    try:
        name_result = subprocess.run(
            ['git', 'config', '--global', 'user.name'],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        email_result = subprocess.run(
            ['git', 'config', '--global', 'user.email'],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        name = name_result.stdout.strip()
        email = email_result.stdout.strip()
        
        if name and email:
            return True, f"Configured as: {name} <{email}>"
        elif name:
            return False, "Git email not configured. Set with: git config --global user.email 'you@example.com'"
        elif email:
            return False, "Git name not configured. Set with: git config --global user.name 'Your Name'"
        else:
            return False, "Git not configured. Set with: git config --global user.name/user.email"
    except FileNotFoundError:
        return False, "Git not installed"
    except Exception as e:
        return False, f"Error checking Git config: {str(e)}"


def main() -> int:
    """
    Main function to check all authentication statuses.
    
    Returns:
        Exit code (0 if all checks pass, 1 otherwise)
    """
    print("🔐 Checking Authentication Status...\n")
    
    checks = {
        "Azure CLI": check_azure_auth,
        "GitHub CLI": check_github_auth,
        "Git Configuration": check_git_config
    }
    
    results: Dict[str, Tuple[bool, str]] = {}
    all_passed = True
    
    for service, check_func in checks.items():
        is_ok, message = check_func()
        results[service] = (is_ok, message)
        
        status_icon = "✅" if is_ok else "❌"
        print(f"{status_icon} {service}: {message}")
        
        if not is_ok:
            all_passed = False
    
    print("\n" + "="*60)
    
    if all_passed:
        print("✅ All authentication checks passed!")
        print("You are ready to use the development environment.")
        return 0
    else:
        print("⚠️  Some authentication checks failed.")
        print("Please authenticate with the services listed above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

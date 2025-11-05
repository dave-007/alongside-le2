"""
Tests for authentication check script.
"""

import subprocess
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock
import pytest

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from check_authentication import (
    check_azure_auth,
    check_github_auth,
    check_git_config
)


class TestAzureAuth:
    """Tests for Azure authentication checks."""
    
    @patch('subprocess.run')
    def test_azure_auth_success(self, mock_run):
        """Test successful Azure authentication."""
        mock_run.return_value = MagicMock(
            returncode=0,
            stdout='{"user": {"name": "test@example.com"}}'
        )
        
        is_auth, message = check_azure_auth()
        
        assert is_auth is True
        assert "test@example.com" in message
        mock_run.assert_called_once()
    
    @patch('subprocess.run')
    def test_azure_auth_not_authenticated(self, mock_run):
        """Test Azure not authenticated."""
        mock_run.return_value = MagicMock(
            returncode=1,
            stdout='',
            stderr='Please run "az login"'
        )
        
        is_auth, message = check_azure_auth()
        
        assert is_auth is False
        assert "Not authenticated" in message
    
    @patch('subprocess.run')
    def test_azure_auth_cli_not_installed(self, mock_run):
        """Test Azure CLI not installed."""
        mock_run.side_effect = FileNotFoundError()
        
        is_auth, message = check_azure_auth()
        
        assert is_auth is False
        assert "not installed" in message
    
    @patch('subprocess.run')
    def test_azure_auth_timeout(self, mock_run):
        """Test Azure authentication timeout."""
        mock_run.side_effect = subprocess.TimeoutExpired('az', 10)
        
        is_auth, message = check_azure_auth()
        
        assert is_auth is False
        assert "timed out" in message


class TestGitHubAuth:
    """Tests for GitHub authentication checks."""
    
    @patch('subprocess.run')
    def test_github_auth_success(self, mock_run):
        """Test successful GitHub authentication."""
        mock_run.return_value = MagicMock(
            returncode=0,
            stdout='Logged in to github.com as testuser',
            stderr=''
        )
        
        is_auth, message = check_github_auth()
        
        assert is_auth is True
        assert "Authenticated" in message
    
    @patch('subprocess.run')
    def test_github_auth_not_authenticated(self, mock_run):
        """Test GitHub not authenticated."""
        mock_run.return_value = MagicMock(
            returncode=1,
            stdout='',
            stderr='Not logged in'
        )
        
        is_auth, message = check_github_auth()
        
        assert is_auth is False
        assert "Not authenticated" in message
    
    @patch('subprocess.run')
    def test_github_auth_cli_not_installed(self, mock_run):
        """Test GitHub CLI not installed."""
        mock_run.side_effect = FileNotFoundError()
        
        is_auth, message = check_github_auth()
        
        assert is_auth is False
        assert "not installed" in message


class TestGitConfig:
    """Tests for Git configuration checks."""
    
    @patch('subprocess.run')
    def test_git_config_success(self, mock_run):
        """Test successful Git configuration."""
        def run_side_effect(*args, **kwargs):
            command = args[0]
            if 'user.name' in command:
                return MagicMock(returncode=0, stdout='Test User\n')
            elif 'user.email' in command:
                return MagicMock(returncode=0, stdout='test@example.com\n')
            return MagicMock(returncode=0, stdout='')
        
        mock_run.side_effect = run_side_effect
        
        is_configured, message = check_git_config()
        
        assert is_configured is True
        assert "Test User" in message
        assert "test@example.com" in message
    
    @patch('subprocess.run')
    def test_git_config_missing_email(self, mock_run):
        """Test Git configuration with missing email."""
        def run_side_effect(*args, **kwargs):
            command = args[0]
            if 'user.name' in command:
                return MagicMock(returncode=0, stdout='Test User\n')
            elif 'user.email' in command:
                return MagicMock(returncode=1, stdout='')
            return MagicMock(returncode=0, stdout='')
        
        mock_run.side_effect = run_side_effect
        
        is_configured, message = check_git_config()
        
        assert is_configured is False
        assert "email not configured" in message
    
    @patch('subprocess.run')
    def test_git_config_not_configured(self, mock_run):
        """Test Git not configured."""
        mock_run.return_value = MagicMock(returncode=1, stdout='')
        
        is_configured, message = check_git_config()
        
        assert is_configured is False
        assert "not configured" in message
    
    @patch('subprocess.run')
    def test_git_not_installed(self, mock_run):
        """Test Git not installed."""
        mock_run.side_effect = FileNotFoundError()
        
        is_configured, message = check_git_config()
        
        assert is_configured is False
        assert "not installed" in message


class TestAuthenticationIntegration:
    """Integration tests for authentication checks."""
    
    def test_check_authentication_script_exists(self):
        """Test that the authentication script exists and is executable."""
        script_path = Path(__file__).parent.parent / 'scripts' / 'check_authentication.py'
        assert script_path.exists()
        assert script_path.is_file()
    
    def test_authentication_script_runs(self):
        """Test that the authentication script can be run."""
        script_path = Path(__file__).parent.parent / 'scripts' / 'check_authentication.py'
        
        # Run the script (it may fail auth checks, but should not error)
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Script should run without exceptions
        # Exit code may be 1 if not authenticated, which is expected
        assert result.returncode in [0, 1]
        assert "Checking Authentication Status" in result.stdout


class TestPostAuthSetup:
    """Tests for post-authentication setup script."""
    
    def test_post_auth_setup_script_exists(self):
        """Test that the post-auth setup script exists and is executable."""
        script_path = Path(__file__).parent.parent / 'scripts' / 'post_auth_setup.py'
        assert script_path.exists()
        assert script_path.is_file()
    
    def test_post_auth_setup_script_structure(self):
        """Test that the post-auth setup script has proper structure."""
        script_path = Path(__file__).parent.parent / 'scripts' / 'post_auth_setup.py'
        content = script_path.read_text()
        
        # Check for required functions
        assert 'def setup_azure_resources' in content
        assert 'def setup_github_config' in content
        assert 'def create_sample_workspace' in content
        assert 'def main' in content


if __name__ == '__main__':
    pytest.main([__file__, '-v'])

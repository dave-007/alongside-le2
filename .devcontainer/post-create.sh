#!/bin/bash
set -e

echo "🚀 Running post-create setup for Alongside Learning Environment..."

# Update package lists
echo "📦 Updating package lists..."
sudo apt-get update

# Install common development tools
echo "🔧 Installing development tools..."
sudo apt-get install -y \
    build-essential \
    curl \
    wget \
    vim \
    jq \
    tree \
    htop

# Install Python packages for Azure AI and LLM development
echo "🐍 Installing Python packages..."
pip install --upgrade pip
pip install \
    azure-ai-textanalytics \
    azure-cognitiveservices-speech \
    openai \
    langchain \
    transformers \
    pytest \
    pytest-asyncio \
    black \
    pylint \
    requests

# Install Node.js packages
echo "📦 Installing Node.js packages..."
npm install -g typescript ts-node @azure/functions-core-tools

# Create workspace directories
echo "📁 Creating workspace directories..."
mkdir -p /workspace/{scripts,tests,samples}

# Set up git configuration (if not already configured)
echo "⚙️ Configuring Git..."
if [ -z "$(git config --global user.email)" ]; then
    echo "Git user.email not configured. You can set it later with: git config --global user.email 'you@example.com'"
fi
if [ -z "$(git config --global user.name)" ]; then
    echo "Git user.name not configured. You can set it later with: git config --global user.name 'Your Name'"
fi

echo "✅ Post-create setup completed successfully!"
echo ""
echo "🎉 Your development environment is ready!"
echo ""
echo "Next steps:"
echo "  1. Authenticate with Azure CLI: az login"
echo "  2. Authenticate with GitHub CLI: gh auth login"
echo "  3. Run tests: pytest tests/"
echo ""

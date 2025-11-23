#!/bin/bash

# Verification script for Alongside LE2 devcontainer
# This script checks that all required tools and dependencies are installed

echo "======================================================"
echo "Alongside LE2 DevContainer Verification"
echo "======================================================"
echo ""

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to check command existence
check_command() {
    if command -v "$1" &> /dev/null; then
        echo -e "${GREEN}✓${NC} $1 is installed"
        if [ "$2" = "version" ]; then
            echo "  Version: $($1 --version 2>&1 | head -n 1)"
        fi
        return 0
    else
        echo -e "${RED}✗${NC} $1 is NOT installed"
        return 1
    fi
}

# Function to check Python package
check_python_package() {
    if python -c "import $1" &> /dev/null; then
        echo -e "${GREEN}✓${NC} Python package '$1' is installed"
        return 0
    else
        echo -e "${RED}✗${NC} Python package '$1' is NOT installed"
        return 1
    fi
}

# Counter for issues
issues=0

echo "Checking Base System..."
echo "------------------------------------------------------"
check_command "python" "version" || ((issues++))
check_command "pip" "version" || ((issues++))
check_command "dotnet" "version" || ((issues++))
check_command "git" "version" || ((issues++))
echo ""

echo "Checking Azure Tools..."
echo "------------------------------------------------------"
check_command "az" "version" || ((issues++))
echo ""

echo "Checking AI/LLM Tools..."
echo "------------------------------------------------------"
check_command "llm" "version" || ((issues++))
check_command "fabric" "version" || ((issues++))
echo ""

echo "Checking Python AI Libraries..."
echo "------------------------------------------------------"
check_python_package "openai" || ((issues++))
check_python_package "anthropic" || ((issues++))
check_python_package "langchain" || ((issues++))
check_python_package "azure.ai.ml" || ((issues++))
check_python_package "azure.ai.textanalytics" || ((issues++))
check_python_package "azure.identity" || ((issues++))
echo ""

echo "Checking Data Science Libraries..."
echo "------------------------------------------------------"
check_python_package "numpy" || ((issues++))
check_python_package "pandas" || ((issues++))
check_python_package "sklearn" || ((issues++))
check_python_package "matplotlib" || ((issues++))
check_python_package "jupyter" || ((issues++))
echo ""

echo "Checking Development Tools..."
echo "------------------------------------------------------"
check_python_package "black" || ((issues++))
check_python_package "pylint" || ((issues++))
check_python_package "pytest" || ((issues++))
check_python_package "mypy" || ((issues++))
echo ""

echo "Checking Additional Utilities..."
echo "------------------------------------------------------"
check_python_package "requests" || ((issues++))
check_python_package "dotenv" || ((issues++))
check_python_package "yaml" || ((issues++))
echo ""

echo "======================================================"
if [ $issues -eq 0 ]; then
    echo -e "${GREEN}✓ All checks passed!${NC}"
    echo "Your devcontainer is ready to use."
else
    echo -e "${YELLOW}⚠ Found $issues issue(s)${NC}"
    echo "Some components may need to be reinstalled."
fi
echo "======================================================"
echo ""

# Additional information
echo "Next Steps:"
echo "------------------------------------------------------"
echo "1. Login to Azure:"
echo "   az login"
echo ""
echo "2. Configure LLM API keys:"
echo "   llm keys set openai"
echo "   llm keys set anthropic"
echo ""
echo "3. Setup Fabric:"
echo "   fabric --setup"
echo "   fabric --update"
echo ""
echo "4. Check the documentation:"
echo "   - Quick Start: .devcontainer/QUICK_START.md"
echo "   - Full Docs: .devcontainer/README.md"
echo "   - Examples: examples/README.md"
echo ""

exit $issues

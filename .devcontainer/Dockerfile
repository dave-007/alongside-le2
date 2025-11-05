# Use the latest Ubuntu LTS as base
FROM ubuntu:latest

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHON_VERSION=3.11
ENV DOTNET_VERSION=8.0

# Install system dependencies
RUN apt-get update && apt-get install -y \
    # Basic utilities
    curl \
    wget \
    git \
    vim \
    nano \
    build-essential \
    software-properties-common \
    apt-transport-https \
    ca-certificates \
    gnupg \
    lsb-release \
    unzip \
    # Python build dependencies
    libssl-dev \
    libffi-dev \
    python3-dev \
    python3-pip \
    python3-venv \
    # Additional tools
    jq \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Install Python 3.11+
RUN add-apt-repository ppa:deadsnakes/ppa -y \
    && apt-get update \
    && apt-get install -y python3.11 python3.11-venv python3.11-dev \
    && update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1 \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1 \
    && curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11 \
    && rm -rf /var/lib/apt/lists/*

# Install .NET SDK 8.0
RUN wget https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/packages-microsoft-prod.deb -O packages-microsoft-prod.deb \
    && dpkg -i packages-microsoft-prod.deb \
    && rm packages-microsoft-prod.deb \
    && apt-get update \
    && apt-get install -y dotnet-sdk-8.0 \
    && rm -rf /var/lib/apt/lists/*

# Install Azure CLI
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash

# Install Python AI/ML libraries
RUN pip install --no-cache-dir \
    # Azure AI SDKs
    azure-ai-ml \
    azure-ai-textanalytics \
    azure-ai-formrecognizer \
    azure-cognitiveservices-speech \
    azure-identity \
    azure-storage-blob \
    azure-keyvault-secrets \
    # OpenAI and LLM libraries
    openai \
    anthropic \
    langchain \
    langchain-openai \
    langchain-community \
    # Data science and ML
    numpy \
    pandas \
    scikit-learn \
    matplotlib \
    seaborn \
    jupyter \
    ipykernel \
    # Development tools
    black \
    pylint \
    flake8 \
    pytest \
    mypy \
    # Additional useful libraries
    requests \
    python-dotenv \
    pyyaml \
    click

# Install Simon Willison's LLM
RUN pip install --no-cache-dir llm

# Install LLM plugins for various AI models
RUN llm install llm-gpt4all \
    && llm install llm-claude-3 \
    && llm install llm-gemini

# Install Daniel Miessler's Fabric
RUN pip install --no-cache-dir pipx \
    && pipx ensurepath

# Switch to non-root user for Fabric installation
USER $USERNAME
ENV PATH="/home/$USERNAME/.local/bin:${PATH}"

# Install Fabric using pipx as the vscode user
RUN pipx install fabric

# Setup Fabric - this creates the config directory
RUN mkdir -p /home/$USERNAME/.config/fabric

# Switch back to root for final setup
USER root

# Install additional Azure AI tools
RUN pip install --no-cache-dir \
    azure-ai-inference \
    azure-ai-projects \
    promptflow \
    promptflow-tools

# Set up working directory
WORKDIR /workspace

# Give ownership to vscode user
RUN chown -R $USERNAME:$USERNAME /workspace

# Switch to non-root user
USER $USERNAME

# Set the default shell
SHELL ["/bin/bash", "-c"]

# Display versions on container start (for verification)
CMD ["/bin/bash"]

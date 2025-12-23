#!/bin/bash

# setup.sh - Initialize development environment with UV

set -e

echo "🚀 Setting up RSS Digest Bot development environment..."

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ UV is not installed. Installing UV..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.cargo/bin:$PATH"
fi

echo "✓ UV is installed"

# Create virtual environment
echo "📦 Creating virtual environment..."
uv venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
uv pip install \
    bedrock-agentcore \
    bedrock-agentcore-starter-toolkit \
    boto3 \
    mcp \
    feedparser \
    jupyter \
    requests \
    httpx

echo "✓ Dependencies installed"

# Sync project dependencies
echo "🔄 Syncing project dependencies..."
uv sync

echo ""
echo "✅ Setup complete!"
echo ""
echo "To activate the virtual environment, run:"
echo "  source .venv/bin/activate"
echo ""
echo "To start the Jupyter notebook, run:"
echo "  jupyter notebook mcp-deploy.ipynb"

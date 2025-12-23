# RSS Digest Bot

A Python-based RSS Digest Bot powered by the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) that fetches items from your favorite tech blogs and news sites, and returns AI-generated summaries via Claude.

## Features

- Pulls the latest posts from:
  - OpenAI Blog
  - Anthropic Blog
  - Google AI Blog
  - AWS Machine Learning Blog
  - Hugging Face Blog
  - Meta AI Blog
  - The Batch (Andrew Ng)
  - Hacker News (AI)
  - ArXiv (Computer Science)
  - And more...
- On-demand summaries driven by Claude (or any other LLM client)
- Easy to run locally or deploy to AWS Bedrock AgentCore Runtime
- Minimal dependencies: `feedparser`, `mcp[cli]`

## Quick Start - Local Development

### 1. Setup Environment

```bash
chmod +x setup.sh
./setup.sh
source .venv/bin/activate
```

### 2. Run Locally

```bash
python main.py
```

### 3. Configure Claude Desktop

Edit `~/.claude/mcp.json`:

```json
{
  "mcpServers": {
    "rss-digest-bot": {
      "command": "/full/path/to/your/project/.venv/bin/mcp",
      "args": ["run", "main.py"],
      "transport": "stdio"
    }
  }
}
```

Restart Claude Desktop.

## Deploy to AWS Bedrock AgentCore

For production deployment to AWS with OAuth authentication:

### 1. Setup

```bash
chmod +x setup.sh
./setup.sh
source .venv/bin/activate
```

### 2. Deploy

```bash
jupyter notebook mcp-deploy.ipynb
```

Run all cells. The notebook will:
- Create Cognito OAuth pool
- Deploy MCP server to AgentCore Runtime
- Generate test scripts and Claude configuration

### 3. Test

```bash
export AGENT_ARN="<from deployment_details.json>"
export BEARER_TOKEN="<from notebook output>"
python test_remote_mcp.py
```

### 4. Configure Claude Desktop

Copy the configuration from the notebook output to `~/.claude/mcp.json` and restart Claude Desktop.

## Documentation

- **[QUICK_START.md](QUICK_START.md)** - Quick reference for deployment
- **[DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)** - Detailed deployment instructions
- **[REFACTORING_SUMMARY.md](REFACTORING_SUMMARY.md)** - Technical changes and improvements

## Project Structure

```
.
├── main.py                 # MCP server entry point
├── server.py              # FastMCP server configuration
├── tools/
│   └── rss_tools.py       # RSS feed tools
├── utils/
│   └── rss_reader.py      # RSS parsing utilities
├── setup.sh               # Environment setup script
├── mcp-deploy.ipynb       # Deployment notebook
├── pyproject.toml         # Project dependencies
└── README.md              # This file
```

## Dependencies

### Core
- `feedparser>=6.0.11` - RSS feed parsing
- `mcp[cli]>=1.9.4` - Model Context Protocol

### Deployment (optional)
- `bedrock-agentcore>=1.0.0` - AWS AgentCore SDK
- `bedrock-agentcore-starter-toolkit>=1.0.0` - Deployment tools
- `boto3>=1.26.0` - AWS SDK
- `requests>=2.31.0` - HTTP client
- `httpx>=0.24.0` - Async HTTP client

### Development (optional)
- `jupyter>=1.0.0` - Jupyter notebooks
- `ipython>=8.0.0` - Interactive Python

## Installation Methods

### Using UV (Recommended)

```bash
./setup.sh
source .venv/bin/activate
```

### Manual Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[deploy,dev]"
```

## Configuration

### Local Development

No configuration needed. The bot uses default RSS feeds defined in `tools/rss_tools.py`.

### AWS Deployment

Configuration is handled by the deployment notebook:
1. Creates Cognito user pool for OAuth
2. Sets up machine-to-machine credentials
3. Deploys to AgentCore Runtime
4. Generates OAuth tokens

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for details.

## Security

- OAuth 2.0 machine-to-machine authentication for remote deployments
- Sensitive configuration files are in `.gitignore`
- All connections use HTTPS
- Short-lived OAuth tokens (typically 1 hour)

## Troubleshooting

### Setup Issues

```bash
# Reset environment
rm -rf .venv
./setup.sh
source .venv/bin/activate
```

### Deployment Issues

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) troubleshooting section.

### Claude Desktop Connection

1. Verify MCP server is running
2. Check `~/.claude/mcp.json` syntax
3. Restart Claude Desktop
4. Check Claude Desktop logs

## License

MIT

## Contributing

Contributions welcome! Please feel free to submit a Pull Request.

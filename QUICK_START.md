# Quick Start - Deploy RSS Digest Bot to AgentCore

## 1. Setup (One-time)

```bash
chmod +x setup.sh
./setup.sh
source .venv/bin/activate
```

## 2. Deploy

```bash
jupyter notebook mcp-deploy.ipynb
```

Run all cells. The notebook will:
- Create Cognito OAuth pool
- Deploy MCP server to AgentCore
- Generate test scripts and Claude config

## 3. Test

After deployment, set environment variables from `deployment_details.json`:

```bash
export AGENT_ARN="<from deployment_details.json>"
export BEARER_TOKEN="<from notebook output>"
python test_remote_mcp.py
```

## 4. Configure Claude Desktop

Copy the configuration from the notebook output to `~/.claude/mcp.json`:

```json
{
  "mcpServers": {
    "rss-digest-bot-remote": {
      "url": "https://bedrock-agentcore.{REGION}.amazonaws.com/runtimes/{ENCODED_ARN}/invocations?qualifier=DEFAULT",
      "auth": {
        "type": "oauth2",
        "clientId": "...",
        "clientSecret": "...",
        "tokenUrl": "...",
        "scopes": ["mcp-server/invoke"]
      }
    }
  }
}
```

Restart Claude Desktop.

## Files Generated

- `cognito_config.json` - OAuth configuration
- `deployment_details.json` - Deployment details and ARN
- `test_remote_mcp.py` - Test client script
- `requirements.txt` - Python dependencies

## Troubleshooting

**Setup fails**: Delete `.venv` and run `./setup.sh` again

**Deployment fails**: Check AWS credentials with `aws sts get-caller-identity`

**Test fails**: Verify `AGENT_ARN` and `BEARER_TOKEN` are set correctly

**Claude connection fails**: Verify URL encoding in config (`:` → `%3A`, `/` → `%2F`)

## Full Documentation

See `DEPLOYMENT_GUIDE.md` for detailed information.

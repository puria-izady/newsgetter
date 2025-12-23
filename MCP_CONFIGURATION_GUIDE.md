# Configuring Your Python MCP Server in Claude Desktop

When building a Python-based MCP (Model Context Protocol) server, getting the configuration right in Claude Desktop can be tricky. This guide walks through the common pitfalls and the correct approach.

## The Problem

If you try to configure your MCP server with just the basic command and args, you'll likely encounter this error:

```
File not found: /main.py
```

This happens because Claude Desktop doesn't automatically resolve relative paths or respect the `cwd` (current working directory) parameter the way you might expect.

## The Solution

Use the **full absolute path** to your Python script in the `args` array, combined with the `mcp run` command.

### Configuration

Add this to your `claude_desktop_config.json` (located at `~/Library/Application Support/Claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "your-server-name": {
      "command": "/full/path/to/your/project/.venv/bin/mcp",
      "args": ["run", "/full/path/to/your/project/main.py"]
    }
  }
}
```

### Example

For a project at `/Users/username/Code/my-mcp-server`:

```json
{
  "mcpServers": {
    "my-mcp-server": {
      "command": "/Users/username/Code/my-mcp-server/.venv/bin/mcp",
      "args": ["run", "/Users/username/Code/my-mcp-server/main.py"]
    }
  }
}
```

## Why This Works

- **`command`**: Points to the `mcp` CLI tool in your virtual environment
- **`args`**: The `run` subcommand with the **absolute path** to your entry point
- The absolute path ensures Claude Desktop can find your script regardless of its working directory

## What Doesn't Work

❌ **Relative paths** — Claude Desktop won't resolve `./main.py` or `main.py`

```json
{
  "args": ["run", "main.py"]  // ❌ File not found
}
```

❌ **Relying on `cwd`** — The `cwd` parameter may not be respected by the `mcp run` command

```json
{
  "command": "/path/to/.venv/bin/mcp",
  "args": ["run", "main.py"],
  "cwd": "/path/to/project"  // ❌ Still won't work
}
```

❌ **Using `python` directly** — This bypasses the MCP CLI wrapper

```json
{
  "command": "/path/to/.venv/bin/python",
  "args": ["main.py"]  // ❌ Doesn't use MCP protocol properly
}
```

## Verification

After updating your config:

1. **Restart Claude Desktop** completely (quit and relaunch)
2. **Check Developer Settings** → Look for your server under "Developer"
3. **Verify it's Enabled** — Toggle it on if needed
4. **Test in Chat** — Click ⚙️ (Search & tools) and confirm your server appears and is toggled on

## Your MCP Server Entry Point

Your `main.py` should initialize and run the MCP server:

```python
from server import mcp
import sys
import tools.rss_tools

if __name__ == "__main__":
    # STDIO transport for direct stdin/stdout JSON-RPC
    mcp.run()
```

The `mcp.run()` call handles the JSON-RPC protocol over stdin/stdout, which is what Claude Desktop expects.

## Summary

The key takeaway: **always use absolute paths in the `args` array** when configuring Python MCP servers in Claude Desktop. This eliminates path resolution issues and ensures your server starts correctly every time.

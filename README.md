# MCP Client Demo

A minimal Model Context Protocol (MCP) client implementation for testing and interacting with MCP servers.

## Features

- **Connect to Local MCP Servers**: Connects to any MCP server script via stdio.
- **Inspect Server Capabilities**: List available tools, prompts, and resources exposed by the server.
- **Interactive Chat**: Chat with the MCP server using OpenAI's models, allowing the LLM to use the server's tools.

## Prerequisites

- Python 3.10 or higher
- [Poetry](https://python-poetry.org/) for dependency management
- An OpenAI API key (for chat functionality)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd mcp-demo
   ```

2. **Install dependencies:**
   ```bash
   poetry install
   ```

3. **Configure Environment:**
   Create a `.env` file in the project root and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

The CLI tool `mcp-demo` is the entry point. You need to provide the path to the MCP server script you want to interact with.

### 1. List Server Members

To see what tools, prompts, and resources a server provides:

```bash
poetry run mcp-demo mcp_server/mcp_server.py --members
```

Example Output:
```text
MCP Server Members
==================================================

TOOLS (1):
------------------------------
 > echo - Echo back the message.

PROMPTS (1):
------------------------------
 > greeting_prompt - A simple greeting prompt.

RESOURCES (1):
------------------------------
 > greeting_file - The greeting text file.

==================================================
```

### 2. Interactive Chat

To start a chat session where the AI can use the server's tools:

```bash
poetry run mcp-demo mcp_server/mcp_server.py --chat
```

You can then type messages, and the client will use OpenAI to process your request, potentially calling tools on the MCP server (like `echo` in the example server).

## Project Structure

- `src/mcp_demo/`: Source code for the MCP client.
  - `cli.py`: Command-line argument parsing.
  - `mcp_client.py`: Core client logic, handling connection and member listing.
  - `chat.py`: Chat loop implementation.
  - `handlers.py`: OpenAI integration for tool calling.
- `mcp_server/`: A simple example MCP server for testing.
  - `mcp_server.py`: The server script.
  - `greeting.txt`: A resource file used by the server.

## Development

To add more features or modify the client, the main logic resides in `src/mcp_demo/mcp_client.py`. The `MCPClient` class manages the connection lifecycle and interaction with the `mcp` library.

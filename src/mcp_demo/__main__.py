import asyncio
from dotenv import load_dotenv

from mcp_demo.cli import parse_args
from mcp_demo.mcp_client import MCPClient

async def main() -> None:
    """Run the MCP demo with the specified options."""
    load_dotenv()
    args = parse_args()
    if not args.server_path.exists():
        print(f"Error: Server script '{args.server_path}' not found")
        return

    try:
        async with MCPClient(str(args.server_path)) as client:
            if args.members:
                await client.list_all_members()
            elif args.chat:
                await client.run_chat()
    except RuntimeError as e:
        print(e)

def cli_main():
    """Entry point for the mcp-demo CLI app."""
    asyncio.run(main())

if __name__ == "__main__":
    asyncio.run(main())

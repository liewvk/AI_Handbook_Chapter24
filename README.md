# AI Handbook — Chapter 24

Python examples and Model Context Protocol (MCP) demos for Chapter 24 of the AI Handbook.

## Overview

The examples demonstrate MCP tools, resources, and prompts using a small sample bookstore catalogue, along with input validation and a safe dispatch simulation.

## Files

- `example_24_1.py` — reports the Python interpreter and checks whether the `mcp` package is installed.
- `example_24_2.py` — calculates a quotation for a sample book catalogue.
- `example_24_7.py` — demonstrates quotation validation and error responses.
- `example_24_8.py` — demonstrates a simulated dispatch flow with approval and ID checks.
- `mcp_server.py` — exposes `quote_book` as an MCP tool.
- `resource_server.py` — exposes a sample bookstore catalogue as an MCP resource.
- `prompt_server.py` — exposes an MCP prompt that explains an AI term.
- `book_tools_server.py` — combines an MCP tool, resource, and prompt in one server.

## Requirements

- Python 3
- Visual Studio Python tooling for opening the included `.pyproj`/`.slnx` files
- The MCP SDK for the MCP servers:

```bash
python -m pip install mcp
```

## Running the examples

From the repository root:

```bash
python example_24_1.py
python example_24_2.py
python example_24_7.py
python example_24_8.py
```

Run an MCP server with stdio transport:

```bash
python mcp_server.py
python resource_server.py
python prompt_server.py
python book_tools_server.py
```

The MCP server processes remain waiting for an MCP client connection when they are started directly.

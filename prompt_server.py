from mcp.server.fastmcp import FastMCP
 
mcp = FastMCP('Learning Prompts')
 
@mcp.prompt()
def explain_ai(term: str) -> str:
    """Build a short learning prompt for an AI term."""
    return (f'Explain {term} in simple English. '
            'Give one real-world example and one limitation.')
 
if __name__ == '__main__':
    mcp.run(transport='stdio')


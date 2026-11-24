from mcp.server.fastmcp import FastMCP
 
mcp = FastMCP('Book Reference Server')
 
@mcp.resource('bookstore://catalogue')
def catalogue() -> str:
    """Provide a read-only catalogue for a demo."""
    return ('AI Handbook: MYR 40; '
            'Python Guide: MYR 55; '
            'All prices are illustrative.')
 
if __name__ == '__main__':
    mcp.run(transport='stdio')


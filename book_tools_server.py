from mcp.server.fastmcp import FastMCP
 
mcp = FastMCP('Bookstore Learning Demo')
BOOKS = {'AI Handbook': 40.0, 'Python Guide': 55.0}
 
@mcp.tool()
def book_quote(title: str, qty: int) -> dict:
    """Return a demo quotation without placing an order."""
    if title not in BOOKS:
        raise ValueError('Unknown book title')
    if type(qty) is not int or qty < 1 or qty > 20:
        raise ValueError('Invalid quantity')
    return {'title': title, 'qty': qty,
            'amount_myr': round(BOOKS[title] * qty, 2)}
 
@mcp.resource('bookstore://books')
def list_books() -> str:
    """Return the sample catalogue."""
    return '\n'.join(f'{name}: MYR {price:.2f}'
                     for name, price in BOOKS.items())
 
@mcp.prompt()
def explain_book(title: str) -> str:
    """Prepare a beginner-level book explanation request."""
    return f'Explain who might benefit from {title}.'
 
if __name__ == '__main__':
    mcp.run(transport='stdio')


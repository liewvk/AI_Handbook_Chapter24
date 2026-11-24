from mcp.server.fastmcp import FastMCP
 
mcp = FastMCP('Beginner Book Tools')
CATALOGUE = {'AI Handbook': 40.0, 'Python Guide': 55.0}
 
@mcp.tool()
def quote_book(title: str, quantity: int) -> dict:
    """Calculate a read-only book quotation in MYR."""
    if title not in CATALOGUE:
        raise ValueError('Unknown title')
    if type(quantity) is not int or not 1 <= quantity <= 20:
        raise ValueError('Quantity must be from 1 to 20')
    amount = round(CATALOGUE[title] * quantity, 2)
    return {'title': title, 'quantity': quantity,
            'subtotal': amount, 'currency': 'MYR'}
 
if __name__ == '__main__':
    mcp.run(transport='stdio')


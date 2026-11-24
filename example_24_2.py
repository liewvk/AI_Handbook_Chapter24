CATALOGUE = {'AI Handbook': 40.0, 'Python Guide': 55.0}
 
def quote(title: str, quantity: int) -> dict:
    if title not in CATALOGUE:
        raise ValueError('Unknown title')
    if type(quantity) is not int or not 1 <= quantity <= 20:
        raise ValueError('Quantity must be from 1 to 20')
    subtotal = round(CATALOGUE[title] * quantity, 2)
    return {'title': title, 'quantity': quantity,
            'subtotal': subtotal, 'currency': 'MYR'}
 
print(quote('AI Handbook', 2))


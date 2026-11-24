PRICES = {'AI Handbook': 40.0}
 
def quote(title, qty):
    if title not in PRICES:
        return {'error': 'Unknown title'}
    if type(qty) is not int or not 1 <= qty <= 20:
        return {'error': 'Invalid quantity'}
    return {'amount_myr': round(PRICES[title] * qty, 2)}
 
for title, qty in [('AI Handbook', 3),
                   ('AI Handbook', -2), ('Missing', 1)]:
    print(quote(title, qty))



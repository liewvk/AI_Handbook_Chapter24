def simulate_dispatch(order_id: str, approved: bool) -> str:
    if approved is not True:
        return 'Dispatch refused: approval required'
    if not order_id.startswith('TEST-'):
        return 'Dispatch refused: demo IDs only'
    return f'Simulation: dispatch {order_id}'
 
print(simulate_dispatch('TEST-42', False))
print(simulate_dispatch('TEST-42', True))


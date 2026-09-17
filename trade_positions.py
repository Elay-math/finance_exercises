trades = [
    ("AAPL", 10),
    ("MSFT", 20),
    ("AAPL", -4),
    ("GOOG", 7),
    ("MSFT", -20),
    ("TSLA", -7)]
def calculate_positions(trades):
    positions = {}
    for symbol, quantity in trades:
        if symbol in positions:
            positions[symbol] += quantity
        else:
            positions[symbol] = quantity
    positions = {
    symbol: quantity
    for symbol, quantity in positions.items()
    if quantity != 0
    }
    positions = sorted(positions.items(), key=lambda item: (-abs(item[1]), item[0]))
    return positions
print(calculate_positions(trades))
# Problem 001 — Calculate Trading Positions

## Problem Description

Given a list of trades, where each trade is represented by a pair `(symbol, quantity)`, calculate the final position for each financial instrument.

If the same symbol appears multiple times, its quantities must be accumulated.

Positions with a final quantity of `0` should be removed.

Finally, return the positions sorted by:

1. **Absolute position size**, from largest to smallest.
2. **Symbol**, in alphabetical order, when two positions have the same absolute size.

### Example

Given the following trades:

```python
trades = [
    ("abc", 100),
    ("def", 200),
    ("ghi", 300),
    ("jkl", 400),
    ("abc", -100)
]
```

The position for `abc` is:

```text
100 + (-100) = 0
```

Therefore, `abc` is removed from the final result.

The expected output is:

```python
[
    ("jkl", 400),
    ("ghi", 300),
    ("def", 200)
]
```

---

## Approach

The solution uses a **dictionary (hash map)** to keep track of the current position of each symbol.

For every trade:

* If the symbol already exists in the dictionary, its quantity is updated.
* Otherwise, the symbol is added with its initial quantity.

After processing all trades, positions with a quantity of `0` are removed using a **dictionary comprehension**.

Finally, the remaining positions are sorted using Python's `sorted()` function.

---

## Algorithm

### 1. Initialize the positions dictionary

```python
positions = {}
```

This dictionary will store:

```text
symbol → accumulated quantity
```

For example:

```python
{
    "abc": 100,
    "def": 200
}
```

### 2. Process each trade

```python
for symbol, quantity in trades:
    if symbol in positions:
        positions[symbol] += quantity
    else:
        positions[symbol] = quantity
```

This accumulates all trades belonging to the same symbol.

### 3. Remove zero positions

```python
positions = {
    symbol: quantity
    for symbol, quantity in positions.items()
    if quantity != 0
}
```

Only positions whose final quantity is different from zero are retained.

### 4. Sort the positions

```python
positions = sorted(
    positions.items(),
    key=lambda item: (-abs(item[1]), item[0])
)
```

The sorting key contains two criteria:

```python
(-abs(item[1]), item[0])
```

The first criterion:

```python
-abs(item[1])
```

sorts positions by absolute quantity in descending order.

The second criterion:

```python
item[0]
```

sorts symbols alphabetically when two positions have the same absolute quantity.

---

## Complexity Analysis

Let:

* `n` = number of trades.
* `m` = number of distinct symbols.

### Time Complexity

Processing the trades requires:

```text
O(n)
```

Removing zero positions requires:

```text
O(m)
```

Sorting the final positions requires:

```text
O(m log m)
```

Therefore, the overall time complexity is:

```text
O(n + m log m)
```

### Space Complexity

The dictionary stores up to `m` distinct symbols:

```text
O(m)
```

Therefore, the space complexity is:

```text
O(m)
```

---

## Implementation

```python
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

    positions = sorted(
        positions.items(),
        key=lambda item: (-abs(item[1]), item[0])
    )

    return positions
```

### Example

```python
trades = [
    ("abc", 100),
    ("def", 200),
    ("ghi", 300),
    ("jkl", 400),
    ("abc", -100)
]

print(calculate_positions(trades))
```

Output:

```python
[
    ("jkl", 400),
    ("ghi", 300),
    ("def", 200)
]
```

---

## Concepts Practiced

* Python dictionaries
* Hash maps
* Iteration over dictionaries
* `dict.items()`
* Dictionary comprehensions
* Tuples
* `sorted()`
* `lambda` functions
* Custom sorting keys
* `abs()`
* Time and space complexity
* Basic financial position aggregation

## Financial Context

A **position** represents the net quantity held in a financial instrument.

For example, buying `100` units and later selling `40` units results in a net position of:

```text
100 - 40 = 60
```

A position of `0` means that the trades have completely offset each other.

This problem introduces a basic operation found in trading systems: **aggregating individual transactions into current net positions**.

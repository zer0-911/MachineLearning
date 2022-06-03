def divide_n_items(n, items):
    """
    Decide how many ways to divide n items.
    """
    # Base case
    if n == 0:
        return 1
    
    # Recursive case
    else:
        return sum(divide_n_items(n - i, items[i:]) for i in range(1, len(items)))

print(divide_n_items(1, [1, 2, 3]))
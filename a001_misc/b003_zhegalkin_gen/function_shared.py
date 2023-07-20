def binary_indices(n):
    indices = []
    count = 0
    while n > 0:
        if n % 2:
            indices.append(count)
        n = n // 2
        count += 1
    return indices

def sum_first_n(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

print(sum_first_n(100))
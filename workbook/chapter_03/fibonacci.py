def fibonacci_iterative(n):
    previous = 0
    current = 1
    for i in range(n - 1):
        current_old = current
        current = previous + current
        previous = current_old
    return current

def fibonacci_recursive(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_iterative(n - 2) + fibonacci_iterative(n - 1)


def fibonacci_list(x):
    lst = []
    for i in range(x + 1):
        if i <= 1:
            lst.append(i)
        else:
            minus_two = lst[i - 2]
            minus_one = lst[i - 1]
            current = minus_two + minus_one
            lst.append(current)

    return lst

print(fibonacci_list(10))
def fibonacci_iterative(n):
    minus_two, current = 0, 0
    minus_one = 1
    for i in range(n - 1):
        current_old = minus_one
        current = minus_two + minus_one
        minus_two = current_old
    return current

def fibonacci_recursive(n):
    if n == 0 or n == 1 or ((n - 2 == 0) and (n - 1 == 1)):
        return n
    else:
        return fibonacci_iterative(n - 2) + fibonacci_iterative(n - 1)


def fibonacci_dynamic(n):
    storage_dict = {}
    result = 0

    for i in reversed(range(n)):
        if (i + 1) in storage_dict:
            print(f'This sequence {str(i + 1)}has been already computed')

    ##todo: complete this task
    return result

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
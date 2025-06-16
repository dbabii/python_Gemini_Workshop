import time
stored_results = {}

def sum_to_num(n):
    start_time = time.perf_counter()
    result = 0
    for i in reversed(range(n)):
        if (i + 1) in stored_results:
            print(f'The result has been computed {str(i + 1)}')
            result += stored_results[i + 1]
            break
        else:
            result += i + 1

    stored_results[n] = result
    print(time.perf_counter() - start_time)
    return result

print(sum_to_num(5))
print(sum_to_num(10))
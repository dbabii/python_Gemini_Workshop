import time
import random

# mark time before running a code
time_before = time.time_ns()
# code
l = [random.randint(1, 999) for _ in range(10 * 3)]
# mark time after running a code
time_after = time.time_ns()
# calculate difference in ns
td = time_after - time_before
print(td)


nums = list(range(1000))
# filter returns the elements when function returns True
filtered = filter(lambda x: x % 3 == 0 or x % 7 == 0, nums)

print(sum(filtered))
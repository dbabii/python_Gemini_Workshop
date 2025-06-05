# List Comprehension: You previously had code to create a list l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and then a loop to print even numbers.
# 1. Create the list l1 with numbers from 1 to 10 using the range() function and list().
# 2. Using a list comprehension, create a new list even_numbers containing only the even numbers from l1. Print even_numbers.

l1 = []
for i in range(1,11):
    l1.append(i)

print(l1)

l2 = list(range(1,11))
print(l2)

l3 = [i for i in range(1,11)]

even_num = [i for i in l1 if i % 2 == 0]
print(even_num)
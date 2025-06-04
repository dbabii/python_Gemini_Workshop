## Ex. 29. Using zip() method ot manipulate dictionaries
# items = ['apple', 'orange', 'banana']
# quantity = [5, 3, 2]
#
# orders = zip(items, quantity)
# print(orders)
# # print(list(orders))
# # print(tuple(orders))
# print(dict(orders))

## Ex. 30. Accessing a dictionary using dictionary methods
# orders = {'apple': 5, 'orange': 3, 'banana': 2}
# print(orders.values())
# print(list(orders.values()))
# print(list(orders.keys()))
#
# for tuple in list(orders.items()):
#     print(tuple)

## Ex. 31. Exploring Tuple Properties in Our shopping list
# t = ('bread', 'milk', 'eggs')
# print(len(t))
#
# # t.append('apple') #AttributeError: 'tuple' object has no attribute 'append'
# # t[2] = 'apple' # TypeError: 'tuple' object does not support item assignment
#
# print(t + ('apple', 'orange'))
# print(t)
#
# t_mix = 'apple', True, 3
# print(t_mix)
#
# t_shopping = ('apple', 3), ('orange', 2), ('banana', 5)
# print(t_shopping)

## Ex. 32. Using Sets
# s1 = set([1,2,3,4,5,6])
# print(s1)
# s2 = set([1,2,2,3,4,4,5,6,6])
# print(s2)
# s3 = set([3,4,5,6,6,6,1,1,2])
# print(s3)
# s4 = {"apple", "orange", "banana"}
# print(s4)
# s4.add('pineapple')
# print(s4)

## Ex. 33. Implementing Set ops
s5 = {1,2,3,4}
s6 = {3,4,5,6}
#union
print(s5 | s6)
print(s5.union(s6))
#intersection
print(s5 & s6)
print(s5.intersection(s6))
#difference
print(s5 - s6)
print(s5.difference(s6))
#is sub-sets
print(s5 <= s6)
print(s5.issubset(s6))

#-----#
s7 = {1,2,3}
s8 = {1,2,3,4,5}
print(s7 <= s8)
print(s7.issubset(s8))

print(s7 < s8)
s9 = {1,2,3}
s10 = {1,2,3}
print(s9 < s10)
print(s9 <= s7)
#upperset
print(s8 >= s7)
print(s8.issuperset(s7))
print(s8 > s7)
print(s8 > s8)

print(s7 == s9)
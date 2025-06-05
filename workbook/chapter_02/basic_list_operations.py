# shopping = ["bread", "milk", "eggs"]
# print(len(shopping))
#
# list1 = [1,2,3]
# list2 = [4,5,6]
# final_list = list1 + list2
# print(final_list)
#
# list3 = ["oi"]
# print(list2*3)
#
# print(shopping)
# shopping[1] = "banana"
# print(shopping)
# print(shopping[-1])
# print(shopping[0:2])
# print(shopping[:3])
# print(shopping[1:])
# shopping.append("apple")
# print(shopping)

## Ex. 27
# shopping = []
# shopping.append("bread")
# shopping.append("milk")
# shopping.append("eggs")
# shopping.append("apple")
# print(shopping)
#
# shopping.insert(2, "ham")
# print(shopping)

## Ex. 28
movie = {
    "title": "The Godfather",
    "director": "Francis Ford Coppola",
    "year": 1972,
    "rating": 9.2
}
print(movie['year'])
movie['rating'] = (movie['rating'] + 9.3) / 2
print(movie['rating'])

movie["actors"] = ["Marlon Brando", "Al Pacino", "James Caan"]
movie["other details"] = {
    "runtime": 175,
    "language": "English"
}

for i in movie:
    print(f"{i}: {movie[i]}")
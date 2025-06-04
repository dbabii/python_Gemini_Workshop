# Processing a List of Strings: Write a function normalize_strings(string_list) that takes a list of strings. The function should return a new list where each string is:
#
#     Converted to lowercase.
#     Stripped of leading and trailing whitespace.
#     Example: normalize_strings([" Hello WORLD ", " Python "]) should return ['hello world', 'python'].

def normalize_strings(string_list):
    for el in string_list:
        print(el.lower())
        el.strip()

    print(string_list)
    return string_list

l1 = [" JoSkasO Kiosala", " KKKKK", "LLLL "]
l2 = []
for i in l1:
    i = i.lower()
    i = i.strip()


print(l1)
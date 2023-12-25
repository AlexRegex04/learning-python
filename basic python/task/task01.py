x = 'mom'
# # x = str(input('enter number'))

# # Method 01
# # 1881

# tmp = ''

# # # string, tuple, list, dictionary, set, frozenset

# i = len(x) - 1
# while (i >= 0):
#     tmp += x[i]  # tmp = tmp + x[i]
#     i -= 1  # i = i - 1
# if (x == tmp):
#     print(f'{x} is palindrome number')
# else:
#     print(f"{x} is not palindrome number")


# # Method 02
# string = "MOM"

# tmp = [*string]
# tmp.reverse()
# newStr = ''.join(tmp)
# if (string == newStr):
#     print(f'{string} is palindrome number')
# else:
#     print(f"{string} is not palindrome number")


# lst = []
# for letter in string:
#     lst.append(letter)

# letter = [x for x in string]

# print(list(string))

# lst = []
# lst.extend(string)
# print(lst)

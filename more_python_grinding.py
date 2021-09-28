# def freind(X):
#     new_list = []
#     for freind in x:
#         if len(freind) == 4:
#             new_list.append(freind)
#     return new_list
#
#
# def friend(x):
#     return [f for f in x if len(f) == 4]


# def binary_array_to_number(arr):
#   return int("".join(map(str, arr)), 2)
# To convert integer to binary, start with the integer in question and divide it by 2 keeping notice of the quotient
# and the remainder


# def add_binary(a, b):
#     return bin(a + b).replace('0b', '')
#
#
# def add_binary(a, b):
#     return "{0:b}".format(int(a + b))

#
# def infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1


# gen = infinite_sequence()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# for i in infinite_sequence():
#     print(i, end=" ")

# def is_palindrome(num):
#     # Skip single-digit inputs
#     if num // 10 == 0:
#         return False
#     temp = num
#     reversed_num = 0
#
#     while temp != 0:
#         reversed_num = (reversed_num * 10) + (temp % 10)
#         temp = temp // 10
#
#     if num == reversed_num:
#         return num
#     else:
#         return False
# #

#
#
# for i in infinite_sequence():
#     pal = is_palindrome(i)
#     if pal:
#         print(i)
# nums_squared_lc = [num**2 for num in range(5)]
# nums_squared_gc = (num**2 for num in range(5))
# print(next(nums_squared_gc))
# print(nums_squared_
# letters = ["a", "b", "c", "y"]
# it = iter(letters)
# while True:
#     try:
#         letter = next(it)
#     except StopIteration:
#         break
#     print(letter)

# def infinite_palindromes():
#     num = 0
#     while True:
#         if is_palindrome(num):
#             i = (yield num)
#             if i is not None:
#                 num = i
#         num += 1
#
#
#
# pal_gen = infinite_palindromes()
# for i in pal_gen:
#     digits = len(str(i))
#     pal_gen.send(10 ** digits)
# pal_gen = infinite_palindromes()
# for i in pal_gen:
#     print(i)
#     digits = len(str(i))
#     if digits == 5:
#         pal_gen.throw(ValueError("We don't like large palindromes"))
#     pal_gen.send(10 ** (digits))


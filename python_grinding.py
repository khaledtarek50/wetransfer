# def get_middle(s):
#     str_len = len(s)
#     if str_len % 2 > 0:
#         return s[str_len / 2]
#     if str_len % 2 == 0:
#         return s[(str_len / 2 - 1): (str_len / 2 + 1)]
#     else:

# def middle_char(txt):
#     return txt[(len(txt) - 1) // 2:(len(txt) + 2) // 2]
#
#
# print(middle_char('testing'))

#
# def is_isogram(string):
#     string.lower()
#     for i in range(len(string)):
#
#         if string.count(string[i]) == 1:
#             return True
#         elif string == "":
#             return True
#         elif string.count(string[i]) > 1:
#             return False


# def is_isogram(string):
#     string = string.lower()
#     if len(string) == 0:
#         return True
#     for i in range(len(string)):
#         if string.count(string[i]) > 1:
#             return False
#     return True
#
#
# print(is_isogram(""))
# print(is_isogram('Dermatoglyphics'))
# print(is_isogram('aba'))
# print(is_isogram('moOse'))


# import math
#
#
# def is_square(n):
#     if n < 0:
#         return False
#     elif n == math.sqrt(n) ** 2:
#         return True
#     return False
#
#
# print(is_square(-1))

# import math
#
# def is_square(n):
#     #for n in range(0,n):
#     if n < 0:
#         return False
#     elif n == 0:
#         return True
#     elif n == 1:
#         return True
#     elif n%math.sqrt(n) == 0:
#         return True
#     elif n%math.sqrt(n) != 0:
#         return False
#
# return n

# def to_jaden_case(string):
#     new_list = []
#     words = string.split()
#     for word in words:
#         new_list.append(word.capitalize())
#     return ' '.join(new_list)
#
# print(to_jaden_case("Most Trees Are Blue How Can Mirrors Be Real If Our Eyes Aren't Real All The Rules In This World Were Made By Someone No Smarter Than You. So Make Your Own." should equal 'All The Rules In This World Were Made By Someone No Smarter Than You. So Make Your Own.'))

# def find_short(s):
#     items = s.split()
#     l = min(len(ele) for ele in items)
#     return l

# find_short("bitcoin take over the world maybe who knows perhaps")


# def xo(s):
#     s = s.lower()
#     if s.count('o') and s.count('x') == 0:
#         return True
#     elif s.count('o') == s.count('x'):
#         return True
#     return False

#
# def filter_list(l):
#     """return a new list with the strings filtered out"""
#     return [n for n in l if isinstance(n, int)]


# def get_sum(a, b):
#     min(a, b)
#     max(a, b)
#     return (max(a, b) - min(a, b) + 1) * (min(a, b) + max(a, b)) / 2
# # def get_sum(a, b):
# #     return sum(xrange(min(a, b), max(a, b) + 1))
#
# print(get_sum(3, 6))
# print(get_sum(1, 2))
# print(get_sum(0, 1))
# print(get_sum(1, 1))
# print(get_sum(-1, 0))
# print(get_sum(-1, 2))


# def get_sum(a,b):
#     if a == b:
#         return a
#     s = 0
#     for n in xrange(min(a,b), max(a,b)+1):
#         s += n
#     return s


# def maskify(cc):
#     hidden_part = cc[:-4]
#     if cc == '':
#         return cc
#     return cc.replace(hidden_part,'#' * len(hidden_part))


# def sum_two_smallest_numbers(numbers):
#     numbers.sort()
#     mini = min(numbers)
#     second_min = numbers[1]
#     return mini + second_min

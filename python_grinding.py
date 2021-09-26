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

# def sum_two_smallest_numbers(numbers):
#     first_min = min(numbers)
#     numbers.remove(first_min)
#     second_min = min(numbers)
#     return first_min + second_min

#  learning lambda functions
# def double(n):
#     return n * 2


# double = lambda n: n * 2
# larger = lambda a, b: a if a > b else b
# return a if a > b else return b
# names = ['alan', 'gregory', 'zlatan', 'jonas', 'tom', 'augustine']
# names.sort(key=lambda x: len(x))
# print(names)

# using for loop and append()
# numbers = [1, 2, 3, 4, 5]
# squared_nums = []
# square = lambda n: n ** 2
# for num in numbers:
#     squared_nums.append(square(num))
# print(squared_nums)

# using map() and lambda(functions)

# numbers = [1, 2, 3, 4, 5]
# squared_nums = list(map(lambda n: n ** 2, numbers))
# print(squared_nums)

# def longest(a1, a2):
#     return ''.join(sorted(dict.fromkeys(a1 + a2)))
#      return ''.join(sorted(set(a1 + a2)))
# print(longest("loopingisfunbutdangerous", "lessdangerousthancoding"))

# my solution
# def validate_pin(pin):
#     if pin.isdecimal():
#         if len(pin) == 4:
#             return True
#         elif len(pin) == 6:
#             return True
#         return False
#     return False
# another solution
# def validate_pin(pin):
#     return len(pin) in (4, 6) and pin.isdigit()


# print(validate_pin("1"))
# print(validate_pin("12"))
# print(validate_pin("12345"))
# print(validate_pin("1234567"))
# print(validate_pin("-1234"))
# print(validate_pin("-12345"))
# print(validate_pin("1.234"))
# print(validate_pin("00000000"))
# mine
# def printer_error(s):
#     alphabet_list = 'abcdefghijklm'
#     letters = []
#     for letter in s:
#         if letter not in alphabet_list:
#             letters.append(letter)
#     return f'{len(letters)}/{len(s)}'

# not mine
# def printer_error(s):
#     return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))

# mine but failed cus i put the return elsewhere
# def printer_error(s):
#     good_colors = "abcdefghijklm"
#     counter = 0
#     for i in s:
#         if i not in good_colors:
#             counter += 1
#     return str(counter) + "/" + str(len(s))
# print(printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))
# print(printer_error("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))
# print(printer_error("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"))

# import  math
# def find_next_square(sq):
#     root = math.sqrt(sq)
#     if int(root + 0.5) ** 2 == sq:
#         root += 1
#         return pow(root,2)
#     return -1


# def open_or_senior(data):
#
#     for info in data:
#         print(data)
#         age, handicap = info
#         if age >= 55 and handicap > 7:
#             return 'Senior'
#         return 'Open'
# def open_or_senior(data):
#     new_list = []
#     for info in data:
#         age, handicap = info
#         if age >= 55 and handicap > 7:
#             new_list.append('Senior')
#         else:
#             new_list.append('Open')
#     return new_list


# def openOrSenior(data):
#     return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]

# def open_or_senior(data):
#     return list(map(lambda d: 'Senior' if d[0] >= 55 and d[1] > 7 else 'Open', data))

#
# print(open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)]))
# print(open_or_senior([(16, 23), (73, 1), (56, 20), (1, -1)]))

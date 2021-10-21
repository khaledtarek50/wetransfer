# def decodeMorse(morse_code):
#     answer = []
#     split = morse_code.split('   ')
#     for i in split:
#         for letter in i.split():
#             answer.append(MORSE_CODE[letter])
#         answer.append(' ')
#     print(answer)
#     return ''.join(answer).strip()

# def find_even_index(arr):
#     r = sum(arr)
#     l = 0
#     for i, x in enumerate(arr):
#         r -= x
#         if r == l:
#             return i
#         l += x
#     return -1

# def find_even_index(arr):
#     for i in range(len(arr)):
#         if sum(arr[:i]) == sum(arr[i+1:]):
#             return i
#     return -1


# def iq_test(numbers):
#     odd = []
#     even = []
#     listing = list(map(int, numbers.split()))
#     for i, num in enumerate(listing):
#         if num % 2 == 1:
#             odd.append(i + 1)
#         if num % 2 == 0:
#             even.append(i + 1)
#     if len(odd) < len(even):
#         return odd[0]
#     return even[0]


# import itertools


# def unique_in_order(iterable):
#     return [k for k, _ in itertools.groupby(iterable)]
# def unique_in_order(iterable):
#     result = [None]
#     for item in iterable:
#         if item != result[-1]:
#             result.append(item)
#
#     return result[1:]
# print(unique_in_order('AAAABBBCCDAABBB'))

# def song_decoder(song):
#     mystring = song.replace('WUB', ' ')
#     return ' '.join(mystring.split())
#
#
# song_decoder("AWUBBWUBC")
# song_decoder("AWUBWUBWUBBWUBWUBWUBC")
# song_decoder("WUBAWUBBWUBCWUB")
#
#
# def is_valid_walk(walk):
#     if 'n' in walk:
#         if len(walk) == 10 and walk.count('n') != walk.count('s'):
#             return True
#     if 'w' in walk:
#         if len(walk) == 10 and walk.count('w') != walk.count('e'):
#             return True
#         return False
#
#
# def is_valid_walk(walk):
#     if len(walk) == 10 and walk.count('n') != walk.count('s') or walk.count('w') != walk.count('e'):
#         return True
#     return False
#
#
# def to_camel_case(text):
#     final_result = []
#     if '_' or '-' in text:
#         underscore = text.replace('_', '-')
#         sentence = underscore.split('-')
#         if text != '':
#             final_result.append(sentence[0])
#         the_rest = underscore.title()
#         final_result.append(the_rest[len(sentence[0]):].title())
#         grouping = ''.join(final_result)
#         split = grouping.split('-')
#         last_touch = ''.join(split)
#         return last_touch
#
# def to_camel_case(text):
#     return text[:1] + text.title()[1:].replace('_', '').replace('-', '')
#
# to_camel_case('')
# to_camel_case("the_stealth_warrior")
# to_camel_case("The-Stealth-Warrior")
# to_camel_case("A-B-C")

# # def likes(names):
# #     if len(names) == 0:
# #         return 'no one likes this'
# #     elif len(names) == 1:
# #         return f'{names[0]} likes this'
# #     elif len(names) == 2:
# #         return f'{names[0]} and {names[1]} like this'
# #     elif len(names) == 3:
# #         return f'{names[0]}, {names[1]} and {names[2]} like this'
# #     elif len(names) >= 4:
# #         return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'
# #
# #
# # print(likes([]))
# # print(likes(['Peter']))
# # print(likes(['Jacob', 'Alex']))
# # print(likes(['Max', 'John', 'Mark']))
# # print(likes(['Alex', 'Jacob', 'Mark', 'Max']))
#
#
# # def duplicate_count(text):
# #     Text = text.lower()
# #     sett = set()
# #     for letter in Text:
# #         if Text.count(letter) > 1:
# #             sett.add(letter)
# #     return len(sett)
# #
# #
# # print(duplicate_count(""))
# # print(duplicate_count("abcde"))
# # print(duplicate_count("abcdeaa"))
# # print(duplicate_count("abcdeaB"))
# # print(duplicate_count("Indivisibilities"))
#
#
# # def spin_words(sentence):
# #     new_list = []
# #     for word in sentence.split(' '):
# #         if len(word) > 5:
# #             print(word[::-1])
# #             new_list.append(word)
# #         elif word not in new_list:
# #             print(word)
# #
# #
# # spin_words(
# #     'the a more a like of present a than like of consist present one but in the the letter of be of that reversed')
# # spin_words('to')
# # def persistence(n):
# #     str(n)
# #     print(n)
# # persistence(999)
#
# # def add(a, b):
# #     result = a + b
# #     return result
# #
# #
# # add(2, 2)
# #
# #
# # def add(a, b):
# #     result = a + b
# #     return result
# #
# #
# # print(add(2, 2))
# #
# # import statistics as st
# #
# #
# # def describe(sample):
# #     return st.mean(sample), st.median(sample), st.mode(sample)
# #
# #
# # sample = [10, 2, 4, 7, 9, 3, 9, 8, 6, 7]
# # mean, median, mode = describe(sample)
# #
# # print(mean)
# #
# # print(median)
# #
# # print(mode)
# #
# # desc = describe(sample)
# # print(desc)
# #
# # type(desc)
#
# # def spin_words(sentence):
# #     last_result = []
# #     split_sentence = sentence.split()
# #     for word in split_sentence:
# #         if len(word) >= 5:
# #             last_result.append(word[::-1])
# #         else:
# #             last_result.append(word)
# #     last = ' '.join(last_result)
# #     return last
# #     #         last_result.append(word)
# #     #     last = ' '.join(last_result)
# #     # return last
# #
# #
# # print(spin_words("Hey fellow warriors"))
# # print(spin_words("This is a test"))
# # print(spin_words("This is another test"))
# # def spin_words(sentence):
# #     # Your code goes here
# #     return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
#
# # def persistence(n):
# #     str1 = str(n)
# #     # initializing substring
# #     A = 1
# #     # create a result list
# #     result = []
# #     for i in range(0, len(str1), A):
# #         # convert to int, after the slicing process
# #         result.append(int(str1[i: i + A]))
# #         answer = 1
# #     while n > 9:
# #         for n in result:
# #             answer = answer * n
# #
# #         return answer
# #     return 0
# #
# #
# # print(persistence(39))
# # print(persistence(4))
# # print(persistence(25))
# # print(persistence(999))
# # def get_All():
# #     a = ['foo', 'bar', 'baz']
# #     for i in a:
# #         print(i)
# # get_All()
#
#
# # def persistence(n):
# #     counter = 0
# #     string = str(n)
# #     if len(string) > 1:
# #         numbers = map(int, list(string))
# #         multip_result = 1
# #         for num in numbers:
# #             multip_result = multip_result * num
# #
# #         counter += persistence(multip_result) + 1
# #     return counter
# # def persistence(n):
# #     n = str(n)
# #     count = 0
# #     while len(n) > 1:
# #         p = 1
# #         for i in n:
# #             p *= int(i)
# #         n = str(p)
# #         count += 1
# #     return count
#
#
# # print(persistence(39))
#
#
# # def array_diff(a, b):
# #     answer = []
# #     for item in a:
# #         if item not in b:
# #             answer.append(item)
# #     return answer
# # array_diff([1,2], [1])
# # array_diff([1,2,2], [1])
# # array_diff([1,2,2], [2])
# # array_diff([1,2,2], [])
# # array_diff([], [1,2]), [], "a was [], b was [1,2], expected []")
# # array_diff([1,2,3], [1]
#
# # def duplicate_encode(word):
# #     listing = []
# #     word = word.lower()
# #     for i in word:
# #         if word.count(i) >= 2:
# #             listing.append(i.replace(i, ')'))
# #         else:
# #             listing.append(i.replace(i, '('))
# #     joining = ''.join(listing)
# #     return joining
# #
# #
# # duplicate_encode("recede")
# # duplicate_encode("Success")
# # duplicate_encode("(( @")
#
#


# def create_phone_number(n):
#     s = [str(i) for i in n]
#     res = "".join(s)
#     part_1 = res[0:3]
#     part_2 = res[3:6]
#     part_3 = res[6:10]
#     first_part = '(' + part_1 + ')'
#     final_part = f' {part_2}-{part_3}'
#     return first_part + final_part


# def create_phone_number(n):
# return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
#
# create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
# create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0])
# create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# def find_outlier(integers):
#     even_list = []
#     odd_list = []
#     for num in integers:
#         if num % 2 == 0:
#             even_list.append(num)
#         if num % 2 == 1:
#             odd_list.append(num)
#     if len(odd_list) == 1:
#        return odd_list.pop(0)
#     if len(even_list) == 1:
#         return even_list.pop(0)
#
#
def find_outlier(int):
    odds = [x for x in int if x % 2 != 0]
    evens = [x for x in int if x % 2 == 0]
    return odds[0] if len(odds) < len(evens) else evens[0]


# x = find_outlier([2, 4, 6, 8, 10, 3])
# print(x)


# def alphabet_position(text):
#     new_list = []
#     dict = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17','r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'}
#     new_text = text.lower()
#     for i in new_text:
#         if i in dict:
#             new_list.append(dict[i])
#             new_text = new_text.replace(i, dict[i])
#     return ' '.join(new_list)
#
# def alphabet_position(text):
#     return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

# alphabet_position("The sunset sets at twelve o' clock.")
# alphabet_position("The narwhal bacons at midnight.")

#
# def order(sentence):
#     words = sentence.split()
#     myre = re.compile(r'\d+')
#     words.sort(key=lambda x: myre.findall(x))
#     print(' '.join(words))
#

# def order(words):
#     return ' '.join(sorted(words.split(), key=lambda w: sorted(w)))


# order("is2 Thi1s T4est 3a")
# order("4of Fo1r pe6ople g3ood th5e the2")
# order("")

# def tribonacci(signature, n):
#     n1, n2, n3 = signature
#     if n == 0:
#         return []
#     else:
#         for i in range(n):
#             trying = tribonacci(n1 - 1, n) + tribonacci(n2 - 2, n) + tribonacci(n3 - 3, n)
#             return trying


# tribonacci([1, 1, 1], 10)
#
# def count_bits(n):
#     return bin(n).count('1')

# Stack implementation in python


# Creating a stack
def create_stack():
    stack = []
    return stack


# Creating an empty stack
def check_empty(stack):
    return len(stack) == 0


# Adding items into the stack push
def push(stack, item):
    stack.append(item)
    print(f'you added {item}')


# Removing an element from the stack pop
def pop(stack):
    if check_empty(stack):
        return None
    return f'{stack.pop()} the list now is {len(stack)} items'


stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print(check_empty(stack))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))


# Queue implementation in Python

class Queue:
    # creates the queue
    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)
        print(f'you added {item}')

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop()

    # Display  the queue
    def display_queue(self):
        print(self.queue)

    # gets the size of the queue
    def queue_size(self):
        return len(self.queue)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display_queue()

q.dequeue()
q.dequeue()
q.dequeue()
q.enqueue(6)
q.enqueue(3)
q.enqueue(6)
q.enqueue(3)
q.enqueue(6)
q.enqueue(3)
q.enqueue(6)
q.enqueue(4)

print("After removing an element")
q.display_queue()
print(q.queue_size())

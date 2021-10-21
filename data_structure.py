# Creating a stack
# def create_stack():
#     stack = []
#     return stack
#
#
# # Creating an empty stack
# def check_empty(stack):
#     return len(stack) == 0
#
#
# # Adding items into the stack push
# def push(stack, item):
#     stack.append(item)
#     print(f'you added {item}')
#
#
# # Removing an element from the stack pop
# def pop(stack):
#     if check_empty(stack):
#         return None
#     return f'{stack.pop()} the list now is {len(stack)} items'
#
#
# stack = create_stack()
# push(stack, str(1))
# push(stack, str(2))
# push(stack, str(3))
# push(stack, str(4))
# print(check_empty(stack))
# print("popped item: " + pop(stack))
# print("stack after popping an element: " + str(stack))
#

# # Queue implementation in Python

# class Queue:
#     # creates the queue
#     def __init__(self):
#         self.queue = []
#
#     # Add an element
#     def enqueue(self, item):
#         self.queue.append(item)
#         print(f'you added {item}')
#
#     # Remove an element
#     def dequeue(self):
#         if len(self.queue) < 1:
#             return None
#         print(f'you removed {self.queue[0]}')
#         return self.queue.pop(0)
#
#     # Display  the queue
#     def display_queue(self):
#         print(self.queue)
#
#     # gets the size of the queue
#     def queue_len(self):
#         return len(self.queue)
# #
# #
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.enqueue(5)
#
# q.display_queue()
#
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.enqueue(6)
# q.enqueue(3)
# q.enqueue(6)
# q.enqueue(3)
# q.enqueue(6)
# q.enqueue(3)
# q.enqueue(6)
# q.enqueue(4)
#
# print("After removing an element")
# q.display_queue()
# print(q.queue_len())
# q.enqueue(6)
# q.enqueue(3)
# q.enqueue(6)
# q.enqueue(3)
# q.enqueue(6)
# q.enqueue(3)
# q.enqueue(6)
# q.enqueue(4)
# q.display_queue()
# q.enqueue(6)
# q.enqueue(3)
# q.enqueue(6)
# q.enqueue(3)
# q.enqueue(6)
# q.enqueue(3)
# q.enqueue(6)
# q.enqueue(4)
# q.display_queue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.display_queue()


# Circular Queue implementation in Python


# Circular Queue implementation in Python


# class MyCircularQueue:
#
#     def __init__(self, k):
#         self.k = k
#         self.queue = [None] * k
#         self.head = self.tail = -1
#
#     # Insert an element into the circular queue
#     def enqueue(self, data):
#
#         if (self.tail + 1) % self.k == self.head:
#             print("The circular queue is full\n")
#
#         elif self.head == -1:
#             self.head = 0
#             self.tail = 0
#             self.queue[self.tail] = data
#         else:
#             self.tail = (self.tail + 1) % self.k
#             self.queue[self.tail] = data
#
#     # Delete an element from the circular queue
#     def dequeue(self):
#         if self.head == -1:
#             print("The circular queue is empty\n")
#
#         elif self.head == self.tail:
#             temp = self.queue[self.head]
#             self.head = -1
#             self.tail = -1
#             return temp
#         else:
#             temp = self.queue[self.head]
#             self.head = (self.head + 1) % self.k
#             return temp
#
# def printCQueue(self):
#     if self.head == -1:
#         print("No element in the circular queue")
#
#     elif self.tail >= self.head:
#         for i in range(self.head, self.tail + 1):
#             print(self.queue[i], end=" ")
#         print()
#     else:
#         for i in range(self.head, self.k):
#             print(self.queue[i], end=" ")
#         for i in range(0, self.tail + 1):
#             print(self.queue[i], end=" ")
#         print()

# class MyCircularQueue:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.queue = [None] * capacity
#         self.tail = -1
#         self.head = 0
#         self.size = 0
#
#     def enqueue(self, data):
#         if self.size == self.capacity:
#             print('queue is full!')
#         self.tail = (self.tail + 1) % self.capacity
#         self.queue[self.tail] = data
#         self.size = self.size + 1
#
#     def dequeue(self):
#         if self.size == 0:
#             print('queue is empty')
#             return
#         else:
#             temp = self.queue[self.head]
#             self.head = (self.head + 1) % self.capacity
#         self.size = self.size - 1
#         return temp
#
#     def display(self):
#         if self.size == 0:
#             print('queue is empty! \n')
#         elif self.tail >= self.head:
#             for i in range(self.head, self.tail + 1):
#                 print(self.queue[i], end=" ")
#             print()
#         else:
#             for i in range(self.head, self.capacity):
#                 print(self.queue[i], end=" ")
#             for i in range(0, self.tail + 1):
#                 print(self.queue[i], end=" ")
#             print()
#         # else:
#             # index = self.head
#             # for i in range(self.size):
#             #     print(self.queue[index], end=" ")
#             #     # print()
#             #     index = (index + 1) % self.capacity
#
#
# q = MyCircularQueue(5)
# q.enqueue(5)
# q.enqueue(2)
# q.enqueue(10)
# q.enqueue(4)
# q.enqueue(5)
# q.display()
# q.dequeue()
# q.dequeue()
# q.display()
# q.enqueue(6)
# q.enqueue(8)
# q.display()
# q.dequeue()
# q.dequeue()
# q.display()
# q.enqueue(10)
# q.enqueue(16)
# q.display()


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(5)
# obj.enqueue(1)
# obj.enqueue(2)
# obj.enqueue(3)
# obj.enqueue(4)
# obj.enqueue(5)
# print("Initial queue")
# obj.printCQueue()
#
# obj.dequeue()
# print("After removing an element from the queue")
# obj.printCQueue()
# obj.enqueue(10)
# obj.printCQueue()
# obj.dequeue()
# obj.dequeue()
# obj.printCQueue()
# obj.enqueue(2)
# obj.enqueue(4)
# obj.printCQueue()
# obj.dequeue()
# obj.dequeue()
# obj.printCQueue()
# obj.enqueue(6)
# obj.enqueue(8)
# obj.printCQueue()


# Heap Sort in python


# def heapify(arr, length, i):
#     # Find largest among root and children
#     largest = i
#     left = 2 * i + 1
#     right = 2 * i + 2
#
#     if left < length and arr[i] < arr[left]:
#         largest = left
#
#     if right < length and arr[largest] < arr[right]:
#         largest = right
#
#     # If root is not largest, swap with largest and continue heapifying
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         heapify(arr, length, largest)
#
#
# def heap_sort(arr):
#     length = len(arr)
#
#     # Build max heap
#     for i in range(length // 2, -1, -1):
#         heapify(arr, length, i)
#
#     for i in range(length - 1, 0, -1):
#         # Swap
#         arr[i], arr[0] = arr[0], arr[i]
#
#         # Heapify root element
#         heapify(arr, i, 0)

#
# arr = [1, 12, 9, 5, 6, 10]
# heap_sort(arr)
# length = len(arr)
# print("Sorted array is")
# for i in range(length):
#     print(arr[i], end=' ')


# Priority queue
# function to heapify the tree
# Find the largest among root, left child and right child
# def heapify(arr, length, i):  # i == root
#     largest = i
#     left = 2 * i + 1
#     right = 2 * i + 2
#
#     if left < length and arr[i] < arr[left]:
#         largest = left
#     if right < length and arr[largest] < arr[right]:
#         largest = right
#
#     # Swap and continue heapifying if root is not largest
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         heapify(arr, length, largest)
#
#
# def insert(array, new_num):
#     size = len(array)
#     if size == 0:
#         array.append(new_num)
#     else:
#         array.append(new_num)
#         for i in range((size // 2) - 1, -1, -1):
#             heapify(array, size, i)
#
#
# def delete_node(array, num):
#     size = len(array)
#     i = 0
#     for i in range(0, size):
#         if num == array[i]:
#             break
#     array[i], array[size - 1] = array[size - 1], array[i]
#     array.remove(size - 1)
#
#     for i in range((len(array) // 2) - 1, -1, -1):
#         heapify(array, len(array), i)
#
#
# arr = []
#
# insert(arr, 3)
# insert(arr, 4)
# insert(arr, 9)
# insert(arr, 5)
# insert(arr, 2)
#
# print("Max-Heap array: " + str(arr))
#
# delete_node(arr, 4)
# print("After deleting an element: " + str(arr))
# print(arr)


# Deque implementation in python

class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        self.items.pop(0)

    def remove_rear(self):
        self.items.pop()

    def display(self):
        print(self.items)


#
# d = Deque()
# print(d.is_empty())
# d.add_rear(8)
# d.add_rear(5)
# d.add_front(7)
# d.add_front(10)
# print(d.size())
# print(d.is_empty())
# d.display()
# d.add_rear(11)
# d.remove_rear()
# d.remove_front()
# d.add_front(55)
# d.add_rear(45)
# d.display()


# Linked list implementation in Python

class Node:
    # creating a node(item)
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, new_data):
        # 1 & 2: Allocate the Node &
        #        Put in the data
        new_node = Node(new_data)
        # 3. Make next of new Node as head
        new_node.next = self.head
        # 4. Move the head to point to new Node
        self.head = new_node

    #  insert_after_a_node
    def insert_after(self, prev_node, new_data):
        # 1. check if the given prev_node exists
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return
        # 2. Create new node &
        # 3. Put in the data
        new_node = Node(new_data)
        # 4. Make next of new Node as next of prev_node
        new_node.next = prev_node.next
        # 5. make next of prev_node as new_node
        prev_node.next = new_node

    def append(self, new_data):
        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)
        # 4. If the Linked List is empty, then make the
        #    new node as head
        if self.head is None:
            self.head = new_node
            return
        # 5. Else traverse till the last node
        last = self.head
        while last.next:
            last = last.next
        # 6. Change the next of last node
        last.next = new_node

    def delete_node(self, key):

        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if temp is None:
            return

        # Unlink the node from linked list
        prev.next = temp.next

        temp = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False


linked_list = LinkedList()
# Assign item values

# linked_list.insert_after(linked_list.head, 6)
linked_list.append(1)
linked_list.insert_at_beginning(2)
linked_list.insert_at_beginning(3)
linked_list.append(6)
linked_list.insert_after(linked_list.head.next, 5)

print('linked list:')
linked_list.print_list()
linked_list.insert_at_beginning(1)
linked_list.insert_after(linked_list.head.next, 10)
linked_list.append(9)
print("\nAfter adding  an element:")
linked_list.delete_node(5)
linked_list.print_list()
item_to_find = 3
if linked_list.search(item_to_find):
    print(str(item_to_find) + " is found")
else:
    print(str(item_to_find) + " is not found")

# llist.sortLinkedList(llist.head)
# print("Sorted List: ")
# llist.printList()
# Connect nodes


# Print the linked list item
# while linked_list.head != None:
#     print(linked_list.head.item, end=" ")
#     linked_list.head = linked_list.head.next

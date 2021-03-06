class Node:
    def __init__(self, data):
        '''создание элемента списка'''
        self.data = data
        self.next = None
        
class SingleLinkedList:
    def __init__(self):
        '''создание списка'''
        self.head = None
        self.tail = None

    def push(self, data):
        '''добавление элемента в начало списка'''
        node = Node(data)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node

    def append(self, data):
        '''добавление элемента в конец списка'''
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def reverse(self):
        '''разворот списка'''
        prev = None
        curr = self.head
        self.tail = curr
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def print(self):
        '''вывод всех элементов списка'''
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

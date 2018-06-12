# Importing the class defined in Node.py
from DS_LinkedList.Node import Node

# Creating a new class for LL
class LinkedList(object):
    # Constructor
    def __init__(self):
        self.head = None
        self.counter = 0

    # Function to traverse the list. O(n)
    def traverseList(self):
        actualNode = self.head
        while actualNode is not None:
            print(actualNode.data)
            actualNode = actualNode.nextNode

    # Function to insert at start. O(1)
    def insertStart(self, data):

        self.counter += 1

        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    # Function to return the size of the list. O(1)
    def size(self):
        return self.counter

    # Function to insert at the end. O(n)
    def insertEnd(self, data):
        if self.head is None:
            self.insertStart(data)
            return

        self.counter += 1

        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    # Function to remove a node. O(n)
    def remove(self, data):
        self.counter -= 1
        if self.head:
            if data == self.head.data:
                self.head = self.head.nextNode
            else:
                self.head.remove(data, self.head)

# Defining the class Node
class Node(object):

    # Construction for class Node
    def __init__(self, data):
        self.data = data

        # defining both the child nodes as NULL for the head node
        self.leftChild = None
        self.rightChild = None

    # Defining the insert function.
    # 'data' contains the new value to be inserted within the tree.
    # 'self' designates the node which is calling this function
    def insert(self, data):
        # If the new data value is less than calling node's data the new value has to go to left branch of the tree
        if data < self.data:
            if not self.leftChild:  # if there are no nodes on the left
                self.leftChild = Node(data)  # assign the new node as the left child
            else:  # if there are nodes on the left
                self.leftChild.insert(data)  # call the insert function again with the immediate left child node
        # If the new data value is greater than calling node's data the new value has to go to right branch of the tree
        else:
            if not self.rightChild:  # if there are no nodes on the right
                self.rightChild = Node(data)  # assign the new node as the right child
            else:  # if there are nodes on the right
                self.rightChild.insert(data)  # call the insert function again with the immediate right child node

    # Defining the remove function
    # Parameters: self, data and parent node
    def remove(self, data, parentNode):
        if data < self.data:
            if self.leftChild is not None:
                self.leftChild.remove(data, self)
        elif data > self.data:
            if self.rightChild is not None:
                self.rightChild.remove(data, self)
        else:
            if self.leftChild is not None and self.rightChild is not None:
                self.data = self.rightChild.getMin()
                self.rightChild.remove(self.data, self)
            elif parentNode.leftChild == self:
                if self.leftChild is not None:
                    tempNode = self.leftChild
                else:
                    tempNode = self.rightChild

                parentNode.leftChild = tempNode

            elif parentNode.rightChild == self:
                if self.leftChild is not None:
                    tempNode = self.leftChild
                else:
                    tempNode = self.rightChild

                parentNode.rightChild = tempNode


    def getMin(self):
        if self.leftChild is None:
            return self.data
        else:
            self.leftChild.getMin()

    def getMax(self):
        if self.rightChild is None:
            return self.data
        else:
            self.rightChild.getMax()

    def traverseInOrder(self):
        if self.leftChild is not None:
            self.leftChild.traverseInOrder()

        print(self.data)

        if self.rightChild is not None:
            self.rightChild.traverseInOrder()
# Defining a class
class Node(object):
    # Constructor
    def __init__(self, data):
        self.data = data
        self.nextNode = None

    # Function to remove a node
    def remove(self, data, previousNode):
        if self.data == data:
            previousNode.nextNode = self.nextNode
            del self.data
            del self.nextNode
        else:
            self.nextNode.remove(data, self)

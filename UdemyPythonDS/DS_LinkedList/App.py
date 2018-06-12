from DS_LinkedList.LinkedList import LinkedList

linkedList = LinkedList()

linkedList.insertEnd(12)
linkedList.insertEnd(122)
linkedList.insertStart(31)
linkedList.insertStart(3)

print('\nThis is the first run:')
linkedList.traverseList()
print('The size of the list is:', linkedList.size())

linkedList.remove(12)

print('\nThis is the second run:')
linkedList.traverseList()
print('The size of the list is:', linkedList.size())
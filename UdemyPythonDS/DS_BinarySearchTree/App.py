from DS_BinarySearchTree.BinarySearchTree import BST

bst = BST()
bst.insert(12)
bst.insert(10)
bst.insert(-2)
bst.insert(1)

print('Traversing the original tree:')
bst.traverseInOrder()

print('Max value in the tree:', bst.getMax())
print('Min value in the tree:', bst.getMin())

print('Traversing the tree with one node removed:')
bst.remove(10)
bst.traverseInOrder()
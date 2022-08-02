class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        node = Node(value)
        if self.root == None:
            self.root = node
            return True
        temp = self.root
        while True:
            if node.value == temp.value:
                return False
            if node.value < temp.value:
                if temp.left is None:
                    temp.left = node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = node
                    return True
                temp = temp.right


    def contains(self,value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
        
    def minValue(self,nodes):
        temp = nodes
        while temp.left is not None:
            temp = temp.left
        return temp.value

bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(6)
bst.insert(8)
bst.insert(1)
bst.insert(15)
bst.insert(19)
bst.insert(99)
bst.insert(11)
print('root value:', bst.root.value)
print(bst.root.left.value)
print(bst.root.right.value)
print(bst.contains(1))
print(bst.minValue(bst.root.right))
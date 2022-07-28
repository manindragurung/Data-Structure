# Removing an item from the tail end of a Linked List: O(n)
# Removing an item from the beginning of a Linked List: O(1)
# Finding an item by index in a Linked List: O(n)


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def prepend(self,value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def pop(self):
        temp = self.head
        pre = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            while temp.next:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
        self.length -= 1
        return temp

    def popFirst(self):
        temp = self.head
        if self.length == 0:
            return None
        else:
            self.head = temp.next
            temp.next = None
        self.length -= 1
        return temp

    def get(self,index):
        temp = self.head
        if index < 0 or index >= self.length:
            return None
        else:
            for _ in range(index):
                temp = temp.next
        return temp

    def setValue(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self,value,index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1   
        return True 

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.popFirst()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp 

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next



ssl = SingleLinkedList()
ssl.append(1)
ssl.append(2)
ssl.append(3)
ssl.printList()

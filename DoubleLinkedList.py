

class Node:
    def __init__(self,value):
        self.value = value
        self.before = None
        self.after = None

class DoulbleLinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
    
    def append(self,value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.after = node
            node.before = self.tail
            self.tail = node
        self.length += 1

    def prepend(self,value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.after = self.head
            self.head.before = node
            self.head = node
        self.length += 1



    def pop(self):
        temp = self.tail
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.before
            self.tail.after = None
            temp.before = None
        self.length -= 1
        return temp

    def popFirst(self):
        temp = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.after
            self.head.before = None
            temp.after = None
        self.length -= 1
        return temp

    def get(self,index):
        temp = self.head
        if index < 0 or index >= self.length:
            return None
        elif index < self.length/2:
            for _ in range(index):
                temp = temp.after
        else:
            temp = self.tail
            for _ in range(self.length-1,index,-1):
                temp = temp.before
        return temp

    def setValue(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self,index,value): 
        a=None
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length - 1:
            return self.append(value)
        prev = self.get(index - 1)
        next = prev.after
        node = Node(value)
        node.before = prev
        node.after = next
        prev.after = node
        next.before = node
        self.length += 1
        
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.popFirst()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        temp.after.before = temp.before
        temp.before.after = temp.after
        temp.before = None
        temp.after = None
        self.length -= 1
        return temp




    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.after

ddl = DoulbleLinkedList()
ddl.append(0)
ddl.append(1)
ddl.append(2)
ddl.append(3)
ddl.printList()


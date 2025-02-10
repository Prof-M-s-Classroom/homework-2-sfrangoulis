import Spaceship


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self):
        return str(self.head)

    def append(self, value):
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def delfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def dellast(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def insertatindex(self, index: int, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            print("Index out of range")
            return False

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        counter = 0
        pre = None
        temp = self.head
        while counter < index:
            pre = temp
            temp = temp.next
            counter += 1

        pre.next = new_node
        new_node.next = temp
        self.length += 1
        return True

    def deleteatindex(self, index: int):
        if index < 0 or index > self.length:
            print("Index out of range")
            return False

        if index == 0:
            return self.delfirst()


        if index == self.length:
            return self.dellast()


        counter = 0
        pre = None
        temp = self.head
        while counter < index:
            pre = temp
            temp = temp.next
            counter += 1

        pre.next = None
        pre.next = temp.next
        self.length -= 1
        return True








# TODO : Write function insertatindex to insert a newnode at any given index. Consider all edge cases, including missing nodes.

# TODO : Write fucntion deleteatindex to delete a newnode at any given index. COnsider all edge cases, including missing nodes.
# Make sure to reuse existing function for the correct edge cases for both TODOs
# Write appropriate test function below to test for the new functions.

s1 = Spaceship.Spaceship("Voyager", 300)
s2 = Spaceship.Spaceship("Enterprise", 300)
s3 = Spaceship.Spaceship("Atlantis", 300)
s4 = Spaceship.Spaceship("Challenger", 300)
s5 = Spaceship.Spaceship("Artemis", 300)

mylinkedlist = LinkedList(s1)
mylinkedlist.append(s2)
mylinkedlist.append(s3)
mylinkedlist.append(s4)
mylinkedlist.append(s5)

mylinkedlist.deleteatindex(2)
mylinkedlist.insertatindex(2, s3)



mylinkedlist.print_list()
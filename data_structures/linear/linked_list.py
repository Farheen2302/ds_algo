from node import Node


class UOLinkedList:

    def __init__(self, head=None):
        self.head = head
        self.size = 1 if self.head else 0

    def __str__(self):
        current = self.head
        output = ""
        while current != None:
            output += str(current.getValue()) + ' '
            current = current.getNext()
        return output

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.head == None

    # Adds item at the beginning
    def add(self, item):
        # item.setNext(self.head)
        # self.head = item
        # self.size += 1
        """ Saves us from declaring Node instances. """
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.size += 1

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getValue() == item:
                found = True
            else:
                current = current.getNext()
        return found

    """ Removes the given item """
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getValue() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        self.size -= 1

    """ Deletes the item at given position """
    def delete(self, pos):
        i = 1
        current = self.head
        previous = None
        if pos > 1:
            while i < pos and current != None:
                previous = current
                current = current.getNext()
                i += 1
            previous.setNext(current.getNext())
            current.setNext(None)
        else:
            self.head = current.getNext()
            current.setNext(None)
        self.size -= 1

    def append(self, item):
        tmp = Node(item)
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        current.setNext(tmp)
        tmp.setNext(None)
        self.size += 1

    def insert(self, pos, item):
        tmp = Node(item)
        i = 1
        current = self.head
        previous = None
        if pos > 1:
            while i < pos and current != None:
                previous = current
                current = current.getNext()
                i += 1
            previous.setNext(tmp)
            tmp.setNext(current)
        else:
            self.add(item)
        self.size += 1

    def index(self, item):
        pos = 0
        current = self.head
        while current != None:
            pos += 1
            if current.getValue() == item:
                return pos
            else:
                current = current.getNext()

# Test Cases
mylist = UOLinkedList()
mylist.add("Saurav")
mylist.add("Pratik")
mylist.add("Bay")
mylist.add("Bangalore")
mylist.add("Jamshedpur")
mylist.add("Square")
assert mylist.getSize() == 6
assert mylist.search("Jamshedpur") == True
assert mylist.search("India") == False

mylist.add("India")
assert mylist.getSize() == 7
assert mylist.search("India") == True

mylist.remove("Pratik")
assert mylist.getSize() == 6
mylist.remove("Bay")
assert mylist.getSize() == 5
mylist.remove("Square")
assert mylist.getSize() == 4
mylist.append("Panther")
assert mylist.getSize() == 5
mylist.insert(3, "Six")
assert mylist.index("Six") == 3
mylist.insert(4, "Eight")
assert mylist.index("Eight") == 4

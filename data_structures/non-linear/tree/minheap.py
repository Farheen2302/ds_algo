class MinBinaryHeap:

    def __init__(self):
        self.list = [0]
        self.size = 0

    def insert(self, element):
        self.list.append(element)
        self.size += 1
        self.percUp(self.size)

    def percUp(self, i):
        while i // 2 > 0:
            if self.list[i // 2] > self.list[i]:
                self.list[i // 2], self.list[i] = self.list[i], self.list[i // 2]
            i = i // 2

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def findMin(self):
        return self.list[1]

    def delMin(self):
        minval = self.list[1]
        self.list[1] = self.list[self.size]
        self.size -= 1
        self.list.pop()
        self.percDown(1)
        return minval

    def percDown(self, i):
        while 2 * i <= self.size:
            mc = self.getMinChild(i)
            if self.list[i] > self.list[mc]:
                self.list[i], self.list[mc] = self.list[mc], self.list[i]
            i = mc

    def getMinChild(self, i):
        if 2 * i + 1 > self.size:
            return 2 * i
        else:
            if self.list[2 * i + 1] < self.list[2 * i]:
                return 2 * i + 1
            else:
                return 2 * i

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.size = len(alist)
        self.list = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i -= 1

bh = MinBinaryHeap()
bh.buildHeap([9, 5, 6, 2, 3])
assert bh.findMin() == 2
bh.insert(45)
bh.insert(5)
assert bh.findMin() == 2
bh.delMin()
assert bh.findMin() == 3
bh.insert(1)
assert bh.findMin() == 1
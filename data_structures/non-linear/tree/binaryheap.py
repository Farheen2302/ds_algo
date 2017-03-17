# Max Heap
class BinaryHeap:

    def __init__(self):
        self.list = [0]
        self.size = 0

    def insert(self, element):
        self.list.append(element)
        self.size += 1
        self.percUp(self.size)

    def percUp(self, i):
        while i // 2 > 0:
            if self.list[i] > self.list[i // 2]:
                self.list[i], self.list[
                    i // 2] = self.list[i // 2], self.list[i]
            i = i // 2

    def findMax(self):
        return self.list[1]

    def delMax(self):
        maxval = self.list[1]
        self.list[1] = self.list[self.size]
        self.size -= 1
        self.list.pop()
        self.percDown(1)
        return maxval

    def percDown(self, i):
        while 2 * i <= self.size:
            mc = self.maxChild(i)
            if self.list[mc] > self.list[i]:
                self.list[mc], self.list[i] = self.list[i], self.list[mc]
            i = mc

    def maxChild(self, i):
        if 2 * i + 1 > self.size:
            return 2 * i
        else:
            if self.list[2 * i] > self.list[2 * i + 1]:
                return 2 * i
            else:
                return 2 * i + 1

    def isEmpty(self):
        return self.size == 1

    def size(self):
        return self.size

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.size = len(alist)
        self.list = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i -= 1

# Test Cases
bh = BinaryHeap()
bh.buildHeap([9, 5, 6, 2, 3])
assert bh.findMax() == 9
bh.insert(10)
assert bh.findMax() == 10
bh.delMax()
assert bh.findMax() == 9
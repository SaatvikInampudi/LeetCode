class MinStack:

    def __init__(self):
        self.arr = []
        # self.minval = float('inf')
        # self.minHeap = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        # if self.minval > val:
        #     self.minval = val
        # heapq.heappush(self.minHeap,val)

    def pop(self) -> None:
        # if self.arr[-1] == self.minHeap[0]:
        #     heapq.heappop(self.minHeap)
        self.arr = self.arr[0:len(self.arr)-1]
        print(self.arr)

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        # return self.minHeap[0]
        return min(self.arr)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, key):
        self.heap.append(key) 
        self._heapify_up(len(self.heap) - 1)  

    def delete(self, index):
        if index >= len(self.heap):
            return
        self.heap[index] = self.heap[-1] 
        self.heap.pop()  
        if index < len(self.heap): 
            self._heapify_down(index)
            self._heapify_up(index)

    def max_heapify(self, i):
        largest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)

    def extract_max(self):
        """extract the max value"""
        if not self.heap:
            return None
        max_value = self.heap[0]
        self.delete(0)
        return max_value

    def _heapify_up(self, i):
        """bottom-up"""
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            # swap if larger than parent
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def _heapify_down(self, i):
        """top-down"""
        self.max_heapify(i)

    def heap_sort(self):
        result = []
        original_size = len(self.heap)
        for _ in range(original_size):
            result.append(self.extract_max())
        return result

    def display(self):
        print(self.heap)

# testing
if __name__ == "__main__":
    max_heap = MaxHeap()
    max_heap.insert(10)
    max_heap.insert(20)
    max_heap.insert(15)
    max_heap.insert(30)
    max_heap.insert(40)

    print("max heap:")
    max_heap.display()

    print("extract the maximum:", max_heap.extract_max())
    print("delete the element with index 2:")
    max_heap.delete(2)
    max_heap.display()

    print("heap sort:", max_heap.heap_sort())

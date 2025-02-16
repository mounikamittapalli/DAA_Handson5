class minimum_heap:
    def __init__(self, data=None):
        self.heap = data
        self.build_minimum_heap()

    #adding nodes using bit manipulation
    def parent(self, i):
        return (i - 1) >> 1

    def left_child(self, i):
        return (i << 1) + 1

    def right_child(self, i):
        return (i << 1) + 2


    def build_minimum_heap(self):
        for i in range(len(self.heap) // 2, -1, -1):
            self.heapify(i)

    # Heapify a subtree with the root at index i
    def heapify(self, i):
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    # Remove and return the root (min value)
    def remove(self):
        if len(self.heap) == 0:
            raise IndexError("remove from empty heap")
        root_value = self.heap[0]
        self.heap[0] = self.heap[-1]  # Move the last element to root
        self.heap.pop()  # Remove the last element
        self.heapify(0)  # Re-heapify the root
        return root_value

    # Insert a new element into the heap
    def insert(self, value):
        self.heap.append(value)  # Add value to the end of the list
        i = len(self.heap) - 1  # Index of the newly inserted element
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    # Get the root element (min value)
    def get_root_element(self):
        if len(self.heap) == 0:
            raise IndexError("get root element from empty heap")
        return self.heap[0]

    # Print the heap
    def __str__(self):
        return str(self.heap)

# Example usage
if __name__ == "__main__":
    # Create a min heap from an unsorted list
    data1 = [20, 15, 30, 40, 10, 50, 5, 35]#in alist
    print("intial min heap with unsorted list in int:", data1)


    min_heap1 = minimum_heap(data1)
    print("Initial Min Heap in int:", min_heap1)
    print("remove root:", min_heap1.remove())# Pop the root (min value)
    print("Min Heap after removing root:", min_heap1)
    min_heap1.insert(3) # Insert new element
    print("Min Heap after inserting 3:", min_heap1)
    print("Peek at the root:", min_heap1.get_root_element())# Peek at the root element
    print()
    data2 = [20.5, 15.3, 30.2, 40.1, 10.4, 50.7, 5.8, 35.6]  # using float
    print("intial min heap with unsorted list in float:",data2)
    min_heap2 = minimum_heap(data2)
    print("Initial Min Heap in float:", min_heap2)
    print("remove root:", min_heap2.remove())# Pop the root (min value)
    print("Min Heap after removing root:", min_heap2)
    min_heap1.insert(3.5)# Insert new element
    print("Min Heap after inserting 3:", min_heap2)
    print("Peek at the root:", min_heap2.get_root_element())# Peek at the root element

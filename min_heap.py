# Name: Miles Kesser
# OSU Email: kesserm@oregonstate.osu
# Course: CS261 - Data Structures
# Assignment: 6: MinHeap Implementation
# Due Date: 23 November 2021
# Description: Produces a tree with min heap properties based on values inputted from a dynamic array
# Import DynamicArray from Assignment 2
from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()
        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self.heap[i] for i in range(self.heap.length())]
        return 'HEAP ' + str(heap_data)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def percolate_up(self, node):
        """
        Percolates up from a node
        """
        node_index = self.heap.length() - 1
        node = self.heap.get_at_index(node_index)
        # Percolate loop
        while node_index != 0:
            # Set parent to value of nodes parent
            parent_index = ((node_index - 1) // 2)
            # Index of the parent node
            parent_node = parent_node = self.heap.get_at_index(((node_index - 1) // 2))
            # Percolate up swapping values when needed
            if node < parent_node:
                self.heap.swap(node_index, parent_index)
            # Update node index to its parent
            node_index = parent_index

    def percolate_down(self, node_index):
        """
        Percolates down from a node
        """
        # Set length to the current length of array
        length = self.heap.length() - 1
        # Set left_index to left child index
        left_index = (node_index * 2) + 1
        # Set right_index to right child index
        right_index = (node_index * 2) + 2
        # Set current min to node index
        temp_node_index = node_index
        # If node has a left child
        if left_index <= length:
            # If node value is larger than its left child
            if self.heap.get_at_index(node_index) > self.heap.get_at_index(left_index):
                # Set temp_node_index to left index
                temp_node_index = left_index
                # If node has a right child
        if right_index <= length:
            # If current node value is larger than its right child
            if self.heap.get_at_index(temp_node_index) > self.heap.get_at_index(right_index):
                # Set temp_node_index to right index
                temp_node_index = right_index

        if temp_node_index != node_index:
            # Swap values at indices
            self.heap.swap(node_index, temp_node_index)
            # Percolate with updated value
            self.percolate_down(temp_node_index)

    def add(self, node: object) -> None:
        """
        Adds a new object to the MinHeap maintaining heap property
        """
        self.heap.append(node)
        # Index of inputted node
        node_index = self.heap.length() - 1
        # Set node to the value of node
        node = self.heap.get_at_index(node_index)
        # If not the root
        if node_index != 0:
            # Percolate up from node index
            self.percolate_up(node_index)

    def get_min(self) -> object:
        """
        Returns an object with a minimum key without removing it from the heap.
        If the heap is empty,the method raises a MinHeapException
        """
        # If empty, raise exception
        if self.is_empty():
            raise MinHeapException()
        else:
            # Return first element
            return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        Returns an object with a minimum key and removes it from the heap.
        If the heap is empty, the method raises a MinHeapException
        """
        # If tree is empty raise exception
        if self.is_empty():
            raise MinHeapException()

        # Value of root
        min_val = self.heap.get_at_index(0)
        # Value of last value in array
        last_node_index = self.heap.length() - 1
        # Swap values of root and newly inputted node
        self.heap.swap(0, last_node_index)
        # Remove last element in array
        self.heap.pop()
        # Percolate down
        self.percolate_down(0)

        return min_val

    def build_heap(self, da: DynamicArray) -> None:
        """
        Receives a dynamic array with objects in any order and builds a proper MinHeap from them
        """
        length = da.length() - 1
        parent_node_index = (length - 1) // 2
        # Build heap
        # Percolate down at each parent node until root
        while parent_node_index > 0:
            # New parent node index
            parent_node_index = (length - 1) // 2
            # If node only has left child
            if (parent_node_index * 2) + 2 > length:
                # If node value is larger than left node value
                if da.get_at_index(parent_node_index) > da.get_at_index((parent_node_index * 2) + 1):
                    # Swap node value with left node value
                    da.swap(parent_node_index, (parent_node_index * 2) + 1)
            # If node has two children
            elif (parent_node_index * 2) + 1 <= length and (parent_node_index * 2) + 2 <= length:
                # If parent value is larger than left value, and right value is larger than left value
                if da.get_at_index(parent_node_index) > da.get_at_index((parent_node_index * 2) + 1) and da.get_at_index((parent_node_index * 2) + 2) > da.get_at_index((parent_node_index * 2) + 1):
                    # Swap node value with left child value
                    da.swap(parent_node_index, (parent_node_index * 2) + 1)
                # If node value is larger than right child
                if da.get_at_index(parent_node_index) > da.get_at_index((parent_node_index * 2) + 2):
                    # Swap node value with right child value
                    da.swap(parent_node_index, (parent_node_index * 2) + 2)
            # Decrement length by 2 to find next parent in tree
            length -= 2
        # Percolate down at root
        parent_node_index = 0
        # If node value is larger than left child, and left child is smaller than right child
        if da.get_at_index(parent_node_index) > da.get_at_index((parent_node_index * 2) + 1) and da.get_at_index((parent_node_index * 2) + 2) > da.get_at_index((parent_node_index * 2) + 1):
            da.swap(parent_node_index, (parent_node_index * 2) + 1)
        # If node value is larger than right child
        if da.get_at_index(parent_node_index) > da.get_at_index((parent_node_index * 2) + 2):
            # Swap node value with right child value
            da.swap(parent_node_index, (parent_node_index * 2) + 2)

    # @staticmethod
    def heapsort(da: DynamicArray) -> None:
        """
        Receives a DynamicArray and sorts its content in non-ascending order using the Heapsort algorithm
        """
        if da.length() == 0:
            return None

        length = da.length() - 1
        parent_node_index = (length - 1) // 2
        # Build heap
        # Percolate down at each parent node up to root
        while parent_node_index > 0:
            # New parent node index
            parent_node_index = (length - 1) // 2
            # If node value is larger than left child, and left child is smaller than right child
            if da.get_at_index(parent_node_index) > da.get_at_index((parent_node_index * 2) + 1) and da.get_at_index(
                    (parent_node_index * 2) + 2) > da.get_at_index((parent_node_index * 2) + 1):
                # Swap node value with left child value
                da.swap(parent_node_index, (parent_node_index * 2) + 1)

            # If node value is larger than right child
            elif da.get_at_index(parent_node_index) > da.get_at_index((parent_node_index * 2) + 2):
                # Swap node value with right child value
                da.swap(parent_node_index, (parent_node_index * 2) + 2)
            # Decrement length by 2 to find next parent in tree
            length -= 2

        # Rearrange array in place
        k = da.length() - 1
        # Initial swap of first and last element
        da.swap(0, k)

        while k > 1:
            # Reset parent index to zero
            parent_node_index = 0
            while parent_node_index < k // 2:
                # Set length to the current length of array
                length = k
                # Set left_index to left child index
                left_index = (parent_node_index * 2) + 1
                # Set right_index to right child index
                right_index = (parent_node_index * 2) + 2
                # If left index is within length, less than k, value is less than parent,
                # right node value is greater than left value
                if left_index <= length and left_index < k and da.get_at_index(parent_node_index) > da.get_at_index(
                        left_index) and da.get_at_index(right_index) > da.get_at_index(left_index):
                    # Swap values at parent and left child indices
                    da.swap(parent_node_index, left_index)
                    # Change parent index
                    parent_node_index = left_index
                # If right index is within length, less than k, and value is less than parent
                elif right_index <= length and right_index < k and da.get_at_index(parent_node_index) > da.get_at_index(
                        right_index):
                    # Swap values at parent and right indices
                    da.swap(parent_node_index, right_index)
                    # Change parent index
                    parent_node_index = right_index
                else:
                    # Decrement k
                    k -= 1
                    # Swap values at first and last indices
                    da.swap(0, k)
                    # Reset parent index
                    parent_node_index = 0
        # Last iteration
        parent_node_index = 0
        right_index = (parent_node_index * 2) + 2
        left_index = (parent_node_index * 2) + 1
        if left_index <= length and da.get_at_index(parent_node_index) < da.get_at_index(left_index):
            da.swap(parent_node_index, left_index)
        elif left_index <= length and da.get_at_index(parent_node_index) < da.get_at_index(right_index):
            da.swap(parent_node_index, right_index)

    def size(self) -> int:
        """
        Returns the number of items currently stored in the heap in O(1) runtime complexity
        """
        # Length = number of elements in array
        return self.heap.length()

    def clear(self) -> None:
        """
        Clears the contents of the heap in O(1) runtime complexity
        """
        # Reduces size to 0 regardless of values stored
        self.heap.set_length(0)


# BASIC TESTING
if __name__ == '__main__':
    """print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)
    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)
    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())
    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())"""
    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([-40599, -9377, 81349, 38113, 40036, -99532])
    h = MinHeap()
    #print(h)
    h.build_heap(da)
    #print(h)
    #da[0] = 500
    print(da)
    #print(h)
    """print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    MinHeap.heapsort(da)
    print(f"After:  {da}")
    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    MinHeap.heapsort(da)
    print(f"After:  {da}")
    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())
    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())
    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)"""""
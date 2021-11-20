# Name: Miles Kesser
# OSU Email: kesserm@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2
# Due Date: October 18th
# Description: Dynamic Array class with methods

from static_array import *


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.data = StaticArray(self.capacity)
        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/" + str(self.capacity) + ' ['
        out += ', '.join([str(self.data[_]) for _ in range(self.size)])
        return out + ']'

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        return self.data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        self.data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size

    def set_length(self, num):
        """
        Sets new length to num
        CUSTOM METHOD
        """
        self.size = num

    def set_length_plus(self):
        """
        Sets new length for appended value
        CUSTOM METHOD
        """
        self.size += 1

    def set_length_minus(self):
        """
        Sets new length for removed value
        CUSTOM METHOD
        """
        self.size -= 1

    def set_cap(self, num) -> None:
        """
        Sets new capacity
        CUSTOM METHOD
        """
        self.capacity = num

    def get_cap(self) -> int:
        """
        Returns capacity
        CUSTOM METHOD
        """
        return self.capacity

    def get_input_arr(self):
        """
        Return original static array
        CUSTOM METHOD
        """
        return self.data

    def set_input_arr(self, arr):
        """
        Sets original input array to arr
        CUSTOM METHOD
        """
        self.data = arr

        # -----------------------------------------------------------------------

    def swap(self, node_index1, node_index2):
        """
        Swaps values of node and its parent
        """
        node1 = self.get_at_index(node_index1)
        node2 = self.get_at_index(node_index2)

        self.set_at_index(node_index1, node2)
        self.set_at_index(node_index2, node1)

    def pop(self):
        """
        removes last element and returns its vaue
        """
        num = self.get_at_index(self.length() - 1)

        self.set_at_index((self.length() - 1), None)
        self.set_length_minus()
        # self.set_cap(self.length())

        return num

    def resize(self, new_capacity: int) -> None:
        """
        Changes the capacity of the underlying storage for the array elements
        """
        # If capacity is zero return
        if new_capacity <= 0:
            return

        # Sets original capacity to new capacity if larger than number of elements
        if new_capacity >= self.length():
            self.set_cap(new_capacity)

        # Initialize new static array with new capacity
        newArr = StaticArray(self.get_cap())

        index = 0
        # Transfer elements from original array to new array
        while index < self.length():
            newArr[index] = self.get_input_arr()[index]
            index += 1
        self.set_input_arr(newArr)

    def append(self, value: object) -> None:
        """
        Adds a new value at the end of the dynamic array
        """
        # Double capacity if full of elements
        if self.length() == self.get_cap():
            self.resize(self.get_cap() * 2)
            self.get_input_arr()[self.length()] = value

        else:
            # Add value to array
            self.get_input_arr()[self.length()] = value
        # Increase size
        self.set_length_plus()

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Adds a new value at the specified index position
        """
        if index < 0 or index > self.length():
            raise DynamicArrayException()

        # Double capacity if array full
        if self.length() == self.get_cap():
            self.resize(self.get_cap() * 2)

        # Inserting at first position if occupied
        if self.get_input_arr()[index] is not None and index == 0:

            newArr = StaticArray(self.get_cap())

            index = 0
            num = self.length()

            while index < self.length():
                newArr[num] = self.get_input_arr()[num - 1]
                index += 1
                num -= 1

            newArr[0] = value
            self.set_length_plus()
            self.set_input_arr(newArr)

        # Inserting other than first position if occupied
        elif self.get_input_arr()[index] is not None and index != 0:

            newArr = StaticArray(self.get_cap())

            for num in range(self.length(), index - 1, -1):
                newArr[num] = self.get_input_arr()[num - 1]
            for num in range(0, index):
                newArr[num] = self.get_input_arr()[num]

            newArr[index] = value
            self.set_length_plus()
            self.set_input_arr(newArr)

        # Inserting if position is unoccupied
        elif self.get_input_arr()[index] is None:
            newArr = StaticArray(self.get_cap())
            for index in range(0, self.length() + 1):
                newArr[index] = self.get_input_arr()[index]

            newArr[index] = value
            self.set_length_plus()
            self.set_input_arr(newArr)

    def remove_at_index(self, index: int) -> None:
        """
        Removes the element at the specified index
        """
        if index < 0 or index > self.length() - 1:
            raise DynamicArrayException()

        # Resize capacity when needed
        if self.get_cap() > 10:
            if self.length() < self.get_cap() / 4:
                if self.length() * 2 < 10:
                    self.set_cap(10)
                else:
                    self.set_cap(self.length() * 2)

        # If first element
        if self.get_input_arr()[index] is not None and index == 0:
            newArr = StaticArray(self.get_cap())
            for i in range(0, self.length() - 1):
                newArr[i] = self.get_input_arr()[i + 1]

            self.set_length_minus()
            self.set_input_arr(newArr)

        # If last element
        if self.get_input_arr()[index] is not None and index != 0 and index == self.length() - 1:

            newArr = StaticArray(self.get_cap())
            for i in range(0, self.length() - 1):
                newArr[i] = self.get_input_arr()[i]

            self.set_length_minus()
            self.set_input_arr(newArr)

        # If element in middle
        if self.get_input_arr()[index] is not None and index != 0 and index != self.length() - 1:
            newArr = StaticArray(self.get_cap())
            for i in range(index, self.length() - 1):
                newArr[i] = self.get_input_arr()[i + 1]
            for j in range(0, index):
                newArr[j] = self.get_input_arr()[j]

            self.set_length_minus()
            self.set_input_arr(newArr)

    def slice(self, start_index: int, size: int) -> object:
        """
        Returns a new Dynamic Array object that contains the
        requested number of elements from the original array starting
        with the element located at the requested start index
        """

        if start_index < 0 or size < 0 or (start_index + size) > self.length() or start_index >= self.length():
            raise DynamicArrayException()
        if size == 0:
            return DynamicArray()

        # Initialize new array and transfer elements between and including start and size
        newArr = StaticArray(size)
        for i in range(start_index, start_index + size):
            newArr[i - start_index] = self.get_input_arr()[i]
        newDA = DynamicArray()
        newDA.resize(newArr.length())
        newDA.set_length(size)
        newDA.set_input_arr(newArr)

        sizeTwo = 4
        while (sizeTwo < size):
            sizeTwo *= 2
        newDA.set_cap(sizeTwo)

        return newDA

    def merge(self, second_da: object) -> None:
        """
        This method takes another Dynamic Array object as a parameter,
        and appends all elements from this other array onto the current one,
        in the same order as they are stored in the array parameter.
        """
        # Append elements in new array to original array
        for i in range(0, second_da.length()):
            self.append(second_da[i])

    def map(self, map_func) -> object:
        """
        Creates a new Dynamic Array where the value of
        each element is derived by applying a given map_func
        """
        # Initialize new array
        newArr = StaticArray(self.length())
        i = 0

        # Each value evaluated with map function
        while i < self.length():
            newArr[i] = map_func(self.get_input_arr()[i])
            i += 1

        newDA = DynamicArray()
        newDA.resize(newArr.length())
        newDA.set_length(self.length())
        newDA.set_input_arr(newArr)

        sizeTwo = 4
        while (sizeTwo < self.length()):
            sizeTwo *= 2
        newDA.set_cap(sizeTwo)

        return newDA

    def filter(self, filter_func) -> object:
        """
        Creates a new Dynamic Array populated only with
        those elements from the original array for which
        filter_func returns True
        """
        if self.length() == 0:
            return DynamicArray()

        newArr = StaticArray(self.length())
        i = 0
        insert = 0

        # Each value evaluated with filter function and adds True values to new array
        while i < self.length():
            if filter_func(self.get_input_arr()[i]):
                newArr[insert] = self.get_input_arr()[i]
                insert += 1
            i += 1

        newDA = DynamicArray()
        newDA.resize(insert)
        newDA.set_length(insert)
        newDA.set_input_arr(newArr)

        sizeTwo = 4
        while (sizeTwo < insert):
            sizeTwo *= 2
        newDA.set_cap(sizeTwo)

        return newDA

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Sequentially applies the reduce_func to all elements of the
        Dynamic Array and returns the resulting value
        """
        # If array and initializer is length zero, return nothing
        if self.length() == 0:
            if initializer is None:
                return None
            else:
                return initializer

        # If there is no initializer, treat first element in array as such
        if initializer is None:
            i = 1
            initializer = self.get_input_arr()[0]
            while i < self.length():
                initializer = reduce_func(initializer, self.get_input_arr()[i])
                i += 1
            return initializer

        # If there is an initializer, evaluate all values in array
        if initializer is not None:
            i = 0
            while i < self.length():
                initializer = reduce_func(initializer, self.get_input_arr()[i])
                i += 1
            return initializer
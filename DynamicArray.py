import ctypes


class DynamicArray:
    """
    dynamic python array instead of python list
    """
    def __init__(self):
        """
        create an empty array
        """
        self._number_of_actual_elements = 0
        self._capacity = 1
        self._low_level_array = self._make_array(self._capacity)

    def __len__(self) -> int:
        """

        :return: the length of array
        """
        return self._number_of_actual_elements

    def  __getitem__(self, index: int) -> object:
        """

        :type index: int
        :param index: the index of desired item in the array.
        :return: return the item.
        """
        if not 0 <= index < self._number_of_actual_elements:
            raise IndexError("index out of range")
        return self._low_level_array[index]

    def is_empty(self):
        if self._number_of_actual_elements == 0:
            return True
        return False

    def pop(self):
        if self.is_empty():
            raise Exception("empty array")
        var = self._low_level_array[self._number_of_actual_elements - 1]
        self._number_of_actual_elements -= 1
        return var

    def append(self, item: object):
        """
        add object to the end of array
        :param item: desired object
        """
        if self._number_of_actual_elements == self._capacity:
            self._resize(2 * self._capacity)
        self._low_level_array[self._number_of_actual_elements] = item
        self._number_of_actual_elements += 1

    def _resize(self, new_size: int):
        """
        resize the internal array to capacity new_size
        :param new_size: desired capacity
        """
        new_array = self._make_array(new_size)
        for k in range(self._number_of_actual_elements):
            new_array[k] = self._low_level_array[k]
        self._low_level_array = new_array
        self._capacity = new_size

    def _make_array(self, capacity: int) -> object:
        """
        return new array with fixed capacity.
        :param capacity: the desired capacity
        :return: return ctypes array
        """
        return (capacity * ctypes.py_object)()


if __name__ == '__main__':
    c_array = DynamicArray()
    for i in "Damavand_iran":
        c_array.append(i)

    for i in range(len(c_array)):
        print(c_array[i])
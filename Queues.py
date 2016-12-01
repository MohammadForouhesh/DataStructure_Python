
class ArrayQueues:
    """
    FIFO circular Queue implementation using python list as internal storage.
    """
    DEAFAULT_SIZE = 10

    def __init__(self):
        """
        _data: a reference to a list instance with a fixed capacity
        _size: as an integer representation of the number of elements stored in queue.
        _front: a reference to where the data begin in queue.
        """
        self._data = [None]*ArrayQueues.DEAFAULT_SIZE                                   # basic list
        self._size = 0                                                                  # number of elements
        self._front = 0                                                                 # reference to first element

    @property
    def __len__(self):
        """

        :return: the length of the queue size.
        """
        return len(self._size)                                                          # number of elements

    @property
    def is_empty(self) -> bool:
        """

        :return: bool True if empty, False otherwise.
        """
        if len(self._size) == 0:
            return True                                                                 # there is no element
        return False

    def front(self) -> object:
        """

        :return:
        """
        if self.is_empty:
            raise Exception("empty queue exception.")

        return self._data[self._front]

    def enqueue(self, element: object):
        """
        add an element to the queue
        :param element: add element to the the queue after the front
        """
        pass

    def dequeue(self) -> object:
        """
        remove and return current front from queue.
        :return: deleted previous front.
        """
        front_value = self._data[self._front]
        self._data[self._front] = None                                                  # delete the first element
        self._front = (self._front + 1) % self._data                                    # increment front circularly
        self._size -= 1                                                                 # number of elements decrements
        return front_value

    def _resize(self, newsize: object):
        """

        :param newsize:
        :return:
        """
        pass
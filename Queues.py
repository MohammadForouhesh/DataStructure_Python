
class ArrayQueues:
    """
    circular queue implementation with array.
    """
    def __init__(self, data: list, size: int, front: int):
        """

        :type data: list
        :type size: int
        :type front: int
        :param data: a reference to a list instance with a fixed capacity
        :param size: size of the queue independent of the length of data
        :param front: a reference to where the data begin in queue
        """
        self._data = data
        self._size = size
        self._front = front

    def __len__(self):
        """

        :return:
        """
        pass

    def is_empty(self) -> bool:
        pass

    def front(self) -> object:
        """

        :return:
        """
        pass

    def dequeue(self, element: object) -> object:
        """

        :param element:
        :return:
        """
        pass

    def enqueue(self) -> object:
        """

        :return:
        """
        pass

    def _resize(self, newsize: object):
        """

        :param newsize:
        :return:
        """
        pass
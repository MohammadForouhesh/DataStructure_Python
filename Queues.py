
class ArrayQueues:
    """
    FIFO circular Queue implementation using python list as internal storage.
    """
    DEFAULT_SIZE = 10

    def __init__(self):
        """
        _data: a reference to a list instance with a fixed capacity
        _size: as an integer representation of the number of elements stored in queue.
        _front: a reference to where the data begin in queue.
        """
        self._data = [None]*ArrayQueues.DEAFAULT_SIZE                                # basic list
        self._size = 0                                                               # number of elements
        self._front = 0                                                              # reference to first element

    @property
    def __len__(self):
        """

        :return: the length of the queue size.
        """
        return self._size                                                            # number of elements

    @property
    def is_empty(self) -> bool:
        """

        :return: bool True if empty, False otherwise.
        """
        if self._size == 0:
            return True                                                              # there is no element
        return False

    def front(self) -> object:
        """

        :return:
        """
        if self.is_empty:
            raise Exception("empty queue exception.")

        return self._data[self._front]

    def enqueue(self, element):
        """
        add an element to the queue
        :param element: add element to the the queue after the front
        """
        if self._size == len(self._data):                                            # queue is full !
            self._resize(2 * len(self._data))                                        # queue is doubled

        var = (self._front + self._size) % len(self._data)
        self._data[var] = element
        self._size += 1                                                              # number of elements is incremented

    def dequeue(self) -> object:
        """
        remove and return current front from queue.
        :return: deleted previous front.
        """
        if self.is_empty:
            raise Exception('Empty queue.')
        front_value = self._data[self._front]
        self._data[self._front] = None                                               # delete the first element
        self._front = (self._front + 1) % len(self._data)                            # increment front circularly
        self._size -= 1                                                              # number of elements is decremented
        return front_value

    def _resize(self, new_size: object):
        """
        assume that new_size > current_size
        :param new_size: the size we want to have
        """
        old_data = self._data
        self._data = [None] * new_size
        step = self._front

        for index in range(self._size):
            self._data[index] = old_data[step]                                      # actually old data are in room 0
            step = (step + 1) % len(old_data)                                       # to size - 1.
        self._front = 0                                                             # front reference should be realign

    def querry(self):
        """
        for TTD and debuging.
        """
        for k in self._data:
            print(k)


if __name__ == '__main__':
    q = ArrayQueues()
    for i in range(12):
        q.enqueue(i)

    for j in range(4):
        q.dequeue()

    for i in range(10):
        q.enqueue(i)

    q.querry()

    print()
    print("\/\/\/\/\/\/\//new test with adding capacity//\/\/\/\/\/\/\/")
    print()

    for i in "kilimanjaro":
        q.enqueue(i)

    q.querry()


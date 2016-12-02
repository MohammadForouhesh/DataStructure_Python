
class LinkedQueue:
    """
    FIFO implementation of queue with using linked list as internal storage
    """

    # ---------------------------------------------- Nested Class --------------------------------------------------
    class _Node:
        "light weight class for storing liked node"
        __slots__ = '_element', '_next'                                             # streamline memory usage

        def __init__(self, element, next):                                          # initialize node field
            self._element = element                                                 # reference to current element
            self._next = next                                                       # reference to the next node

    # --------------------------------------------- Stack Methods --------------------------------------------------
    def __init__(self):
        self._head = self._Node(None, None)
        self._tail = self._Node(None, None)
        self._size = 0

    def __len__(self) -> int:
        """
        return the number of elements in the linked list
        :return: integer
        """
        return self._size

    def __iter__(self):
        """
        iterate thorough the linked list
        """
        if self.is_empty():
            yield
        current = self._head
        while current is not None:
            yield current
            current = current._next

    def is_empty(self) -> bool:
        """

        :return: bool True if list is empty and False otherwise
        """
        return self._size == 0

    def first(self):
        """
        just Return the first element in the queue
        """
        if self.is_empty():
            raise Exception("empty Error")
        return self._head._element

    def dequeue(self):
        """
        remove and return the first element
        """
        if self.is_empty():
            raise Exception("empty Error")
        var = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return var

    def enqueue(self, element):
        newest = self._Node(element, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def querry(self):
        """
        for TTD and debuging.
        """
        for k in self:
            print(k._element)


if __name__ == '__main__':
    q = LinkedQueue()
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

    print()
    print("\/\/\/\/\/\/\//new test with adding capacity//\/\/\/\/\/\/\/")
    print()

    for i in range(25):
        q.dequeue()

    q.querry()
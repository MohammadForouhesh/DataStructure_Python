
class LinkedStack():
    """
    LIFO stack implementation using simple linked list as internal storage.
    """
    # ---------------------------------------------- Nested Class --------------------------------------------------
    class _Node:
        "light weight class for storing liked node"
        __slots__ = '_element', '_next'                                         # streamline memory usage

        def __init__(self, element, next):                                      # initialize node field
            self._element = element                                             # reference to current element
            self._next = next                                                   # reference to the next node

    # --------------------------------------------- Stack Methods --------------------------------------------------
    def __init__(self):
        self._head = self._Node(None, None)                                     # _head is a kind of node
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

    def push(self, element: object):
        """
        add element to the top of the stack
        :param element: element to add
        """
        self._head = self._Node(element, self._head)                            # created and linked a new node
        self._size += 1                                                         # size is incremented

    @property
    def top(self) -> object:
        """

        :return: the top element of the stack
        """
        if self.is_empty():
            raise Exception("stack is empty")
        return self._head._element

    def pop(self) -> _Node:
        """
        remove and return element from the top of the stack
        :return: return a _Node
        """
        if self.is_empty():
            raise Exception("stack is empty")
        answer = self._head._element
        self._head = self._head.next                                            # bypass the former node :)
        self._size -= 1                                                         # size decremented
        return answer

    def querry(self):
        """
        for TTD and debuging.
        """
        for k in self:
            print(k._element)

if __name__ == '__main__':
    stack = LinkedStack()
    for s in "saint_helen_mountain":
        stack.push(s)

    stack.querry()
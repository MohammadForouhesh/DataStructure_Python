
class ArrayStack:
    """
    LIFO stack implementation using Python list as underlying storage.
    """
    def __init__(self):
        self._contents = list()

    def __len__(self):
        return len(self._contents)

    def isEmpty(self) -> bool:
        """

        :return: bool True if Stack is empty.
        """
        if len(self._contents) == 0:
            return True
        return False

    def pop(self) -> object:
        """
        if the Stack is empty it will Rise empty exception

        :return: delete and return the last input
        """
        # if self.isEmpty:
        #     raise Exception("The Stack is empty")
        return self._contents.pop()

    def top(self) -> object:
        """
        if the Stack is empty it will Rise empty exception

        :return: return the last input object and not delete
        """
        # if self.isEmpty:
        #     raise Exception("The Stack is empty")
        var = self._contents[-1]
        return var

    def push(self, element: object):
        """

        :type element: object
        """
        self._contents.append(element)

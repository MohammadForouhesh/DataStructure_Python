from Array import DynamicArray


class ArrayStack:
    """
    LIFO stack implementation using self-written DynamicArray based on c-types array as underlying storage.
    """
    def __init__(self):
        self._contents = DynamicArray.DynamicArray()

    def __len__(self) -> int:
        """

        :return: the length of the stack
        """
        return len(self._contents)

    def isEmpty(self) -> bool:
        """

        :return: bool True if Stack is empty.
        """
        if len(self._contents) == 0:
            return True
        return False

    @property
    def pop(self) -> object:
        """
        if the Stack is empty it will Rise empty exception

        :return: delete and return the last input
        """
        # if self.isEmpty:
            # raise Exception("The Stack is empty")
        return self._contents.pop()

    @property
    def top(self) -> object:
        """
        if the Stack is empty it will Rise empty exception

        :return: return the last input object and not delete
        """
        # if self.isEmpty:
            # raise Exception("The Stack is empty")
        var = self._contents[-1]
        return var

    def push(self, element: object):
        """

        :type element: object
        """
        self._contents.append(element)

if __name__ == '__main__':
    var_stack = ArrayStack()
    for s in "everestMountain":
        var_stack.push(s)

    for s in range(len(var_stack)):
        print(var_stack.pop)


from LinkedList.DoublyLinkedBase import _DoublyLinkedBase
from abc import ABCMeta, abstractmethod


class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

    # -------------------------- nested Position class --------------------------
    class Position(metaclass=ABCMeta):
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            """
            Return the element stored at this Position.
            """
            return self._node._element

        def __eq__(self, other):
            """
            Return True if other is a Position representing the same location.
            """
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """
            Return True if other does not represent the same location.
            """
            return not (self == other)                                                 # opposite of __eq__


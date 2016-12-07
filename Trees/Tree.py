from LinkedList.LinkedQueue import LinkedQueue
from abc import ABCMeta


class Tree(metaclass=ABCMeta):
    """Abstract base class representing a tree structure."""

    # ------------------------------- nested Position class -------------------------------
    class Position:
        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)                                  # opposite of __eq__

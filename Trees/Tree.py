from LinkedList.LinkedQueue import LinkedQueue
from abc import ABCMeta


class Tree(metaclass=ABCMeta):
    """Abstract base class representing a tree structure."""

    # ------------------------------- nested Position class -------------------------------
    class Position:
        """An abstraction representing the location of a single element within a tree.
        Note that two position instaces may represent the same inherent location in a tree.
        Therefore, users should always rely on syntax 'p == q' rather than 'p is q' when testing
        equivalence of positions.
        """

        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other: Tree.Position):
            """Return True if other Position represents the same location."""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other: Tree.Position):
            """Return True if other does not represent the same location."""
            return not (self == other)                                  # opposite of __eq__

    # ---------- abstract methods that concrete subclass must support ----------
    @property
    def root(self):
        """
        Return Position representing the tree's root (or None if empty).
        """
        raise NotImplementedError('must be implemented by subclass')

    @property
    def parent(self, p):
        """
        Return Position representing p's parent (or None if p is root).
        """
        raise NotImplementedError('must be implemented by subclass')

    @property
    def num_children(self, p):
        """
        Return the number of children that Position p has.
        """
        raise NotImplementedError('must be implemented by subclass')

    @property
    def children(self, p):
        """
        Generate an iteration of Positions representing p's children.
        """
        raise NotImplementedError('must be implemented by subclass')

    @property
    def __len__(self):
        """
        Return the total number of elements in the tree.
        """
        raise NotImplementedError('must be implemented by subclass')


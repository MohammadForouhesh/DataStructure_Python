from abc import ABCMeta, abstractmethod
from Trees.Tree import Tree


class BinaryTree(Tree, metaclass=ABCMeta):
    """
    Abstract base class representing a binary tree structure.
    """

    # --------------------- additional abstract methods ---------------------
    @abstractmethod
    def left(self, p):
        """
        Return a Position representing p's left child.
        Return None if p does not have a left child.
        """
        raise NotImplementedError('must be implemented by subclass')

    @abstractmethod
    def right(self, p):
        """
        Return a Position representing p's right child.
        Return None if p does not have a right child.
        """
        raise NotImplementedError('must be implemented by subclass')

    # ---------- concrete methods implemented in this class ----------
    def sibling(self, p):
        """Return a Position representing p's sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:                                                  # p must be the root
            return None                                                     # root has no sibling
        else:
            if p == self.left(parent):
                return self.right(parent)                                   # possibly None
            else:
                return self.left(parent)                                    # possibly None

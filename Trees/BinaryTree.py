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

    
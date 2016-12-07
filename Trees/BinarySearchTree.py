
from Trees.LinkedBinaryTree import LinkedBinaryTree
from Trees.MapBase import MapBase


class TreeMap(LinkedBinaryTree, MapBase):
    """Sorted map implementation using a binary search tree."""

    # ---------------------------- override Position class ----------------------------
    class Position(LinkedBinaryTree.Position):
        @property
        def key(self):
            """Return key of map's key-value pair."""
            return self.element()._key

        @property
        def value(self):
            """Return value of map's key-value pair."""
            return self.element()._value

    # ------------------------------- nonpublic utilities -------------------------------
    def _subtree_search(self, p, k):
        """Return Position of p's subtree having key k, or last node searched."""
        if k == p.key:                                                      # found match
            return p
        elif k < p.key:                                                     # search left subtree
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
        else:                                                               # search right subtree
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        return p                                                            # unsucessful search


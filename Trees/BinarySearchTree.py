
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

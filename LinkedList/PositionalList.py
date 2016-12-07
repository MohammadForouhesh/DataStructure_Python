from LinkedList.DoublyLinkedBase import _DoublyLinkedBase
from abc import ABCMeta


class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

    # -------------------------- nested Position class --------------------------
    class Position(metaclass=ABCMeta):
        """An abstraction representing the location of a single element.
        Note that two position instances may represent the same inherent
        location in the list, so We should always rely on
        syntax 'p == q' rather than 'p is q' in testing equivalence of
        positions.
        """

        __slots__ = '_node', '_container'

        def __init__(self, container, node):
            self._container = container
            self._node = _DoublyLinkedBase._Node(node, None, None)

        def __eq__(self, other: _DoublyLinkedBase._Node):
            """
            Return True if other is a Position representing the same location.
            """
            return type(other) is type(self) and other.node is self._node

        def __ne__(self, other: _DoublyLinkedBase._Node):
            """
            Return True if other does not represent the same location.
            """
            return not (self == other)                                            # opposite of __eq__

        @property
        def element(self):
            """
            Return the element stored at this Position.
            """
            return self._node.element

        @property
        def container(self):
            return self._container

        @property
        def node(self):
            return self._node

    # ------------------------------- utility methods -------------------------------
    def _validate(self, p):
        """
        Return position's node, or raise appropriate error if invalid.
        """

        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p.container is not self:
            raise ValueError('p does not belong to this container')
        if p.node.next is None:                                                   # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p.node

    def _make_position(self, node):
        """
        Return Position instance for given node (or None if sentinel).
        """

        if node is self._header or node is self._trailer:
            return None                                                             # boundary violation
        else:
            return self.Position(self, node)                                        # legitimate position

    # ------------------------------- accessors -------------------------------
    @property
    def first(self):
        """
        Return the first Position in the list (or None if list is empty).
        """

        return self._make_position(self._header._next)

    @property
    def last(self):
        """
        Return the last Position in the list (or None if list is empty).
        """

        return self._make_position(self._trailer._prev)

    def before(self, p):
        """
        Return the Position just before Position p (or None if p is first).
        """

        node = self._validate(p)
        return self._make_position(node.prev)

    def after(self, p):
        """
        Return the Position just after Position p (or None if p is last).
        """

        node = self._validate(p)
        return self._make_position(node.next)

    def __iter__(self):
        """
        Generate a forward iteration of the elements of the list.
        """

        cursor = self.first
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # ------------------------------- mutators -------------------------------
    # override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        """
        Add element between existing nodes and return new Position.
        """
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """
        Insert element e at the front of the list and return new Position.
        """

        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """
        Insert element e at the back of the list and return new Position.
        """

        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """
        Insert element e into list before Position p and return new Position.
        """

        original = self._validate(p)
        return self._insert_between(e, original.prev, original)

    def add_after(self, p, e):
        """
        Insert element e into list after Position p and return new Position.
        """

        original = self._validate(p)
        return self._insert_between(e, original, original.next)

    def delete(self, p):
        """
        Remove and return the element at Position p.
        """

        original = self._validate(p)
        return self._delete_node(original)                                      # inherited method returns element

    def replace(self, p, e):
        """
        Replace the element at Position p with e.
        Return the element formerly at Position p.
        """
        original = self._validate(p)
        old_value = original.element                                            # temporarily store old element
        original._element = e                                                   # replace with new element
        return old_value                                                        # return the old element value

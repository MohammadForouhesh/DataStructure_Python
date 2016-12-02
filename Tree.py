from abc import ABCmeta, abstractmethod


class Tree(metaclass=ABCmeta):
    class Node:
        __slots__ = 'data', 'leftChild', 'rightChild'

        def __init__(self, data, leftChild, rightChild):
            self.data = data
            self.leftChild = leftChild
            self.rightChild = rightChild

    def __init__(self):
        self.root = self.Node(None, None, None)
        self.size = 0

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0
    
    @abstractmethod
    def append(self, element)
        

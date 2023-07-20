class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def traverse(self):
        yield self.value
        if self.left:
            yield from self.left.traverse()
        if self.right:
            yield from self.right.traverse()


node_1 = Node(value=1, left=Node(12), right=Node(3))
node_5 = Node(value=5, left=node_1, right=Node(6))

node_8 = Node(value=8, left=Node(2))
node_7 = Node(value=7, left=Node(9), right=node_8)

node_11 = Node(value=11, left=node_5, right=node_7)

assert list(node_11.traverse()) == [11, 5, 1, 12, 3, 6, 7, 9, 8, 2]

assert list(node_1.traverse()) == [1, 12, 3]

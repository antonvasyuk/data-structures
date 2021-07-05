class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
                self.left.parent = self
                return self.left
            else:
                return self.left.insert(value)
        if value > self.value:
            if self.right is None:
                self.right = Node(value)
                self.right.parent = self
                return self.right
            else:
                return self.right.insert(value)

    def height(self):
        if self.left is None and self.right is None:
            return 1
        if self.left is None:
            return self.right.height() + 1
        if self.right is None:
            return self.left.height() + 1
        return max(self.left.height(), self.right.height()) + 1

    def distance(self, node, result=0):
        result += 1
        if self.value == node.value:
            return result
        if self.value > node.value:
            return self.left.distance(node, result)
        if self.value < node.value:
            return self.right.distance(node, result)
    
    def maximum(self):
        if self.right is not None:
            return self.right.maximum()
        return self.value
    
    def second_maximum(self):
        if self.right is not None:
            return self.right.second_maximum()
        if self.left is not None:
            return self.left.maximum()
        return self.parent.value
    
    def print_tree(self):
        if self.left is not None:
            self.left.print_tree()
        print(self.value)
        if self.right is not None:
            self.right.print_tree()
    
    def print_leafs(self):
        if self.left is not None:
            self.left.print_leafs()
        if self.left is None and self.right is None:
            print(self.value)
        if self.right is not None:
            self.right.print_leafs()
    
    def leafs_sum(self):
        result = 0
        if self.left is not None:
            result += self.left.leafs_sum()
        if self.right is not None:
            result += self.right.leafs_sum()
        if self.left is None and self.right is None:
            return self.value
        return result
    
    def is_AVL(self):
        if self.left is None and self.right is None:
            return True
        if self.left is None and self.right is not None and self.right.height() > 1:
            return False
        if self.right is None and self.left is not None and self.left.height() > 1:
            return False
        if self.left is not None and self.right is not None and abs(self.left.height() - self.right.height()) > 1:
            return False
        if self.left is not None and not self.left.is_AVL():
            return False
        if self.right is not None and not self.right.is_AVL():
            return False
        return True


nodes = list(map(int, input().split()))

for i in range(len(nodes)):
    if i == 0:
        tree = Node(nodes[i])
    else:
        tree.insert(nodes[i])

class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:
            if new_node < self.root:
                self.left_child = BinaryTree(new_node)
            else:
                print('Left child bigger or equal: right child, root, left child. Not insert!')
        else:
            if self.get_left_child().get_root_val() > new_node or self.get_right_child().get_root_val() > \
                    new_node > self.root:
                tree_obj = BinaryTree(new_node)
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
            else:
                print('Left child bigger or equal: right child, root, left child. Not insert!')

    def insert_right(self, new_node):
        if self.right_child is None:
            if new_node > self.root:
                self.right_child = BinaryTree(new_node)
            else:
                print('Right child smaller or equal: left child, root, right child. Not insert!')
        else:
            if self.get_right_child().get_root_val() < new_node or self.get_left_child().get_root_val() < \
                    new_node < self.root:
                tree_obj = BinaryTree(new_node)
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
            else:
                print('Right child smaller or equal: left child, root, right child. Not insert!')

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.root = obj

    def get_root_val(self):
        return self.root


root = BinaryTree(5)
print(root.get_root_val())
print(root.get_left_child())
print(root.get_right_child())
root.insert_left(5)
root.insert_left(6)
root.insert_left(4)
print('Left child value:', root.get_left_child().get_root_val())
root.insert_right(5)
root.insert_right(4)
root.insert_right(6)
print('Right child value:', root.get_right_child().get_root_val())
root.insert_right(6)
root.insert_right(4)
root.insert_right(5)
root.insert_right(3)
root.insert_right(7)
print('Right child value:', root.get_right_child().get_root_val())
root.insert_left(4)
root.insert_left(7)
root.insert_left(5)
root.insert_left(8)
root.insert_left(3)
print('Left child value:', root.get_left_child().get_root_val())

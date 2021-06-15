# 3/2021

# class Node:
#     def __init__(self, value, left_son=None, right_son=None):
#         self.value = value
#         self.left_son = left_son
#         self.right_son = right_son

#     def get_left(self):
#         return self.left_son

#     def get_right(self):
#         return self.right_son

#     def get_value(self):
#         return self.value

#     def set_value(self, value):
#         self.value = value


# right_leaf_left_son = Node(6)
# left_leaf_left_son = Node(1)
# right = Node(10)
# left = Node(3, left_leaf_left_son, right_leaf_left_son)
# root = Node(8, left, right)


def sum_tree(node):
    if node.get_left() is None and node.get_right() is None:
        return node.get_value()

    tree_from_node = sum_tree(node.get_left())
    tree_from_node += node.get_value() + sum_tree(node.get_right())
    node.set_value(tree_from_node)
    return node.get_value()


def sum_paths_to_leaves_helper(node, sum_path=0):
    """
    this is an helper function for sum_paths_to_leaves function.
    it will sum the nodes from the path of the leaves.
    :param node: node object
    :param sum_path: summed path
    :return:
    """
    if node.get_left() is None and node.get_right() is None:
        node.set_value(sum_path + node.get_value())
        return None

    sum_paths_to_leaves_helper(node.get_left(), sum_path + node.get_value())
    sum_paths_to_leaves_helper(node.get_right(), sum_path + node.get_value())


def sum_paths_to_leaves(node):
    sum_paths_to_leaves_helper(node)
    return None


def dont_run_twice(func):
    def wrapper(*args, **kwargs):
        if (args, kwargs) == wrapper.prev_args:
            return None
        wrapper.prev_args = args, kwargs
        return func()

    wrapper.prev_args = None
    return wrapper


@dont_run_twice
def test(*args):
    msg = "Hello"
    print(msg)


def iter_list_from(lst, ind):
    if len(lst) == ind:
        return
    yield lst[ind]
    yield from iter_list_from(lst, ind + 1)


if __name__ == '__main__':
    pass

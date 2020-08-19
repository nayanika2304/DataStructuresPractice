'''
Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree.
'''


def find_first_common_ancestor(n1, n2, root):
    # find node where nodes are on left and right side
    n1_on_left = node_in_tree(n1, root.left)
    n2_on_left = node_in_tree(n2, root.left)

    if n1_on_left ^ n2_on_left:
        return root
    else:
        if n1_on_left:
            return find_first_common_ancestor(n1, n2, root.left)
        else:
            return find_first_common_ancestor(n1, n2, root.right)


def node_in_tree(target, node):
    if not node:
        return False

    if target == node:
        return True
    else:
        return (
            node_in_tree(target, node.left) or node_in_tree(target, node.right)
        )


class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
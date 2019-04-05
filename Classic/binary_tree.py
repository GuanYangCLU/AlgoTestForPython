class LinkedListNode:
    def __init__(self, next=None, node=None):
        self.next = next
        self.node = node

    @classmethod
    def get_lst(self, head):
        s = ''
        head = head.next
        while head:
            s += '{} -> '.format(head.node.val)
            head = head.next
        return s[:-3]


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value


class BinaryTree:
    def __init__(self, lst):
        self.root = BinaryTree.build_tree(lst)

    @classmethod
    def build_tree(cls, lst):
        root = Node(lst.pop(0))
        row = [root]
        while lst:
            tmp_row = []
            for node in row:
                if lst:
                    node.left = Node(lst.pop(0))
                    tmp_row.append(node.left)
                if lst:
                    node.right = Node(lst.pop(0))
                    tmp_row.append(node.right)
            row = tmp_row
        return root

    def lst_linkedList_each_row(self):
        pass

    def _helper_linked(self, root):
        pass

    def find_common_acestor(self, a, b):
        pass


if __name__ == '__main__':
    """
        0
    1       2
3   4       5   6
    """
    lst = [i for i in range(7)]
    tree = BinaryTree(lst)
    # print(tree.root.val)
    # print(tree.root.left.val)
    # print(tree.root.right.val)
    # print(tree.root.left.left.val)
    # print(tree.root.left.right.val)
    # print(tree.root.right.left.val)

    for head in tree.lst_linkedList_each_row():
        print(LinkedListNode.get_lst(head))

    print(BinaryTree.find_common_acestor(
                                        tree.root,
                                        tree.root.left,
                                        tree.root.right
                                        ).val)
    print(BinaryTree.find_common_acestor(
                                        tree.root,
                                        tree.root.left.left,
                                        tree.root.left.right
                                        ).val)
    print(BinaryTree.find_common_acestor(
                                        tree.root,
                                        tree.root.left.right,
                                        tree.root.left.left
                                        ).val)

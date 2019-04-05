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
        container = [] #存储每一大轮得到的linklist，以head为头，后面靠next自然可以找到
        row = [self.root]
        while row is not None:  #第一层循环，如果上一轮的tmprow不为空说明还有下一层，继续执行
            tmp_row = [] #每次存储这一层的child节点
            head = LinkedListNode() #不要搞错ll和bitree的Node，特征是一个有next，一个有left，right*************           
            container.append(head)
            for node in row: #第二层循环，为当层所有child节点组成的row，塞入linklist后对该节点检测有无child，有则塞入临时row
                head.next = LinkedListNode(node) #把bitree的“值”塞进linklist的node，并指向下一个
                head = head.next
                for child in [node.left, node.right]: #第三层循环，判断有无child并塞入
                    tmp_row.append(child)
            row = tmp_row #当层的每个节点都塞入linklist后，下一层的child节点也已经塞完，交给第一层循环继续判断是否可以向下一层执行

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

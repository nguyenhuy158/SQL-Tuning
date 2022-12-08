class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(leaf=True)
        self.degree = t

    # Insert node
    def insert(self, k):
        x = self.root
        while x.leaf != True:
            # Find the child of x that is going to be traversed next. Let the child be y.


def main():
    degree = 3

    B = BTree(degree)

    # a = [8, 9, 10, 11, 15, 20, 17]
    a = [8, 9, 10]
    for i in range(len(a)):
        B.insert(a[i])

    # B.print_tree(B.root)

    # print('\nsearch 17: \n')
    # if B.search_key(17) is not None:
    #     print("\nFound")
    # else:
    #     print("\nNot Found")


if __name__ == '__main__':
    main()

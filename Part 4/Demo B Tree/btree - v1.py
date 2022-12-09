class BTreeNode:

    def __init__(self, isLeaf=True):
        self.isLeaf = isLeaf
        self.key = list()
        self.child = list()


class BTree:
    root = None
    m = 0

    def __init__(self, m):
        self.m = m

    def insert(self, key):
        if (self.root == None):
            self.root = BTreeNode()
            self.root.key.append(key)
            return

        current = self.root
        if self.insert_key_to_node(currentNode=current, key=key):
            return

        # not leaf
        while (current.isLeaf == False):
            # v1.0
            # isFlag = False
            # for i in range(len(current.key)):
            #     if key < current.key[i]:
            #         current = current.child[i]
            #         isFlag = True
            #         break
            # if isFlag:
            #     break
            # # get last child
            # current = current.child[-1]
            # break
            # v2.0
            isFlag = False
            for i in range(len(current.key)):
                if key < current.key[i]:
                    current = current.child[i]
                    isFlag = True
                    break
            if isFlag:
                continue
            current = current.child[-1]

        self.insert_key_to_node(currentNode=current, key=key)

    def insert_key_to_node(self, currentNode, key):
        if (currentNode.isLeaf):
            currentNode.key.append(key)
            currentNode.key.sort()

            if len(currentNode.key) < self.m:
                return True

            # put up
            keyLeft = currentNode.key[: self.m//2]
            keyRight = currentNode.key[self.m//2+1:]
            nodeLeft = BTreeNode()
            nodeLeft.key.extend(keyLeft)
            nodeRight = BTreeNode()
            nodeRight.key.extend(keyRight)

            if self.get_parent_node(self.root, currentNode) == None:
                newRootNode = BTreeNode(isLeaf=False)
                newRootNode.key.append(currentNode.key[self.m//2])
                newRootNode.child.append(nodeLeft)
                newRootNode.child.append(nodeRight)

                self.root = newRootNode
                return True
            else:
                tempRootNode = self.get_parent_node(self.root, currentNode)
                tempRootNode.key.append(currentNode.key[self.m//2])
                tempRootNode.child.remove(currentNode)
                tempRootNode.child.append(nodeLeft)
                tempRootNode.child.append(nodeRight)

                isFlag = False
                newRootNode = None
                if len(tempRootNode.key) == self.m:
                    nodeLeft = BTreeNode(isLeaf=False)
                    nodeRight = BTreeNode(isLeaf=False)
                    keyLeft = tempRootNode.key[: self.m//2]
                    keyRight = tempRootNode.key[self.m//2+1:]
                    nodeLeft.key.extend(keyLeft)
                    nodeRight.key.extend(keyRight)
                    childLeft = tempRootNode.child[: self.m//2+1]
                    childRight = tempRootNode.child[self.m//2+1:]
                    nodeLeft.child.extend(childLeft)
                    nodeRight.child.extend(childRight)

                    newRootNode = BTreeNode(isLeaf=False)
                    newRootNode.key.append(tempRootNode.key[self.m//2])
                    newRootNode.child.append(nodeLeft)
                    newRootNode.child.append(nodeRight)

                    if self.get_parent_node(self.root, tempRootNode) == None:
                        self.root = newRootNode
                    else:
                        resultNode = self.get_parent_node(
                            self.root, tempRootNode)
                        resultNode = newRootNode

        return False

    def get_parent_node(self, currentNode, childNode):
        # if currentNode == childNode:
        #     return None
        tempNode = None
        for e in currentNode.child:
            if e == childNode:
                tempNode = currentNode
                break
            else:
                self.get_parent_node(e, childNode=childNode)
        return tempNode

    def printTree(self):
        self.print(node=self.root)

    def print(self, node):
        # if (node.isLeaf):
        #     for key in node.key:
        #         print(f'{key}')

        l = len(node.child)//2
        if len(node.child) % 2 == 1:
            l += 1
        for i in range(l):
            self.print(node.child[i])
        for key in node.key:
            print(f'{key}')
        for i in range(l, len(node.child)):
            self.print(node.child[i])


def main():
    btree = BTree(3)
    btree.insert(1)
    btree.insert(2)
    btree.insert(3)
    btree.insert(4)
    btree.insert(5)
    btree.insert(6)
    btree.insert(0)
    btree.insert(7)
    btree.insert(8)
    btree.insert(9)
    # btree.insert(10)
    btree.printTree()
    pass


if __name__ == '__main__':
    main()

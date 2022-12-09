import random
import igraph
from tkinter import *
from tkinter import ttk


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

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, currentNode: BTreeNode, key):

        for keyIndex in range(len(currentNode.key)):
            tempKey = currentNode.key[keyIndex]
            if tempKey == key:
                return True
            elif key < tempKey and not currentNode.isLeaf:
                child = currentNode.child[keyIndex]
                return self._search(child, key)

        if currentNode.isLeaf:
            return False

        child = currentNode.child[len(currentNode.key)]
        return self._search(child, key)

    def insert(self, key):
        if self.root == None:
            self.root = BTreeNode()
            self.root.key.append(key)
            return

        current = self.root
        if self.insert_key_to_node(currentNode=current, key=key):
            return

        # not leaf
        while current.isLeaf == False:
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

    def insert_key_to_node(self, currentNode: BTreeNode, key):
        if currentNode.isLeaf:
            currentNode.key.append(key)
            currentNode.key.sort()

            if len(currentNode.key) < self.m:
                return True

            # put up
            keyLeft = currentNode.key[: self.m // 2]
            keyRight = currentNode.key[self.m // 2 + 1 :]
            nodeLeft = BTreeNode()
            nodeLeft.key.extend(keyLeft)
            nodeRight = BTreeNode()
            nodeRight.key.extend(keyRight)

            if self.get_parent_node(self.root, None, currentNode) == None:
                newRootNode = BTreeNode(isLeaf=False)
                newRootNode.key.append(currentNode.key[self.m // 2])
                newRootNode.child.append(nodeLeft)
                newRootNode.child.append(nodeRight)

                self.root = newRootNode
                return True
            else:
                tempRootNode = self.get_parent_node(self.root, None, currentNode)
                tempRootNode.key.append(currentNode.key[self.m // 2])
                tempRootNode.key.sort()
                index = tempRootNode.child.index(currentNode)
                tempRootNode.child.remove(currentNode)
                tempRootNode.child.insert(index, nodeRight)
                tempRootNode.child.insert(index, nodeLeft)
                # tempRootNode.child.append(nodeLeft)
                # tempRootNode.child.append(nodeRight)

                isFlag = False
                newRootNode = None
                while len(tempRootNode.key) == self.m:
                    nodeLeft = BTreeNode(isLeaf=False)
                    nodeRight = BTreeNode(isLeaf=False)
                    keyLeft = tempRootNode.key[: self.m // 2]
                    keyRight = tempRootNode.key[self.m // 2 + 1 :]
                    nodeLeft.key.extend(keyLeft)
                    nodeRight.key.extend(keyRight)
                    childLeft = tempRootNode.child[: self.m // 2 + 1]
                    childRight = tempRootNode.child[self.m // 2 + 1 :]
                    nodeLeft.child.extend(childLeft)
                    nodeRight.child.extend(childRight)

                    if self.get_parent_node(self.root, None, tempRootNode) == None:
                        newRootNode = BTreeNode(isLeaf=False)
                        newRootNode.key.append(tempRootNode.key[self.m // 2])
                        newRootNode.child.append(nodeLeft)
                        newRootNode.child.append(nodeRight)
                        self.root = newRootNode
                    else:
                        newRootNode = self.get_parent_node(
                            self.root, None, tempRootNode
                        )
                        newRootNode.key.append(tempRootNode.key[self.m // 2])
                        newRootNode.key.sort()
                        newRootNode.child.remove(tempRootNode)
                        newRootNode.child.append(nodeLeft)
                        newRootNode.child.append(nodeRight)
                        # resultNode = self.get_parent_node(
                        #     self.root, None, tempRootNode)
                        # resultNode = newRootNode

                    tempRootNode = newRootNode

        return False

    def get_parent_node(
        self, currentNode: BTreeNode, parentNode: BTreeNode, childNode: BTreeNode
    ):
        if currentNode == childNode:
            return parentNode
        node = None
        for child in currentNode.child:
            node = self.get_parent_node(child, currentNode, childNode)
            if node != None:
                break

        return node

    def printTree(self):
        self.print(node=self.root)

    def print(self, node: BTreeNode):
        l = len(node.child) // 2
        if len(node.child) % 2 == 1:
            l += 1
        for i in range(l):
            self.print(node.child[i])
        for key in node.key:
            print(f"{key}")
        for i in range(l, len(node.child)):
            self.print(node.child[i])

    def buildTree(
        self,
        currentNode: BTreeNode,
        treeView: ttk.Treeview,
        parent="",
        iid="item",
        index_iid=1,
    ):
        text = ", ".join(str(key) for key in currentNode.key)
        print(text, parent, index_iid)

        treeView.insert(
            parent="", index="end", iid=str(text + str(index_iid)), text=text
        )
        if parent != "":
            treeView.move(item=str(text + str(index_iid)), parent=parent, index="end")

        if not currentNode.isLeaf:
            index = 0
            for child in currentNode.child:
                index += 1
                self.buildTree(
                    child,
                    treeView,
                    parent=str(text + str(index_iid)),
                    index_iid=index_iid + index,
                )

        else:
            pass

    def mainGui(self):
        app = Tk()
        app.title("Application of B Tree")
        ttk.Label(app, text="B Tree").pack()
        treeView = ttk.Treeview(app)
        treeView.pack()
        self.buildTree(self.root, treeView)
        app.mainloop()


def main():
    btree = BTree(3)
    keys = [18, 57, 45, 77, 55, 68, 70, 20, 48, 86, 21, 43, 62, 87, 69]
    for key in keys:
        btree.insert(key=key)
    btree.printTree()

    random.seed(1508)
    for key in keys:
        num = key + random.randint(0, 1)
        print(f"{num} is {True if btree.search(num) else False} ")

    btree.mainGui()
    pass


if __name__ == "__main__":
    main()

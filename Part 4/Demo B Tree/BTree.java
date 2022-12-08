package Backup;
// Inserting a key on a B-tree in Java 

public class BTree {

    private int T;

    // Node Creation
    public class Node {
        int n;
        int key[] = new int[T - 1];
        Node child[] = new Node[T];
        boolean leaf = true;
    }

    public BTree(int t) {
        T = t;
        root = new Node();
        root.n = 0;
        root.leaf = true;
    }

    private Node root;

    // split
    private void split(Node x, int pos, Node y) {

    }

    // insert key
    public void insert(final int key) {
        if (root.leaf) {
            for (int i = root.n - 1; i >= 0; i--) {
                root.key[i + 1] = root.key[i];
            }
            root.key[i + 1] = key;
            root.n += 1;
        } else {
            for (int i = 0; i < root.n; i++) {
                if (key )
            }
        }
    }

    public static void main(String[] args) {
        BTree b = new BTree(3);
        b.insert(8);
        b.insert(9);
        b.insert(10);
        b.insert(11);
        b.insert(15);
        b.insert(20);
        b.insert(17);

    }
}
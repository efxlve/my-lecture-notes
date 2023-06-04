class Node {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

// Binary Search Tree
class BST {
    constructor() {
        this.root = null;
    }

    // Insert a node
    insert(value) {
        const newNode = new Node(value);
        if (!this.root) {
            this.root = newNode;
            return this;
        }

        let current = this.root;
        while (true) {
            if (value === current.value) return undefined;
            if (value < current.value) {
                if (!current.left) {
                    current.left = newNode;
                    return this;
                }
                current = current.left;
            } else {
                if (!current.right) {
                    current.right = newNode;
                    return this;
                }
                current = current.right;
            }
        }
    }

    // Lookup a node
    lookup(value) {
        if (!this.root) return false;

        let current = this.root;
        while (current) {
            if (value === current.value) return current;
            if (value < current.value) current = current.left;
            else current = current.right;
        }
        return false;
    }

    // Remove a node
    remove(value) {
        if (!this.root) return false;

        let current = this.root;
        let parent = null;
        while (current) {
            if (value === current.value) {
                // Option 1: No right child
                if (!current.right) {
                    if (!parent) this.root = current.left;
                    else {
                        if (current.value < parent.value) {
                            parent.left = current.left;
                        } else if (current.value > parent.value) {
                            parent.right = current.left;
                        }
                    }
                }
                // Option 2: Right child which doesn't have a left child
                else if (!current.right.left) {
                    current.right.left = current.left;
                    if (!parent) this.root = current.right;
                    else {
                        if (current.value < parent.value) {
                            parent.left = current.right;
                        } else if (current.value > parent.value) {
                            parent.right = current.right;
                        }
                    }
                }
                // Option 3: Right child that has a left child
                else {
                    // Find the Right child's left most child
                    let leftmost = current.right.left;
                    let leftmostParent = current.right;
                    while (leftmost.left) {
                        leftmostParent = leftmost;
                        leftmost = leftmost.left;
                    }

                    // Parent's left subtree is now leftmost's right subtree
                    leftmostParent.left = leftmost.right;
                    leftmost.left = current.left;
                    leftmost.right = current.right;

                    if (!parent) this.root = leftmost;
                    else {
                        if (current.value < parent.value) {
                            parent.left = leftmost;
                        } else if (current.value > parent.value) {
                            parent.right = leftmost;
                        }
                    }
                }
                return true;
            } else if (value < current.value) {
                parent = current;
                current = current.left;
            } else if (value > current.value) {
                parent = current;
                current = current.right;
            }
        }
        return false;
    }
}

const tree = new BST();
tree.insert(9); // root
tree.insert(4); // left
tree.insert(6); // right
tree.insert(20); // right
tree.insert(170); // right
tree.insert(15); // right
tree.insert(1); // right
tree.lookup(170);  // 170
tree.lookup(171);  // false
tree.remove(170);  // true
tree.remove(171);  // false
JSON.stringify(traverse(tree.root));


function traverse(node) {
    const tree = { value: node.value };
    tree.left = node.left === null ? null : traverse(node.left);
    tree.right = node.right === null ? null : traverse(node.right);
    return tree;
}


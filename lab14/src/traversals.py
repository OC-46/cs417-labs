"""
Tree Traversals — Lab 14

Implement four traversal algorithms for a Binary Search Tree.
The BST module is provided — don't modify bst.py.
"""

import collections

from bst import BST


def build_sample_tree():
    """Build the sample BST from the lab diagram.

    Inserts: 15, 9, 21, 4, 12, 18, 25, 2, 7

             15
            /  \\
           9    21
          / \\   / \\
         4  12 18  25
        / \\
       2   7
    """
    tree = BST()
    for value in [15, 9, 21, 4, 12, 18, 25, 2, 7]:
        tree.insert(value)
    return tree


# ── Task 1: Explore the BST ─────────────────────────────────────────

def explore():
    """Explore the provided BST module.

    TODO:
    - Build the sample tree using build_sample_tree()
    - Print the tree using its display() method
    - Search for the values 12, 20, and 25
      - For each, print whether it was found
        e.g., "Search 12: Found" or "Search 20: Not found"
    - Print the total number of nodes using the size() method
      e.g., "Tree has 9 nodes"
    """
    tree = build_sample_tree()
    tree.display()
    print(f"Search 12: {'Found' if tree.search(12) else 'Not found'}")
    print(f"Search 20: {'Found' if tree.search(20) else 'Not found'}")
    print(f"Search 25: {'Found' if tree.search(25) else 'Not found'}")
    print(f"Tree has {tree.size()} nodes")


# ── Task 2: Inorder Traversal (Left → Self → Right) ─────────────────

def inorder(node):
    """Return a list of values from an inorder traversal.

    Visit the left subtree, then the current node, then the right subtree.
    Returns an empty list if node is None.

    TODO: implement this
    """
    inorder_list = []
    if node is None:
        return []
    else:
        inorder_list.extend(inorder(node.left))
        inorder_list.append(node.value)
        inorder_list.extend(inorder(node.right))
        return inorder_list

# ── Task 3: Preorder Traversal (Self → Left → Right) ────────────────

def preorder(node):
    """Return a list of values from a preorder traversal.

    Visit the current node, then the left subtree, then the right subtree.
    Returns an empty list if node is None.

    TODO: implement this
    """
    preorder_list = []
    if node is None:
        return []
    else:
        preorder_list.append(node.value)
        preorder_list.extend(preorder(node.left))
        preorder_list.extend(preorder(node.right))
        return preorder_list


# ── Task 4: Postorder Traversal (Left → Right → Self) ───────────────

def postorder(node):
    """Return a list of values from a postorder traversal.

    Visit the left subtree, then the right subtree, then the current node.
    Returns an empty list if node is None.

    TODO: implement this
    """
    postorder_list = []
    if node is None:
        return []
    else:
        postorder_list.extend(postorder(node.left))
        postorder_list.extend(postorder(node.right))
        postorder_list.append(node.value)
        return postorder_list


# ── Task 5: Level-Order Traversal (BFS) ─────────────────────────────

def levelorder(node):
    """Return a list of values from a level-order (BFS) traversal.

    Visit nodes level by level, from top to bottom, left to right.
    Uses a queue — not recursion.
    Returns an empty list if node is None.

    Hint: collections.deque works great as a queue.
      - append() adds to the back
      - popleft() removes from the front

    TODO: implement this
    """
    if node is None:
        return []
    list = []
    queue = collections.deque([node])
    while queue:
        current = queue.popleft()
        list.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return list



# ── Main ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    explore()

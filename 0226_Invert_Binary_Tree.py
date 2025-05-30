# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# Example usage:
if __name__ == "__main__":
    # Example tree:
    #     4
    #    / \
    #   2   7
    #  / \ / \
    # 1  3 6  9
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(7)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(9)

    sol = Solution()
    inverted_tree = sol.invertTree(tree)

    # Helper function to print the tree in-order
    def inorder(root):
        if not root:
            return
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

    inorder(inverted_tree)  # Output should be the in-order traversal of the inverted tree

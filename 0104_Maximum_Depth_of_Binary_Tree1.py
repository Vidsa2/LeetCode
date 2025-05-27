# using breadth-first search (BFS) to find the maximum depth of a binary tree
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = 0
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

if __name__ == "__main__":
    # Example tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    sol = Solution()
    print(sol.maxDepth(root))  # Output: 3

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack=[[p,q]]
        while stack:
            node1,node2 = stack.pop()
            if not node1 and not node2:
                continue
            elif not node1 or not node2:
                return False
            elif node1.val != node2.val :
                return False
            stack.append([node1.left,node2.left])
            stack.append([node1.right,node2.right])
        return True

# Example usage:
if __name__ == "__main__":
    # Tree 1
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    # Tree 2
    q = TreeNode(1, TreeNode(2), TreeNode(3))

    sol = Solution()
    print(sol.isSameTree(p, q))  # Output: True

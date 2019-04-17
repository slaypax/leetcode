# https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Your runtime beats 99.03 % of python3 submissions.
# Runtime: 40 ms

class Solution(object):
    def isSymmetric(self, root):
        
        def isMirror(root1, root2):
            if root1 is None and root2 is None:
                return True 

            if (root1 is not None and root2 is not None):
                if root1.val == root2.val:
                    return (isMirror(root1.left, root2.right)and isMirror(root1.right, root2.left))
            return False

        return isMirror(root, root)        
        """
        :type root: TreeNode
        :rtype: bool
        """
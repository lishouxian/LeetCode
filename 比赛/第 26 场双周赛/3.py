# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        global res
        res = 0
        def backtrack(root):
            global res
            res += 1
            if root.left:
                
                if root.left.val < root.val:
                    res -= 1
                    root.left.val = root.val
                backtrack(root.left)


            if root.right:
                
                if root.right.val < root.val:
                    res -= 1
                    root.right.val = root.val
                backtrack(root.right)

                
        backtrack(root)

        return res

a = TreeNode(9)
b = TreeNode(2)
c = TreeNode(3)
b.right = TreeNode(5)
c.right = TreeNode(4)
a.left = b
a.right = c


mm = Solution()
print(mm.goodNodes(b))




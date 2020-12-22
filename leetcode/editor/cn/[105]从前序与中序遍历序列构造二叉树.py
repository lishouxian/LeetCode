# 根据一棵树的前序遍历与中序遍历构造二叉树。 
# 
#  注意: 
# 你可以假设树中没有重复的元素。 
# 
#  例如，给出 
# 
#  前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7] 
# 
#  返回如下的二叉树： 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7 
#  Related Topics 树 深度优先搜索 数组 
#  👍 784 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder: return None
        a = TreeNode(preorder[0])
        index = 0
        while inorder[index] != preorder[0]:
            index += 1
        a.left = self.buildTree(preorder[1:index + 1], inorder[:index])
        a.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return a


# leetcode submit region end(Prohibit modification and deletion)

a = Solution()

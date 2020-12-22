# 给定一个二叉树，找出其最大深度。 
# 
#  二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。 
# 
#  说明: 叶子节点是指没有子节点的节点。 
# 
#  示例： 
# 给定二叉树 [3,9,20,null,null,15,7]， 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7 
# 
#  返回它的最大深度 3 。 
#  Related Topics 树 深度优先搜索 递归 
#  👍 753 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        if not root: return 0
        res = 0
        nodes = [root]
        while nodes:
            res += 1
            temp = []
            for node in nodes:
                if node.left == node.right is None:
                    pass
                elif node.left is None:
                    temp.append(node.right)
                elif node.right is None:
                    temp.append(node.left)
                else:
                    temp.append(node.left)
                    temp.append(node.right)
            nodes = temp
        return res
# leetcode submit region end(Prohibit modification and deletion)



a = Solution()

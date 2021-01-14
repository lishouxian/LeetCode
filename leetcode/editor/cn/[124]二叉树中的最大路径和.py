# 给你一个二叉树的根节点 root ，返回其最大路径和。 
# 
#  本题中，路径被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。该路径 至少包含一个 节点，且不一定经过根节点。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [1,2,3]
# 输出：6
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [-10,9,20,null,null,15,7]
# 输出：42
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目范围是 [1, 3 * 104] 
#  -1000 <= Node.val <= 1000 
#  
#  Related Topics 树 深度优先搜索 递归 
#  👍 845 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxGain1 = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        maxGain = float("-inf")
        def maxGain(node):
            if not node: return 0
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)
            priceNewpath = node.val + leftGain + rightGain
            self.maxGain1 = max(self.maxGain1, priceNewpath)
            return node.val + max(leftGain, rightGain)
        maxGain(root)
        return self.maxGain1

# leetcode submit region end(Prohibit modification and deletion)

        pass

a = Solution()

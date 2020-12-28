# 给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。 
# 
#  例如： 
# 给定二叉树 [3,9,20,null,null,15,7], 
# 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回锯齿形层序遍历如下： 
# 
#  
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
#  
#  Related Topics 栈 树 广度优先搜索 
#  👍 337 👎 0

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root:return []
        res = []
        nodes = [root]
        isOk = False
        while nodes:
            tempres = []
            tempnodes = []
            for node in nodes:
                tempres.append(node.val)
                if node.left: tempnodes.append(node.left)
                if node.right:tempnodes.append(node.right)
            nodes = tempnodes
            if isOk:
                tempres.reverse()
                isOk = False
            else:
                isOk = True
            res.append(tempres)
        return res


# leetcode submit region end(Prohibit modification and deletion)



a = Solution()

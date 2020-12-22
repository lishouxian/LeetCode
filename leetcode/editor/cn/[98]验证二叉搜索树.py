# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。 
# 
#  假设一个二叉搜索树具有如下特征： 
# 
#  
#  节点的左子树只包含小于当前节点的数。 
#  节点的右子树只包含大于当前节点的数。 
#  所有左子树和右子树自身必须也是二叉搜索树。 
#  
# 
#  示例 1: 
# 
#  输入:
#     2
#    / \
#   1   3
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。
#  
#  Related Topics 树 深度优先搜索 递归 
#  👍 852 👎 0
from functools import lru_cache


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        @lru_cache(None)
        def lr(head):
            if head is None: return None, None, True
            else:
                a,b,m = lr(head.left)
                c,d,n = lr(head.right)
                if a == c is None:
                    return head.val, head.val, True
                if a is None:
                    return min(c,head.val), max(d,head.val),head.val < c and n
                if c is None:
                    return min(a,head.val), max(b,head.val), b < head.val and m
                return min(a,c,head.val), max(b,d,head.val), b < head.val < c and m and n
        _,_,res = lr(root)
        return res

# leetcode submit region end(Prohibit modification and deletion)

        pass

a = Solution()

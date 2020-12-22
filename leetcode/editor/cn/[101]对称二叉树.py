# 给定一个二叉树，检查它是否是镜像对称的。 
# 
#  
# 
#  例如，二叉树 [1,2,2,3,4,4,3] 是对称的。 
# 
#      1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#  
# 
#  
# 
#  但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的: 
# 
#      1
#    / \
#   2   2
#    \   \
#    3    3
#  
# 
#  
# 
#  进阶： 
# 
#  你可以运用递归和迭代两种方法解决这个问题吗？ 
#  Related Topics 树 深度优先搜索 广度优先搜索 
#  👍 1151 👎 0
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        nodes = [root]
        while nodes:
            temp = []
            for node in nodes:
                if node is None:
                    pass
                else:
                    temp.append(node.left)
                    temp.append(node.right)
            vals = [temp[i] and temp[i].val for i in range(len(temp))]
            if vals == vals.reverse():
                nodes = temp
            else:
                return False
        return True





        
# leetcode submit region end(Prohibit modification and deletion)

        pass

a = Solution()

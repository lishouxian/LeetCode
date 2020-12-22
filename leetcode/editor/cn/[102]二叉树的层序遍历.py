# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。 
# 
#  
# 
#  示例： 
# 二叉树：[3,9,20,null,null,15,7], 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回其层次遍历结果： 
# 
#  [
#   [3],
#   [9,20],
#   [15,7]
# ]
#  
#  Related Topics 树 广度优先搜索 
#  👍 718 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        nodes = [root]
        while nodes:
            res.append([nodes[i].val for i in range(len(nodes))])
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

        pass

a = Solution()

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        import copy
        global count
        count = 0
        save = [0] * 9
        def back(root, save):
            global count
            save[root.val-1] = save[root.val-1] ^ 1
            if (not root.left) and (not root.right):
                #print(save)
                if sum(save) <= 1:
                    count += 1
            else:
                save1 = copy.deepcopy(save)
                if root.left:back(root.left,save)
                if root.right:back(root.right,save1)
        back(root,save)
        return count
                
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(1)
e = TreeNode(3)
f = TreeNode(1)
g = TreeNode(1)
b.left = c
b.right = d
c.left = e
c.right = f
d.right = g

a = Solution()
print(a.pseudoPalindromicPaths(b))

# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？ 
# 
#  示例: 
# 
#  输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
# 
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3 
#  Related Topics 树 动态规划 
#  👍 916 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def numTrees(self, n: int) -> int:
        if n <= 1: return 1
        count = 0
        for i in range(n):
            count += self.numTrees(i) * self.numTrees(n - i - 1)
        return count


# leetcode submit region end(Prohibit modification and deletion)


a = Solution()
print(a.numTrees(10))

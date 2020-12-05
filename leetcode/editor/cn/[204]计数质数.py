# 统计所有小于非负整数 n 的质数的数量。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 10
# 输出：4
# 解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
#  
# 
#  示例 2： 
# 
#  输入：n = 0
# 输出：0
#  
# 
#  示例 3： 
# 
#  输入：n = 1
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 5 * 106 
#  
#  Related Topics 哈希表 数学 
#  👍 505 👎 0

# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
        temp = [True for i in range(n)]
        count = 2
        for i in range(2, n):
            if temp[i]:
                j = i
                while i * j < n:
                    if temp[i * j]:
                        temp[i * j] = False
                        count += 1
                    j += 1
        return n - count


# leetcode submit region end(Prohibit modification and deletion)

a = Solution()
print(a.countPrimes(10))

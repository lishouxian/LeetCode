# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。 
# 
#  示例 1: 
# 
#  输入: 2.00000, 10
# 输出: 1024.00000
#  
# 
#  示例 2: 
# 
#  输入: 2.10000, 3
# 输出: 9.26100
#  
# 
#  示例 3: 
# 
#  输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2-2 = 1/22 = 1/4 = 0.25 
# 
#  说明: 
# 
#  
#  -100.0 < x < 100.0 
#  n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。 
#  
#  Related Topics 数学 二分查找 
#  👍 565 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            ans = 1.0
            # 贡献的初始值为 x
            x_contribute = x
            # 在对 N 进行二进制拆分的同时计算答案
            while N > 0:
                if N % 2 == 1:
                    # 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                    ans *= x_contribute
                # 将贡献不断地平方
                x_contribute *= x_contribute
                # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
                N //= 2
            return ans

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

# leetcode submit region end(Prohibit modification and deletion)

        pass

a = Solution()

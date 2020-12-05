# 给你一个按升序排序的整数数组 num（可能包含重复数字），请你将它们分割成一个或多个子序列，其中每个子序列都由连续整数组成且长度至少为 3 。 
# 
#  如果可以完成上述分割，则返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  输入: [1,2,3,3,4,5]
# 输出: True
# 解释:
# 你可以分割出这样两个连续子序列 : 
# 1, 2, 3
# 3, 4, 5
#  
# 
#  
# 
#  示例 2： 
# 
#  输入: [1,2,3,3,4,4,5,5]
# 输出: True
# 解释:
# 你可以分割出这样两个连续子序列 : 
# 1, 2, 3, 4, 5
# 3, 4, 5
#  
# 
#  
# 
#  示例 3： 
# 
#  输入: [1,2,3,4,4,5]
# 输出: False
#  
# 
#  
# 
#  提示： 
# 
#  
#  输入的数组长度范围为 [1, 10000] 
#  
# 
#  
#  Related Topics 堆 贪心算法 
#  👍 149 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def isPossible(self, nums) -> bool:
        count_num = 0
        sum = collections.Counter(nums)
        count = len(nums)
        while count:
            for i in range(nums[0], nums[-1] + 1):
                if (sum[i] or 0) == 0:
                    i += 1
                elif (sum[i] or 0) > (sum[i + 1] or 0):
                    # 在当前结束
                    if count_num < 2:
                        return False
                    else:
                        sum[i] -= 1
                        count -= 1
                        count_num = 0
                        break
                elif sum[i] > 0:
                    sum[i] -= 1
                    count -= 1
                    count_num += 1
        return True


# leetcode submit region end(Prohibit modification and deletion)


a = Solution()
print(a.isPossible([1, 2, 3, 3, 4, 4, 5, 5, 6,7]))

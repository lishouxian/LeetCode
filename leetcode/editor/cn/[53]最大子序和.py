# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。 
# 
#  示例: 
# 
#  输入: [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#  
# 
#  进阶: 
# 
#  如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。 
#  Related Topics 数组 分治算法 动态规划 
#  👍 2691 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        l, r, count, res = 0, 0, 0, 0
        while r < len(nums):

            if nums[r] > 0:
                count += nums[r]
            else:
                if count + nums[r] < 0:
                    count = 0
                else:
                    count += nums[r]
            r += 1
            res = max(res, count)
        if res == 0 :return max(nums)
        return res

# leetcode submit region end(Prohibit modification and deletion)



a = Solution()
print(a.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
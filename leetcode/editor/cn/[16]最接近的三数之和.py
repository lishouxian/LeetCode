# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和
# 。假定每组输入只存在唯一答案。 
# 
#  
# 
#  示例： 
# 
#  输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= nums.length <= 10^3 
#  -10^3 <= nums[i] <= 10^3 
#  -10^4 <= target <= 10^4 
#  
#  Related Topics 数组 双指针 
#  👍 645 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSumClosest(self, nums, target):
        res = sum(nums[:2]) + nums[-1]
        nums.sort()
        for i in range(len(nums)-2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                if abs(temp - target) < abs(res - target):
                    res = temp
                if temp == target:
                    return target
                if temp > target:
                    r -= 1
                else:
                    l += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)


a = Solution()
print(a.threeSumClosest([-1,2,1,-4],1))

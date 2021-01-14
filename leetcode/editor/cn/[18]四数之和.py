# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c +
#  d 的值与 target 相等？找出所有满足条件且不重复的四元组。 
# 
#  注意： 
# 
#  答案中不可以包含重复的四元组。 
# 
#  示例： 
# 
#  给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
# 
# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
#  
#  Related Topics 数组 哈希表 双指针 
#  👍 714 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fourSum(self, nums, target: int):
        nums.sort()

        res = []
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                l, r = j + 1, len(nums) - 1
                while l < r:
                    base = nums[i] + nums[j] + nums[l] + nums[r] - target
                    if base > 0:
                        r -= 1
                    elif base < 0:
                        l += 1
                    elif base == 0:
                        if not res:
                            res.append([nums[i] , nums[j] , nums[l] , nums[r]])
                        elif nums[i] != res[-1][0] or nums[j] != res[-1][1] or nums[l] != res[-1][2]:
                            if (nums[i] == res[-1][0] and nums[j] == res[-1][1] and nums[l] < res[-1][2]) or \
                                    (nums[i] == res[-1][0] and nums[j] < res[-1][1]):
                                pass
                            else:
                                res.append([nums[i] , nums[j] , nums[l] , nums[r]])
                        r -= 1
                        l += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)

        pass

a = Solution()
print(a.fourSum([-5,-4,-3,-2,-1,0,0,1,2,3,4,5] ,0))

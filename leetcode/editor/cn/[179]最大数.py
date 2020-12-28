# 给定一组非负整数 nums，重新排列它们每个数字的顺序（每个数字不可拆分）使之组成一个最大的整数。 
# 
#  注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [10,2]
# 输出："210" 
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,30,34,5,9]
# 输出："9534330"
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1]
# 输出："1"
#  
# 
#  示例 4： 
# 
#  
# 输入：nums = [10]
# 输出："10"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 100 
#  0 <= nums[i] <= 109 
#  
#  Related Topics 排序 
#  👍 441 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestNumber(self, nums) -> str:
        save = [[] * 10]
        for i in range(len(nums)):
            print(nums[i][0])
            index = int(nums[i][0])
            save[index].append(nums[i])
        res = []

        for i in range(10):
            save[i].sort()
            save[i].reverse()
            res = res + save[i]
        return "".join(res)

# leetcode submit region end(Prohibit modification and deletion)

a = Solution()

print(a.largestNumber([3, 30, 34, 5, 9]))
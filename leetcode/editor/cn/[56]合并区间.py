# 给出一个区间的集合，请合并所有重叠的区间。 
# 
#  
# 
#  示例 1: 
# 
#  输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#  
# 
#  示例 2: 
# 
#  输入: intervals = [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。 
# 
#  注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。 
# 
#  
# 
#  提示： 
# 
#  
#  intervals[i][0] <= intervals[i][1] 
#  
#  Related Topics 排序 数组 
#  👍 719 👎 0



# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda a: a[0])
        left = right = -1
        res = []
        for a, b in intervals:
            if left == -1:
                left = a
                right = b
            elif right >= a:
                right = max(right,b)
            else:
                res.append([left, right])
                left = a
                right = b
        if right >= left : res.append([left, right])
        return res



# leetcode submit region end(Prohibit modification and deletion)


a = Solution()
print(a.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))

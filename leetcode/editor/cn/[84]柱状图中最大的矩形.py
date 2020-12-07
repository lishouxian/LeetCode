# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。 
# 
#  求在该柱状图中，能够勾勒出来的矩形的最大面积。 
# 
#  
# 
#  
# 
#  以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。 
# 
#  
# 
#  
# 
#  图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。 
# 
#  
# 
#  示例: 
# 
#  输入: [2,1,5,6,2,3]
# 输出: 10 
#  Related Topics 栈 数组 
#  👍 1044 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestRectangleArea(self, heights) -> int:
        stack = []
        hei = [0] + heights + [0]
        res = 0
        for i, h in enumerate(hei):
            while stack and h < hei[stack[-1]]:
                # 当前的h比栈顶元素小 即破坏了递增 要把栈顶一个一个弹出以维护递增栈递增的性质
                # i可能是多个柱子的右边界，要用while一个一个确认，看看是哪些柱子的右边界
                # 弹出栈顶元素 计算这个下标的柱子能组成的高度
                cur_stack = stack.pop()
                # 矩形面积 = 高度 x (右边界 - 左边界- 1)
                res = max(res, hei[cur_stack] * (i - stack[-1] - 1))
            stack.append(i)
        return res


        # leetcode submit region end(Prohibit modification and deletion)


a = Solution()
print(a.largestRectangleArea([2, 1, 2]))

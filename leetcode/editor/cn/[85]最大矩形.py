# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"]
# ,["1","0","0","1","0"]]
# 输出：6
# 解释：最大矩形如上图所示。
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = []
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：matrix = [["0"]]
# 输出：0
#  
# 
#  示例 4： 
# 
#  
# 输入：matrix = [["1"]]
# 输出：1
#  
# 
#  示例 5： 
# 
#  
# 输入：matrix = [["0","0"]]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  rows == matrix.length 
#  cols == matrix.length 
#  0 <= row, cols <= 200 
#  matrix[i][j] 为 '0' 或 '1' 
#  
#  Related Topics 栈 数组 哈希表 动态规划 
#  👍 667 👎 0


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


    def maximalRectangle(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    matrix[i][j] = 0
                elif i == 0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i-1][j] + 1
        return max([self.largestRectangleArea(matrix[i]) for i in range(len(matrix))] + [0])




# leetcode submit region end(Prohibit modification and deletion)



a = Solution()

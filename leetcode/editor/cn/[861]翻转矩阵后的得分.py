# 有一个二维矩阵 A 其中每个元素的值为 0 或 1 。 
# 
#  移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。 
# 
#  在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。 
# 
#  返回尽可能高的分数。 
# 
#  
# 
#  
#  
# 
#  示例： 
# 
#  输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# 输出：39
# 解释：
# 转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
# 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 20 
#  1 <= A[0].length <= 20 
#  A[i][j] 是 0 或 1 
#  
#  Related Topics 贪心算法 
#  👍 109 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def matrixScore(self, A) -> int:
        count = 0
        for i in range(len(A)):
            if A[i][0] == 0:
                for j in range(len(A[0])):
                    A[i][j] = 1 - A[i][j]
        print(A)
        for j in range(len(A[0])):
            is1 = 0
            for i in range(len(A)):
                if A[i][j]: is1 += 1
            count += max(is1, len(A) - is1) * 2 ** (len(A[0]) - j - 1)
        return count


# leetcode submit region end(Prohibit modification and deletion)


a = Solution()
print(a.matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]))

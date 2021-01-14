# 实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "1 + 1"
# 输出：2
#  
# 
#  示例 2： 
# 
#  
# 输入：s = " 2-1 + 2 "
# 输出：3
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "(1+(4+5+2)-3)+(6+8)"
# 输出：23
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 3 * 105 
#  s 由数字、'+'、'-'、'('、')'、和 ' ' 组成 
#  s 表示一个有效的表达式 
#  
#  Related Topics 栈 数学 
#  👍 324 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        def helper(s):
            stack = []
            sign = '+'
            num = 0

            while len(s) > 0:
                c = s.popleft()
                if c.isdigit():
                    num = 10 * num + int(c)
                if c == '(':
                    num = helper(s)

                if (not c.isdigit() and c != ' ') or len(s) == 0:
                    if sign == '+': stack.append((num))
                    if sign == '-': stack.append((-num))
                    if sign == '*': stack[-1] = stack[-1] * num
                    if sign == '/': stack[-1] = int(stack[-1] / float(num))
                    num = 0
                    sign = c
                if c == ')': break
            return sum(stack)
        return helper(deque(list(s)))

# leetcode submit region end(Prohibit modification and deletion)


a = Solution()

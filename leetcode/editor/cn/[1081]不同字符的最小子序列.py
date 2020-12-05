# 返回字符串 text 中按字典序排列最小的子序列，该子序列包含 text 中所有不同字符一次。 
# 
#  
# 
#  示例 1： 
# 
#  输入："cdadabcc"
# 输出："adbc"
#  
# 
#  示例 2： 
# 
#  输入："abcd"
# 输出："abcd"
#  
# 
#  示例 3： 
# 
#  输入："ecbacba"
# 输出："eacb"
#  
# 
#  示例 4： 
# 
#  输入："leetcode"
# 输出："letcod"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= text.length <= 1000 
#  text 由小写英文字母组成 
#  
# 
#  
# 
#  注意：本题目与 316 https://leetcode-cn.com/problems/remove-duplicate-letters/ 相同 
#  Related Topics 栈 贪心算法 字符串 
#  👍 62 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        res = []
        remain_count = collections.Counter(s)
        for c in s:
            if c not in res:
                while res and c < res[-1] and remain_count[res[-1]] > 0:
                    res.pop()
                res.append(c)
            remain_count[c] -= 1
        return ''.join(res)
# leetcode submit region end(Prohibit modification and deletion)


a = Solution()

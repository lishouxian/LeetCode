# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。 
# 
#  注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a", t = "a"
# 输出："a"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length, t.length <= 105 
#  s 和 t 由英文字母组成 
#  
# 
#  
# 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？ Related Topics 哈希表 双指针 字符串 Sliding Window 
#  👍 857 👎 0
print(ord('A'))



# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        temp = [0] * 100
        for c in t:
            temp[ord(c) - 65] += 1
        print(temp)
        l = r = 0
        res = ""
        while r < len(s) + 1:
            while max(temp) <= 0:
                if res == "" or r - l < len(res):
                    res = s[l:r]
                temp[ord(s[l]) - 65] += 1
                l += 1
            if r < len(s):
                temp[ord(s[r]) - 65] -= 1
            r += 1
        return res

        # leetcode submit region end(Prohibit modification and deletion)



a = Solution()
print(a.minWindow(s="a", t="aa"))

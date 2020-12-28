# 给定两个字符串 s 和 t，判断它们是否是同构的。 
# 
#  如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。 
# 
#  所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。 
# 
#  示例 1: 
# 
#  输入: s = "egg", t = "add"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: s = "foo", t = "bar"
# 输出: false 
# 
#  示例 3: 
# 
#  输入: s = "paper", t = "title"
# 输出: true 
# 
#  说明: 
# 你可以假设 s 和 t 具有相同的长度。 
#  Related Topics 哈希表 
#  👍 295 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1 = {}
        m2 = {}
        for i in range(len(s)):
            if s[i] in m1:
                if m1[s[i]] != t[i]:
                    return False
            else:
                m1[s[i]] = t[i]

            if t[i] in m2:
                if m2[t[i]] != s[i]:
                    return False
            else:
                m2[t[i]] = s[i]
        return True


# leetcode submit region end(Prohibit modification and deletion)


a = Solution()

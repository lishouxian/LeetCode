# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。 
# 
#  示例: 
# 
#  输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ] 
# 
#  说明： 
# 
#  
#  所有输入均为小写字母。 
#  不考虑答案输出的顺序。 
#  
#  Related Topics 哈希表 字符串 
#  👍 535 👎 0



# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def groupAnagrams(self, strs):
        map = {}
        res = []

        for s in strs:

            a = list(s)
            a.sort()
            a = ''.join(a)

            if a not in map:
                res.append([s])
                map[a] = len(res) - 1
            else:
                res[map[a]].append(s)

        return res




# leetcode submit region end(Prohibit modification and deletion)



a = Solution()
print(a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

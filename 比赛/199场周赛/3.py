class Solution:
    def countPairs(self, root, distance) -> int:
        save = []
        def getnum(tree):
            if not tree: return []
            left = getnum(tree.left)
            right = getnum(tree.right)
            newsave = [0] *(len(left )+ len(right))
            for i in range(len(left)):
                newsave[i] = left[i]
            for i in range(len(right)):
                newsave[-i-1] = right[i]
            save.append(newsave)

            return newsave
        getnum(root)
        print(save)



a = Solution()
print(a.countPairs(root = [1,2,3,4,5,6,7], distance = 3))
class Solution:
    def numSpecial(self, mat) -> int:
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    count = 0
                    count += sum(mat[i])
                    for k in range(len(mat[0])):
                        count += mat[k][j]
                    print(count)
                    if count == 2:
                        res += 1
        return res



a = Solution()
print(a.numSpecial("  this   is  a sentence "))
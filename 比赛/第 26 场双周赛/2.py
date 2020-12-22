class Solution:
    def simplifiedFractions(self, n: int):
        res = []
        def huzhi(a,b):
            if a == 1 or b == 1: return True
            if a == 0 or b == 0: return False
            else: 
                return huzhi(b, a%b)
        for i in range(2,n+1):
            for j in range(1,i):
                if huzhi(i,j):
                    m = str(j) + '/' + str(i)
                    res.append(m)
                    
        return res





a = Solution()
print(a.simplifiedFractions(1))
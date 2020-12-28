class Solution:
    def getProbability(self, balls) -> float:
        n = sum(balls)//2
        print(n)

        count = 0
        l = len(balls)
        def A(a,b): #排列数
            n = 1
            for i in range(a,a-b,-1):
                n *= i
            return n
        def C(a,b): #组合数
            return A(a,b) // A(b,b)
        for i in range(2 ** l):
            c = bin(i)[2:]
            a = [0]* (l - len(c)) + list(map(int,c))
            #print(a)
            for j in range(2 ** l):
                c = bin(j)[2:]
                b = [0]* (l - len(c)) + list(map(int,c))
                if sum(a) == sum(b):
                    save = 0

                    for i in range(l):
                        if a[i] == 0 and b[i] == 0:
                            save = -1
                        if a[i] == 1 and b[i] == 1 and balls[i] ==1:
                            save = -1

                    if save == 0:
                        suibiannum = 0
                        countnum = n
                        for i in range(l):
                            if a[i] == 1 and b[i] == 0:
                                countnum -= balls[i]

                            elif a[i] == 1 and b[i] == 1:
                                suibiannum += balls[i]-2
                    
                        count += C(suibiannum,countnum)
        print(count)

        print(C)

        return count/ C(n,2*n)
a = Solution()
print(a.getProbability([6,6,6,6,6,6]))
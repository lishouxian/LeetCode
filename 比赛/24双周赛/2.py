class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        back = []
        al = ['a','b','c']
        save = 2
        if k > 2**(n-1) * 3:return ''
        if n ==1:
            if k == 1:return 'a'
            if k == 2: return 'b'
            if k == 3: return 'c'
        while n > 0:
            if k ==1 and n == 1:
                if save == 2:
                        back.append('a')
                        save = 1
                elif save == 1:
                        back.append('a')
                        save = 0
                elif save == 0:
                        back.append('b')
                        save = 2
                break
            if k == 0 or k == 2**(n-1):
                if save == 2:
                        back.append('b')
                        save = 1
                elif save == 1:
                        back.append('a')
                        save = 0
                elif save == 0:
                        back.append('b')
                        save = 1

            elif save == 2 :
                if k // 2**(n-1) == 0:
                    back.append('a')
                    save = 0
                elif k // 2**(n-1) == 1:
                    back.append('b')
                    save = 1
                elif k // 2**(n-1) == 2 or k / 2**(n-1) == 3:
                    back.append('c')
                    save = 2

            elif save == 1:
                if k // 2**(n-1) == 0:
                    back.append('a')
                    save = 0
                else:
                    back.append('c')
                    save = 2
            elif save == 0:
                if k // 2**(n-1) == 0:
                    back.append('b')
                    save = 1
                else:
                    back.append('c')
                    save = 2
            #print(save)
            print(k,2**(n-1))
            k = k % 2**(n-1)
            n = n - 1
        back = ''.join(back)
        return back

a = Solution()
print(a.getHappyString(2,7))
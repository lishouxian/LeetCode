class Solution:
    def reformat(self, s: str) -> str:
        num = ['1','2','3','4','5','6','7','8','9','0']
        shuzu = zimu = 0
        back = []
        back1 = []
        m = 0
        while zimu < len(s) and shuzu < len(s):

            while zimu < len(s):
                if s[zimu] in num:
                    zimu += 1
                else:
                    back.append(s[zimu])
                    zimu += 1
                    break
            if zimu < len(s) and shuzu < len(s):
                while shuzu < len(s):
                    if s[shuzu] in num:
                        back.append(s[shuzu])
                        shuzu += 1
                        break
                    else:
                        shuzu += 1
        if zimu < len(s) and ( not (s[zimu] in num)) and back[-1] in num:

            back.append(s[zimu])


        shuzu = zimu = 0
        while zimu < len(s) and shuzu < len(s):
            while shuzu < len(s):
                if s[shuzu] in num:
                    back1.append(s[shuzu])
                    shuzu += 1
                    break
                else:
                    shuzu += 1
            if zimu < len(s) and shuzu < len(s):
                while zimu < len(s):
                    if s[zimu] in num:
                        zimu += 1
                    else:
                        back1.append(s[zimu])
                        zimu += 1
                        break


        if shuzu < len(s) and s[shuzu] in num and (not back1[-1] in num):
            back1.append(s[shuzu])


        if len(back) == len(s):
            return ''.join(back)
        elif len(back1) == len(s):
            return ''.join(back1)
        else:return ''





a = Solution()
print(a.reformat("1231321332019"))
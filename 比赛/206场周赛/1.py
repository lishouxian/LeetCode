class Solution:
    def reorderSpaces(self, text: str) -> str:
        text = text+' '
        save = []
        count = -1
        left = None
        for i in range(len(text)):
            if text[i] == ' ':
                if left is not None:
                    save.append(text[left:i])
                    left = None
                count += 1
            else:
                if text[i - 1] == ' ' or i == 0:
                    left = i
        if len(save)-1 == 0:
            a = 0
            b = count
        else:
            a = count // (len(save)-1)
            b = count % (len(save)-1)
        print(a,b)
        return (' '*a).join(save) + ' '*b

a = Solution()
print(a.reorderSpaces("  hello"))
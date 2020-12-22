class Solution:
    def arrangeWords(self, text: str) -> str:
        count = []
        left = 0
        for i in range(len(text)):
            if text[i] ==' ':
                count.append(text[left:i])
                left = i + 1
        count.append(text[left:i+1])
        
        # print(count)
        while [' '] in count:
            count.remove(' ')

        count1 = sorted(count,key = lambda i:len(i),reverse=False)
        count1 = ' '.join(count1)
        # print(count1.capitalize())
        # print(count1)

        return count1.capitalize()



a = Solution()
print(a.arrangeWords("Keep calm and code on"))

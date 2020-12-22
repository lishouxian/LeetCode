class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = ' ' + sentence
        searchWord = ' ' + searchWord
        L = len(searchWord)
        save = 0
        for i in range(len(sentence)):
            if sentence[i] == ' ': save += 1
            if sentence[i:i + L] == searchWord:
                return save
        return -1


a = Solution()
print(a.isPrefixOfWord("i use triple pillow","pill"))
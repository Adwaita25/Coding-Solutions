class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        n = len(searchWord)

        for i in range(len(sentence)):
            word = sentence[i]
            if len(word) >= n and searchWord == word[:n]:
                return i+1
        return -1

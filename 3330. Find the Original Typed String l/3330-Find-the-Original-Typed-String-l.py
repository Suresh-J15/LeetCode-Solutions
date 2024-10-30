class Solution:
    def possibleStringCount(self, word: str) -> int:
        result = 1
        for idx in range(len(word) - 1):
            if word[idx] == word[idx + 1]:
                result += 1

        return result
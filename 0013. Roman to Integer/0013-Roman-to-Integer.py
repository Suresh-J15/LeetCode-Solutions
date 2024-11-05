class Solution:
    def romanToInt(self, s: str) -> int:
        i, result, length = 0, 0, len(s)
        roman = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }

        while i < length:
            if i < length - 1 and roman[s[i]] < roman[s[i + 1]]:
                print(roman[s[i]], roman[s[i + 1]], i)
                result += roman[s[i + 1]] - roman[s[i]]
                i += 2
            else:
                result += roman[s[i]]
                i += 1
        
        return result
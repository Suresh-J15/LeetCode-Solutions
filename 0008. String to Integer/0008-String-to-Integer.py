class Solution:
    def myAtoi(self, s: str) -> int:
        i, ans, sign, length = 0, 0, 1, len(s)
        if not(s):
            return 0
        
        while i < length and s[i] == ' ':
            i += 1
        if i < length and s[i] == '-':
            sign = -1
            i += 1
        elif i < length and s[i] == '+':
            i += 1

        digits = set('1234567890')
        while i < length:
            if s[i] in digits:
                ans = (ans * 10) + (ord(s[i]) - 48)
                if ans >= 2147483647 and sign == 1:
                    return 2147483647
                elif ans >= 2147483648 and sign == -1:
                    return -2147483648 
                i += 1
            else:
                return ans * sign
        
        return ans * sign
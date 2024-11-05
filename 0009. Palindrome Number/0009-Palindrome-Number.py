class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        rev, temp = 0, x
        while temp > 0:
            rev = (rev * 10) + (temp % 10)
            temp //= 10
        
        return rev == x
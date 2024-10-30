class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        x, rev = abs(x), 0
        while x > 0:
            mod = x % 10
            rev = (rev * 10) + mod
            x //= 10
            if rev >= 2147483647:
                break

        rev = sign * rev
        if rev >= 2147483647 or rev <= -2147483648:
            return 0
        else:
            return rev
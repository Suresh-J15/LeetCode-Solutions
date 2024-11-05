class Solution {
public:
    int reverse(int x) {
        long rev = 0;
        while (x != 0) {
            int mod = x % 10;
            rev = (rev * 10) + mod;
            x /= 10;
        }
        if (rev <= INT_MIN || rev >= INT_MAX) {
            return 0;
        } else {
            return (int)rev;
        }
    }
};
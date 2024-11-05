class Solution {
public:
    long reverse(int y) {
        long rev = 0;
        while (y > 0){
            int com = y % 10;
            rev = rev * 10 + com;
            y = y / 10;
        }
        return rev;
    }
    bool isPalindrome(int x) {
        // if (x < 0) { return false; }
        long rev = reverse(x);
        long input = x;
        return rev == input;
    }
};
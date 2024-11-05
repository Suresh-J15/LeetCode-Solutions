class Solution {
    public int reverse(int y) {
        int rev = 0;
        while (y > 0){
            int com = y % 10;
            rev = rev * 10 + com;
            y = y / 10;
        }
        return rev;
    }
    public boolean isPalindrome(int x) {
        // if (x < 0) { return false; }
        int rev = reverse(x);
        return rev == x;
    }
}

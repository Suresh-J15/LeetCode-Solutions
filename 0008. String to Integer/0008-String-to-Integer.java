class Solution {
    public int myAtoi(String s) {
        int i = 0;
        long ans = 0, sign = 1;
        if (s.equals("")) {
            return 0;
        }

        while (i < s.length() && s.charAt(i) == ' ') {
            i += 1;
        } 
        if (i < s.length() && s.charAt(i) == '-') {
            sign = -1; i++;
        } else if (i < s.length() && s.charAt(i) == '+') {
            i++;
        }

        while (i < s.length()) {
            if (s.charAt(i) >= '0' && s.charAt(i) <= '9') {
                ans = (ans * 10) + (s.charAt(i) - '0');
                if (ans > Integer.MAX_VALUE && sign == -1) {
                    return Integer.MIN_VALUE;
                } else if (ans > Integer.MAX_VALUE && sign == 1) {
                    return Integer.MAX_VALUE;
                }
                i++;
            } else {
                return (int)(ans * sign);
            }
        }
        return (int)(ans * sign);
    }
}
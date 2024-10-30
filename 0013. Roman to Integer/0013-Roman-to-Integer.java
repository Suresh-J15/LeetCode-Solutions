class Solution {
    public int romanToInt(String s) {
        int i = 0, result = 0;
        int length = s.length();
        int[] roman = new int[256];    
        roman['I'] = 1;     roman['V'] = 5;
        roman['X'] = 10;    roman['L'] = 50;
        roman['C'] = 100;   roman['D'] = 500;
        roman['M'] = 1000;

        while (i < length) {
            if (i < length - 1 && roman[s.charAt(i + 1)] > roman[s.charAt(i)]) {
                result += roman[s.charAt(i + 1)] - roman[s.charAt(i)];
                i += 2;
            } else {
                result += roman[s.charAt(i)];
                i += 1;
            }
        } 
        return result;
    }
}
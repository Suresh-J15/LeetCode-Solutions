class Solution {
    public int possibleStringCount(String word) {
        int result = 1;
        for (int i = 0; i < word.length() - 1; i++) {
            if (word.charAt(i) == word.charAt(i + 1)) {
                result += 1;
            }
        }
        return result;
    }
}
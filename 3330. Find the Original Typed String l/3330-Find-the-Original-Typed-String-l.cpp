class Solution {
public:
    int possibleStringCount(string word) {
        int result = 1;
        for (int i = 0; i < word.length() - 1; i++) {
            if (word[i] == word[i + 1]) {
                result += 1;
            }
        }
        return result;
    }
};
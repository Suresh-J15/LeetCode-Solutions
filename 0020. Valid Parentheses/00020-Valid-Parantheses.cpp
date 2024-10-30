class Solution {
public:
    bool isValid(string s) {
        if (s.length() % 2 != 0) {
            return false;
        }

        int size = 0;
        char stack[s.length()];
        for (int i = 0; i < s.length(); i++) {
            char ch = s[i];
            if (ch == '(') {
                stack[size] = ')';
                size++;
            } else if (ch == '{') {
                stack[size] = '}';
                size++;
            } else if (ch == '[') {
                stack[size] = ']';
                size++;
            } else if (size == 0 || ch != stack[size - 1]) {
                return false;
            } else {
                size--;
            }
        }
        return size == 0;
    }
};
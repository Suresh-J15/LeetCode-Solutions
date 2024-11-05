class Solution {
    public boolean isValid(String s) {
        if (s.length() % 2 != 0) {
            return false;
        }

        int size = 0;
        char[] stack = new char[s.length()];
        for (char ch : s.toCharArray()) {
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
}
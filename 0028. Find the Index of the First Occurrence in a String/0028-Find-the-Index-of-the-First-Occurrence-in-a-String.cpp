class Solution {
public:
    int strStr(string haystack, string needle) {
        int h = 0, n = 0, p = -1;
        while (h < haystack.length()) {
            if (haystack[h] != needle[n]) {
                n = 0;
                if (p != -1) {
                    h = p + 1;
                } else {
                    h = h + 1;
                }
                p = -1;
                continue;
            }

            if (n == 0) {
                p = h;
            }

            h += 1;    
            n += 1;
            
            if (n == needle.length()) {
                return h - n;
            }
        }
        return -1;
    }
};
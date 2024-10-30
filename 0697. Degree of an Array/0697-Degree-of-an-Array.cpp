class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        int maxfreq = 1;
        std::map<int, int> map;
        for (int i = 0; i < nums.size(); i++) {
            map[nums[i]] += 1;
            maxfreq = max(maxfreq, map[nums[i]]);
        }
        if (maxfreq == 1) {
            return 1;
        }

        int minsize = nums.size();
        for (const auto& [key, value] : map) {
            if (value != maxfreq) {
                continue;
            } else {
                int left = 0, right = nums.size() - 1;
                while (nums[left] != key) {
                    left += 1;
                }
                while (nums[right] != key) {
                    right -= 1;
                }
                minsize = min(minsize, right - left + 1);
            }
        }
        return minsize;
    }
};
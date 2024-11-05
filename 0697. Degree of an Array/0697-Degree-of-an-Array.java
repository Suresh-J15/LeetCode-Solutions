class Solution {
    public int findShortestSubArray(int[] nums) {
        int maxfreq = 1;
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i])) {
                int freq = map.get(nums[i]);
                map.put(nums[i], freq + 1);
                maxfreq = Integer.max(maxfreq, freq + 1);
            } else {
                map.put(nums[i], 1);
            }
        }

        if (maxfreq == 1) {
            return 1;
        }

        int minsize = nums.length;
        for (Integer e : map.keySet()) {
            if (map.get(e) != maxfreq) {
                continue;
            } else {
                int left = 0, right = nums.length - 1;
                while (nums[left] != e) {
                    left += 1;
                } while (nums[right] != e) {
                    right -= 1;
                }
                minsize = Integer.min(minsize, right - left + 1);
            }
        }
        return minsize;
    }
}
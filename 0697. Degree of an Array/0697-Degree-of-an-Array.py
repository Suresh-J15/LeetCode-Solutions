class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        degree = max(freq.values())
        
        if degree == 1:
            return 1
        
        ans = len(nums)
        nums_freq = [n for n in freq if freq[n] == degree]
        
        for n in nums_freq:
            first = nums.index(n)
            last = len(nums) - nums[::-1].index(n)
            ans = min(ans, last - first)
        
        return ans

        """
        length, degree = {}, 0
        dictionary = defaultdict(lambda: 0)
        for num in nums:
            dictionary[num] += 1
            degree = max(degree, dictionary[num])

        for num, rep in dictionary.items():
            if rep == degree:
                length[num] = [nums.index(num), -1]
        
        for i in range(len(nums)):
            if nums[i] in length.keys():
                length[nums[i]][1] = i

        result = math.inf
        for num, ran in length.items():
            result = min(result, ran[1] - ran[0] + 1)
        return result
        """
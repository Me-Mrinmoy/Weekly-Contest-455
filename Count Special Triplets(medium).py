from collections import defaultdict

class Solution:
    def specialTriplets(self, nums):
        MOD = 10**9 + 7
        left_count = defaultdict(int)
        right_count = defaultdict(int)
        
        # Count all numbers in right_count initially
        for num in nums:
            right_count[num] += 1
        
        total = 0
        for j in range(len(nums)):
            right_count[nums[j]] -= 1  # Remove current from right

            target = nums[j] * 2
            count_left = left_count[target]
            count_right = right_count[target]
            
            total = (total + count_left * count_right) % MOD
            
            left_count[nums[j]] += 1  # Add current to left

        return total

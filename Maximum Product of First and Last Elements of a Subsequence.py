class Solution:
    def maximumProduct(self, nums, m):
        n = len(nums)
        max_product = float('-inf')

        for i in range(n - m + 1):
            for j in range(i + m - 1, n):
                product = nums[i] * nums[j]
                max_product = max(max_product, product)

        return max_product

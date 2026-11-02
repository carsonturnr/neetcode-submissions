class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        before = 1
        for i in range(len(nums)):
            output[i] = before
            before *= nums[i]

        after = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= after
            after *= nums[i]
        return output
        
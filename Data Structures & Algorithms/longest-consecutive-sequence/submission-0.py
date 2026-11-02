class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for num in seen:
            length = 1
            if num - 1 in seen:
                continue
            while num + 1 in seen:
                length += 1
                num += 1
            longest = max(longest, length)
        return longest

        
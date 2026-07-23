class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        in_memory = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in in_memory:
                return [in_memory[diff], i]
            in_memory[num] = i
        
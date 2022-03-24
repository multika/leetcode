class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap_values = {}
        for index, num in enumerate(nums):
            if target-num in hashmap_values:
                return [index, hashmap_values[target-num]]
            else:
                hashmap_values[num] = index

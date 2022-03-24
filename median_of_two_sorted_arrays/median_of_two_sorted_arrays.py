class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = nums1 + nums2
        merged_array.sort()
        if len(merged_array)%2 != 0:
            return merged_array[len(merged_array)//2]
        average_of_middle_elements = (merged_array[len(merged_array)//2] + merged_array[len(merged_array)//2-1])/2
        return average_of_middle_elements

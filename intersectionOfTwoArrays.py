class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        
        if len(nums1)<len(nums2):
            smaller = nums1
            other = nums2
        else:
            smaller = nums2
            other = nums1
        
        for num in smaller:
            if num in other and num not in result:
                result.append(num)
        return result
        
        
        #time: O(n) squared
        #space: O(n)

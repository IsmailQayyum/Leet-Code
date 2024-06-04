class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        del nums1[m:]
        for i in nums2:
            nums1.append(i)
        nums1.sort()


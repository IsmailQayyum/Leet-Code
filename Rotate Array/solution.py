class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        [nums.insert(0,nums.pop(len(nums)-1)) for _ in range(k)]

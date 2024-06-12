class Solution:
    def canJump(self, nums: List[int]) -> bool:
        steps=nums[0]
        si=0
        if len(nums)==1:
            return True
        elif steps==0:
            return False
        if si+steps>=len(nums)-1:
                return True
        for i in range(1,len(nums)):
            if nums[i]>=steps:
                steps=nums[i]
                si=i
            else:
                steps-=1
            if si+steps>=len(nums)-1:
                return True
            elif steps==0 and i!=len(nums)-1 and nums[i]==0:
                return False

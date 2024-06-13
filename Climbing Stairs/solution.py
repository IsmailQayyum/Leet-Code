class Solution:
    def climbStairs(self, n: int) -> int:
        index=0
        traversed= {}
        def climb(index: int):
            ways=0
            if index==n:
                return 1
            elif index>n:
                return 0
            
            if index in traversed:
                return traversed[index]
            ways+= climb(index+1)
            ways+= climb(index+2)
            traversed[index]=ways
            return ways 
        return climb(index)
    

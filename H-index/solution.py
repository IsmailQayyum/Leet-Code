class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        if citations[0]==0:
            return 0
        for i in range(len(citations)):
            if i+1 <= citations[i]:
                h_index=i+1
            else:
                break
        return h_index
      

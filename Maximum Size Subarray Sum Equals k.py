class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
        prefix = 0
        idx = {}
        fin = 0
        
        
        for i in range(len(nums)):
            prefix += nums[i]
            
            if(prefix == k):
                fin = max(i+1,fin)
                if(idx.get(prefix,None) == None):
                    idx[prefix] = i
            elif(idx.get(prefix-k,None) != None):
                fin = max(i-idx[prefix-k],fin)
            else:
                if(idx.get(prefix,None) == None):
                    idx[prefix] = i
        print(idx)      
        return(fin)
		
# Solution to the problem https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        l,r = 1,n
        
        while(l<=r):
            
            m = (l+r)//2
            
            if(isBadVersion(m)):
                if(m == 1):
                    return(1)
                elif(isBadVersion(m-1)):
                    r = m-1
                else:
                    return(m)
            
            elif(not isBadVersion(m)):
                l = m+1
                
        
# Solution for https://leetcode.com/problems/first-bad-version/
class Solution:
    def mySqrt(self, x: int) -> int:
        
        n = x//2
        
        l,r = 1,n
        if(x == 0):
            return(0)
        if(x == 1):
            return(1)
        while(l<=r):
            
            m = (l+r)//2
            # print(l,r,m,(m+1)**2,x)
            if(m**2 <= x and ((m+1)**2)>x):
                return(m)
            elif(m**2 > x):
                r = m-1
            else:
                l = m+1
                
        

# Solution for https://leetcode.com/problems/sqrtx/
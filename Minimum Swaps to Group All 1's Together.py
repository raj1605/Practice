class Solution:
    def minSwaps(self, data: List[int]) -> int:
        
        count = 0
        for i in data:
            if(i == 1):
                count += 1
                
        count -= 1
        ones = 0
        for i in range(count + 1):
            if(data[i] == 1):
                ones += 1
        # print(ones)
        if(ones == 0):
            return(0)
        fin = count + 1 - ones
        i,j = 0,count
        while(j<len(data)):
            print(i,j)
            if(data[i] == 1):
                if(j+1 == len(data)):
                    break
                elif(data[j+1] == 1):
                    i += 1
                    j += 1
                    continue
                else:
                    ones -= 1
                    
            else:
                if(j + 1 == len(data)):
                    break
                elif(data[j+1] == 0):
                    i += 1
                    j += 1
                    continue
                else:
                    ones += 1
            
            fin = min(fin,count + 1 - ones)
            i += 1
            j += 1
            
        return(fin)
class Solution:
    def isHappy(self, num: int) -> bool:
        lt = []
        while True:
            end_sum = 0
            while(num>0):
                rem = num%10
                end_sum+= (rem**2)
                num = num//10
            num = end_sum
            if(end_sum==1):
                return True
            elif(end_sum in lt):
                return False
            else:
                lt.append(end_sum)
        
                
            
        
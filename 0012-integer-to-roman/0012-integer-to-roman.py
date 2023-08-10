class Solution:
    def intToRoman(self, num: int) -> str:
        dict = {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
        #st = ""
        # temp = num
        # ct = 1
        # while(num>0):
        #     rem = num % 10
        #     num = num //10
        #     if(rem == 4):
        #         tp = ct * 5
        #         temp_st = dict[ct]+dict[tp]
        #     elif(rem==9):
        #         tp = ct * 10
        #         temp_st = dict[ct]+dict[tp]
        #     else:
        #         if(rem >= 5):
        #             key = ct*5
        #             val = rem - 5
        #             temp_st = dict[key]+(val*dict[ct])
        #         else:
        #             temp_st = rem*dict[ct]
        #     st = temp_st+st
        #     ct = ct*10
        st = ""
        nums = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        for each_num in nums:
            while(each_num<=num):
                st+=dict[each_num]
                num-=each_num
        return st
                    
                    
                
        
class Solution:
    def intToRoman(self, num: int) -> str:
        dict = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        st = ""
        temp = num
        ct = 1
        while(num>0):
            rem = num % 10
            num = num //10
            if(rem == 4):
                tp = ct * 5
                temp_st = dict[ct]+dict[tp]
            elif(rem==9):
                tp = ct * 10
                temp_st = dict[ct]+dict[tp]
            else:
                if(rem >= 5):
                    key = ct*5
                    val = rem - 5
                    temp_st = dict[key]+(val*dict[ct])
                else:
                    temp_st = rem*dict[ct]
            st = temp_st+st
            ct = ct*10
        return st
                    
                    
                
        
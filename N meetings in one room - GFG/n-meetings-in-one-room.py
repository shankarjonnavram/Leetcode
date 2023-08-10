#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        temp = []
        for i in range(n):
            temp.append([start[i],end[i],i])
            
        temp = sorted(temp,key = lambda x:(x[1],x[2]))
        
        end_val = temp[0][1]
        ct = 1
        
        for i in range(1,n):
            if(temp[i][0]>end_val):
                ct+=1
                end_val = temp[i][1]
        return ct
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends
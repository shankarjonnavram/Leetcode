#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        # lt = []
        # # for i in range(n):
        # #     lt.append([arr[i],dep[i]])
        # # sorted(lt,key= lambda x:)
        # ct = 1
        # end_time = dep[0]
        # minm = float('inf')
        # for i in range(1,n):
        #     if(len(lt)>0 and arr[i]>minm):
        #         continue
        #     elif(arr[i]>end_time):
        #             end_time = dep [i]
        #     else:
        #         lt.append(end_time)
        #         minm = min(minm,end_time)
        #         ct+=1
        # return ct
        arr.sort()
        dep.sort()
        maxm = 1
        plat = 1
        i , j = 1 ,0
        while i<n and j<n:
            if(arr[i]<=dep[j]):
                plat+=1
                i+=1
            elif(arr[i]>dep[j]):
                j+=1
                plat-=1
            if(plat>maxm):
                maxm=plat
        return maxm
            
        


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
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends
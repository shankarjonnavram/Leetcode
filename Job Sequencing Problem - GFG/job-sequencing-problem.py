#User function Template for python3

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        # code here
        lt = []
        for i in Jobs:
            lt.append([i.id , i.deadline,i.profit])
        lt = sorted(lt , key = lambda x:x[2],reverse=True)
        
        sz = len(lt)
        maxm =0
        ct = 0
        max_dead = 0
        for i in range(sz):
            max_dead = max(max_dead,lt[i][1])
        dead = [-1]*(max_dead)
        # print(dead)
        for i in range(sz):
            for j in range(lt[i][1]-1,-1,-1):
                if(dead[j]==-1):
                    ct+=1
                    dead[j]= i
                    maxm+=lt[i][2]
                    break
        return ct , maxm

                
        
# 5
# 1 2 100 
# 2 1 19 
# 3 2 27 
# 4 1 25 
# 5 1 15



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        ob = Solution()
        res = ob.JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])
# } Driver Code Ends
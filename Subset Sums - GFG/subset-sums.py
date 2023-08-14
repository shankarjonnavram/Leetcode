#User function Template for python3

def sums(left,lt,arr,val,right):
    if(left==right):
        lt.append(val)
        return
    val+=arr[left]
    sums(left+1,lt,arr,val,right)
    val-=arr[left]
    sums(left+1,lt,arr,val,right)
    

class Solution:
	def subsetSums(self, arr, N):
	    lt = []
	    val = 0
	    left = 0
	    right = len(arr)
	    sums(left,lt,arr,val,right)
	    return lt
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends
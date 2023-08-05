//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
/*You are required to complete this function*/

class Solution{
    public:
    int maxLen(vector<int>&A, int n)
    {   
        // Your code here
        int sum = 0;
        int maxm = 0;
        unordered_map<int,int>a1;
        for(int i=0;i<n;i++){
            sum = sum+A[i];
            if(sum==0){
                maxm = i+1;
            }
            else{
                if(a1.count(sum)>0){
                    int ind_len = i - a1 [sum];
                    maxm = max(maxm , ind_len);
                }
                else{
                    a1[sum] = i;
                }
            }
        }
        return maxm;
    }
};


//{ Driver Code Starts.

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int m;
        cin>>m;
        vector<int> array1(m);
        for (int i = 0; i < m; ++i){
            cin>>array1[i];
        }
        Solution ob;
        cout<<ob.maxLen(array1,m)<<endl;
    }
    return 0; 
}



// } Driver Code Ends
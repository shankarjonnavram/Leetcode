class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals =sorted(intervals)
        new_lt = intervals[0]
        res_lt = []
        for i in range(1,len(intervals)):
            # if(new_lt[1]<intervals[i][0]):
            #     res_lt.append(new_lt)
            #     new_lt = intervals[i]
            # elif (new_lt[0]>intervals[i][1]):
            #     res_lt.append(new_lt)
            #     new_lt = intervals[i]
            # else:
            #     new_lt = [min(new_lt[0],intervals[i][0]),
            #               max(new_lt[1],intervals[i][1])]
            if(new_lt[1]>=intervals[i][0]):
                new_lt = [min(new_lt[0],intervals[i][0]),
                           max(new_lt[1],intervals[i][1])]
            else:
                res_lt.append(new_lt)
                new_lt = intervals[i]
        res_lt.append(new_lt)
        return res_lt
            
        
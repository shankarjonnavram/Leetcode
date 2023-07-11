class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res_lt = []
        for i in range(len(intervals)):
            if newInterval[1]<intervals[i][0]:
                res_lt.append(newInterval)
                return res_lt+intervals[i:]
            elif newInterval[0]>intervals[i][1]:
                res_lt.append(intervals[i])
            else:
                newInterval = [min(newInterval[0],intervals[i][0]),
                               max(newInterval[1],intervals[i][1])]
        res_lt.append(newInterval)
        return res_lt
                
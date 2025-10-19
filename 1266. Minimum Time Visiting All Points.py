class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count = 0 # Result integer we are returning 
        x1 , y1 = points.pop() #pops the last point in the list
        while points: # this iteratres throug the list 
            x2 , y2 = points.pop() #pops next point next to it
            count += max(abs(y2-y1), abs(x2-x1)) # takes which value is greater than to move from tehn adds it to count
            x1, y1 = x2 , y2 #switch values for next iteration 
        return count#return count as result
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        def first(x):
            return x[1]

        points.sort(key = first)
        
        arrows = 1
        current_end = points[0][1]
        for start,end in points:
            if start > current_end:
                current_end = end
                arrows += 1
        return arrows
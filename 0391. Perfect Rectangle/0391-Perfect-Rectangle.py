class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        totalArea = 0
        points = set()
        a = lambda: (Y - y) * (X - x)
        c = lambda k: k[0] + k[1] 

        for x, y, X, Y in rectangles:
            totalArea += a()
            points ^= {(x, y), (x, Y), (X, y), (X, Y)}
        
        if len(points) != 4:
            return False
        x, y = min(points, key=c)
        X, Y = max(points, key=c)

        return totalArea == a()
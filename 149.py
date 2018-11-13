# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """

        if len(points) <= 2:
            return len(points)

        dic = {}
        hengxian = 0
        # zero_zero=1
        zero_zero = points.count([0, 0])
        for i in range(len(points)):
            for j in range(i + 1, len(points), 1):
                y = points[i].y - points[j].y
                x = points[i].x - points[j].x

                if x == 0:
                    hengxian += 1
                else:
                    gys = self.maxgys(y, x)
                    if dic.get((y / gys, x / gys)):
                        dic[((int(y / gys), int(x / gys)))].add((points[i].x, points[i].y))
                        dic[((int(y / gys), int(x / gys)))].add((points[j].x, points[j].y))
                    else:
                        dic[((int(y / gys), int(x / gys)))] = set(((points[i].x, points[i].y), (points[j].x, points[j].y)))
        if dic:
            maxnum = 0
            for i in dic.values():
                maxnum = max(maxnum, len(i))
            if zero_zero:
                ans = max(hengxian, maxnum + zero_zero - 1)
            else:
                ans = max(hengxian, maxnum + zero_zero)

        else:
            return hengxian
        return ans

    def maxgys(self, dividend, divisor):
        if dividend % divisor == 0:
            return divisor
        else:
            return self.maxgys(divisor, dividend % divisor)

a=Solution()
a.maxPoints([[0,0],[1,1],[0,0]])
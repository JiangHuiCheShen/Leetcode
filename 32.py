n = int（raw_input()）
for i in range(n):
    ### 算出移动后坐标(16个，团中每个点4个)
    corr = [[]]

    for j in range(4):
        input = map(int, raw_input().split())
        a = input[0]
        b = input[1]
        x = input[2]
        y = input[3]
        for k in range(4):
            coor[j].append([new_a, new_b])
            new_a = (b - y) + x
            new_b = -(a - x) + y

            step = 0
            minstep = 1000
            ###判断是否为正方形
            for j in range(4):
                for k in range(4):
                    for m in range(4):
                        for n in range(4):
                            tmp = [corr[i], corr[j], corr[m], corr[n]]
                            step = i + k + m + n
                            if validSqaure(corr):
                                minstep = min(step, minstep)
                                output.append(minstep)
                                print output


### 是否为正方形函数
def validSquare(tmp):
    p1, p2, p3, p4 = tmp[0], tmp[1], tmp[2], tmp[3]


points = [p1, p2, p3, p4]
dists = collections.Counter()
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dists[getDistance(points[i], points[j])] += 1

return len(dists.values()) == 2 and 4 in dists.values() and 2 in dists.values()


def getDistance(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
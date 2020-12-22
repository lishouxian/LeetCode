class Solution:
    def numPoints(self, points, r) -> int:
        print(len(points))
        def getCircle(p1, p2, p3):
            x21 = p2[0] - p1[0]
            y21 = p2[1] - p1[1]
            x32 = p3[0] - p2[0]
            y32 = p3[1]- p2[1]
            # three colinear
            if (x21 * y32 - x32 * y21 == 0):
                return 0,0,-1
            xy21 = p2[0] * p2[0] - p1[0] * p1[0] + p2[1] * p2[1] - p1[1] * p1[1]
            xy32 = p3[0] * p3[0] - p2[0] * p2[0] + p3[1] * p3[1] - p2[1] * p2[1]
            y0 = (x32 * xy21 - x21 * xy32) /( 2 * (y21 * x32 - y32 * x21))
            if x21 == 0:x0 =0
            else:x0 = (xy21 - 2 * y0 * y21) / (2.0 * x21)
            R = ((p1[0] - x0) ** 2 + (p1[1] - y0) ** 2) ** 0.5
            return x0, y0, R

        res = 1

        for i in range(len(points)):
            for j in range(i+1,len(points)):
                for k in range(j+1,len(points)):
                    x,y,r0 = getCircle(points[i],points[j],points[k])
                    if r0 == -1:break
                    count = 0
                    for p in range(len(points)):
                        if (points[p][0] - x) ** 2 + (points[p][1] - y) ** 2 <= r * r:
                            count += 1
                    res = max(res,count)

        #if res >= 3: return res

        for i in range(len(points)):
            for j in range(len(points)):
                x,y= points[i][0]/2.0 + points[j][0]/2.0,points[i][1]/2.0 + points[j][1]/2.0
                r0 = ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** 0.5
                #if r0 <= r:
                count = 0
                for p in range(len(points)):
                    if (points[p][0] - x) ** 2 + (points[p][1] - y) ** 2 <= r * r:
                        count += 1
                res = max(res,count)

        return res


a = Solution()
print(a.numPoints([[5738,-1857],[2264,1769],[5944,-9368],[3459,-9748],[8624,159],[985,-5051],[-8275,-9383],[7923,-591],[-8121,4781],[-9594,938],[-24,223],[9084,-4952],[-6787,5289],[4879,-4],[3998,369],[-7996,-7220],[-414,3638],[5092,4406],[1454,2965],[9210,-6966],[-4111,-8614],[4507,2213],[-4112,3699],[-9956,-2420],[7246,6775],[1164,5762],[6778,-5099],[-6655,-9514],[-2778,-7768],[6973,-7458],[7334,-1124],[4840,-8991],[941,5018],[1937,3608],[6807,6159],[763,1355],[-9776,-5074],[1107,1822],[-6779,-5400],[4219,-5674],[9823,-4630],[-9172,-7089],[-1875,162],[2267,1685],[4161,-1638],[-2475,9697],[-5367,-952],[-7786,4367],[839,1415],[8832,-4596],[-3843,7126],[-4242,8513],[-7883,1951],[9105,8342],[-4109,-4510],[1875,3149],[-7759,-6505],[1764,1624],[-6917,-6653],[-1438,6916],[-758,-3300],[3694,6699],[6135,2622],[7485,8284],[-9616,-8501],[408,4743],[8939,-731],[9208,-3748],[6059,-2587],[8403,4154],[2361,5708],[-3958,-3943],[-1746,-9082],[2864,-3231],[-4940,8519],[-8786,7898],[5154,-3647],[9011,8170],[-205,8717],[-4880,-9901],[1208,8896],[-430,4555],[-4699,3528]]
,4411))
class Solution:
    def getTriggerTime(self, increase, requirements):
        lens = len(requirements)
        for i in range(lens):
            requirements[i].append(i)
        requirements.sort()
        #print(requirements)
        back = [-1 for i in range(lens)]
        save_num = [0,0,0]
        i = 0
        while i < lens:
            if save_num[0] < requirements[i][0]:
                break
            if save_num[0] >= requirements[i][0] and save_num[1] >= requirements[i][1] and save_num[2] >= \
                    requirements[i][2]:
                back[requirements[i][3]] = 0
                requirements.remove(requirements[i])
                lens -= 1
                i = i - 1
            i = i + 1

        for time in range(len(increase)):
            save_num[0],save_num[1],save_num[2] = save_num[0] + increase[time][0],save_num[1] + increase[time][1],save_num[2] + increase[time][2],
            i = 0
            while i < lens:
                if save_num[0] < requirements[i][0]:
                    break
                if save_num[0] >= requirements[i][0] and save_num[1] >= requirements[i][1] and save_num[2] >= \
                        requirements[i][2]:
                    back[requirements[i][3]] = time + 1
                    requirements.remove(requirements[i])
                    lens -= 1
                    i = i - 1
                i = i+ 1
        return back

a = Solution()
print(a.getTriggerTime([[1,1,1]],[[0,0,0]]))
class Solution:
    def displayTable(self, orders):
        cai = []
        people = []
        for order in orders:
            if not order[2] in cai:
                cai.append(order[2])
            if not order[1] in people:
                people.append(order[1])
        #save = [[0] * len(cai) for i in range(len(people))]
        print(cai,people)
        #print(save)

        cai = sorted(cai)
        m =['Table']
        for ca in cai:
            m.append(ca)
        cai = m
        save = [[0] * len(cai) for i in range(len(people))]
        print(cai)
        for order in orders:
            save[people.index(order[1])][cai.index(order[2])] += 1
            save[people.index(order[1])][0] = int(order[1])
        save.sort()
        for i in range(len(save)):
            for j in range(len(save[0])):
                save[i][j] = str(save[i][j])
        return [cai] + save




a = Solution()
print(a.displayTable([["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]))
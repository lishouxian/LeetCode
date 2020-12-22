class TreeAncestor:

    def __init__(self, n: int, parent):
        self.save = []
        for i in range(n):
            if i == 0 : self.save.append([i,-1])

            else: 
                if len(self.save[parent[i]]) <= 500:
                    self.save.append([i] + self.save[parent[i]])
                else:
                    self.save.append([i])

        print(self.save)

    def getKthAncestor(self, node: int, k: int) -> int:
        while 1:
            if k >= len(self.save[node]) and self.save[node][-1] > 0:
                k -= len(self.save[node])
                node = self.save[node]
            elif k >= len(self.save[node]) and self.save[node][-1] < 0:
                return -1
            else: return self.save[node][k]


a = TreeAncestor(7,[-1, 0, 0, 1, 1, 2, 2])

print(a.getKthAncestor(5,1))
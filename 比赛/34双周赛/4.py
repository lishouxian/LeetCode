class Solution:
    def containsCycle(self, grid):
        help = [[0] *len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if help[i][j] == 0:
                    save = grid[i][j]
                    help[i][j] = 1
                    p, q = i, j
                    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                    savedirection = 0
                    rode = 0
                    while 1:
                        if savedirection == 1:
                            direction = [[0,1],[1,0],[0,-1],[-1,0]]
                        if savedirection == 2:
                            direction = [[1,0],[0,-1],[-1,0],[0,1]]
                        if savedirection == -1:
                            direction = [[0,-1],[-1,0],[0,1],[1,0]]
                        if savedirection == -2:
                            direction = [[-1,0],[0,1],[1,0],[0,-1]]
                        for dir in range(4):
                            m, n = p + direction[dir][0], q + direction[dir][1]
                            if 0<=m<len(grid) and 0<= n < len(grid[0]) and help[m][n] == 0 and grid[m][n] == save:
                                print(m,n)
                                savedirection = direction[dir][0] * 2 + direction[dir][1]
                                help[m][n] = 1
                                p, q = m, n
                                rode += 1
                                break
                        else: break
                        if abs(p-i) + abs(q-j) == 1 and rode >= 3: return True
        return False


a = Solution()
print(a.containsCycle([["a","b","b"],["b","z","b"],["b","b","a"]]))


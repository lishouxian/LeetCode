# 公司共有 n 个项目和 m 个小组，每个项目要不无人接手，要不就由 m 个小组之一负责。 
# 
#  group[i] 表示第 i 个项目所属的小组，如果这个项目目前无人接手，那么 group[i] 就等于 -1。（项目和小组都是从零开始编号的）小组可能存
# 在没有接手任何项目的情况。 
# 
#  请你帮忙按要求安排这些项目的进度，并返回排序后的项目列表： 
# 
#  
#  同一小组的项目，排序后在列表中彼此相邻。 
#  项目之间存在一定的依赖关系，我们用一个列表 beforeItems 来表示，其中 beforeItems[i] 表示在进行第 i 个项目前（位于第 i 个
# 项目左侧）应该完成的所有项目。 
#  
# 
#  如果存在多个解决方案，只需要返回其中任意一个即可。如果没有合适的解决方案，就请返回一个 空列表 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[
# 3,6],[],[],[]]
# 输出：[6,3,4,1,5,2,0,7]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[
# 3],[],[4],[]]
# 输出：[]
# 解释：与示例 1 大致相同，但是在排序后的列表中，4 必须放在 6 的前面。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= m <= n <= 3 * 104 
#  group.length == beforeItems.length == n 
#  -1 <= group[i] <= m - 1 
#  0 <= beforeItems[i].length <= n - 1 
#  0 <= beforeItems[i][j] <= n - 1 
#  i != beforeItems[i][j] 
#  beforeItems[i] 不含重复元素 
#  
#  Related Topics 深度优先搜索 图 拓扑排序 
#  👍 104 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def tp_sort(self, items, indegree, neighbors):
        q = collections.deque([])
        ans = []
        for item in items:
            if not indegree[item]:
                q.append(item)
        while q:
            cur = q.popleft()
            ans.append(cur)

            for neighbor in neighbors[cur]:
                indegree[neighbor] -= 1
                if not indegree[neighbor]:
                    q.append(neighbor)

        return ans

    def sortItems(self, n: int, m: int, group: List[int], pres: List[List[int]]) -> List[int]:
        max_group_id = m
        for project in range(n):
            if group[project] == -1:
                group[project] = max_group_id
                max_group_id += 1

        project_indegree = collections.defaultdict(int)
        group_indegree = collections.defaultdict(int)
        project_neighbors = collections.defaultdict(list)
        group_neighbors = collections.defaultdict(list)
        group_projects = collections.defaultdict(list)

        for project in range(n):
            group_projects[group[project]].append(project)

            for pre in pres[project]:
                if group[pre] != group[project]:
                    # 小组关系图
                    group_indegree[group[project]] += 1
                    group_neighbors[group[pre]].append(group[project])
                else:
                    # 项目关系图
                    project_indegree[project] += 1
                    project_neighbors[pre].append(project)

        ans = []

        group_queue = self.tp_sort([i for i in range(max_group_id)], group_indegree, group_neighbors)

        if len(group_queue) != max_group_id:
            return []

        for group_id in group_queue:

            project_queue = self.tp_sort(group_projects[group_id], project_indegree, project_neighbors)

            if len(project_queue) != len(group_projects[group_id]):
                return []
            ans += project_queue

        return ans
# leetcode submit region end(Prohibit modification and deletion)


a = Solution()

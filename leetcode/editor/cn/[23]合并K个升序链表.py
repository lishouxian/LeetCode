# 给你一个链表数组，每个链表都已经按升序排列。 
# 
#  请你将所有链表合并到一个升序链表中，返回合并后的链表。 
# 
#  
# 
#  示例 1： 
# 
#  输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
#  
# 
#  示例 2： 
# 
#  输入：lists = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  输入：lists = [[]]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  k == lists.length 
#  0 <= k <= 10^4 
#  0 <= lists[i].length <= 500 
#  -10^4 <= lists[i][j] <= 10^4 
#  lists[i] 按 升序 排列 
#  lists[i].length 的总和不超过 10^4 
#  
#  Related Topics 堆 链表 分治算法 
#  👍 1031 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        def merge(left, right):
            if right - left <= 2:
                node1 = lists[left]
                if right - left == 2:
                    node2 = lists[left + 1]
                else:
                    node2 = None
            else:
                mid = (left + right) // 2
                node1 = merge(left, mid)
                node2 = merge(mid, right)
            res = ListNode()
            head = res
            while node1 is not None or node2 is not None:
                if node1 is None:
                    head.next = node2
                    break
                elif node2 is None:
                    head.next = node1
                    break
                elif node1.val <  node2.val:
                    head.next = node1
                    node1 = node1.next
                else:
                    head.next = node2
                    node2 = node2.next
                head = head.next
            return res.next
        if not lists: return None
        return merge(0, len(lists))

        # leetcode submit region end(Prohibit modification and deletion)




a = Solution()

# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。 
# 
#  你应当保留两个分区中每个节点的初始相对位置。 
# 
#  
# 
#  示例: 
# 
#  输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5
#  
#  Related Topics 链表 双指针 
#  👍 282 👎 0
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def partition(self, head, x: int):
        l = ListNode(0)
        r = ListNode(0)
        a, b = l, r
        while head is not None:
            if head.val < x:
                l.next = head
                l = l .next
            else:
                r.next = head
                r = r.next
            head = head.next
        l.next, r.next = None, None
        l.next = b.next
        return a.next

# leetcode submit region end(Prohibit modification and deletion)


a = Solution()

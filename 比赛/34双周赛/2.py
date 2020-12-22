class LinkedList:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return self.val

class Solution:
    def findLatestStep(self, arr, m: int):
        help = [LinkedList(0) for i in range(len(arr)+2)]
        res = -1
        nextval = -1
        for i in range(len(arr)):
            lo = arr[i]
            if m == help[lo-1].val or m == help[lo+1] . val: res = i
            if help[lo-1].val == 0 and help[lo+1].val == 0:
                nextval = 1
                help[lo].val = nextval
                help[lo].next = help[lo]
            elif help[lo-1].val != 0 and help[lo+1].val != 0:
                nextval = help[lo-1].val + help[lo+1].val + 1
                help[lo - 1].next.val = help[lo + 1].next.val = nextval
                help[lo - 1].next.next , help[lo + 1].next.next = help[lo + 1].next , help[lo - 1].next
            elif help[lo-1].val != 0:
                nextval = help[lo - 1].val + 1
                help[lo - 1].next.val = help[lo].val = nextval
                help[lo - 1].next.next , help[lo].next = help[lo] , help[lo - 1].next
            elif help[lo+1].val != 0:
                nextval = help[lo + 1].val + 1
                help[lo + 1].next.val = help[lo].val = nextval
                help[lo + 1].next.next , help[lo].next = help[lo] , help[lo + 1].next
            if m == nextval: res = i + 1

            for i in range(len(help)):
                print(help[i].val)
        return res




a = Solution()

print(a.findLatestStep([2,1],2))
class Solution:
    def isMagic(self, target):

        n = len(target)
        root = [i + 1 for i in range(n)]

        def xipai(a):
            b = []
            for i in range(len(a)):
                if i % 2 == 1:
                    b.append(a[i])
            for i in range(len(a)):
                if i % 2 == 0:
                    b.append(a[i])
            return b

        def qupai(k, cards):
            cards = xipai(cards)
            temp = len(target) - len(cards)
            for i in range(k):
                if i == len(cards):
                    return True
                if cards[i] != target[temp + i]:
                    return False
            return qupai(k, cards[k:])

        root2 = xipai(root)
        for i in range(len(root)+1):
            if i == len(root):
                return True
            if root2[i] == target[i]:
                pass
            else:
                if i==0: return False
                if qupai(i, root2[i:]):
                    return True
                break
        return False


a = Solution()


def xipai(a):
    b = []
    for i in range(len(a)):
        if i % 2 == 1:
            b.append(a[i])
    for i in range(len(a)):
        if i % 2 == 0:
            b.append(a[i])
    return b

test = [i + 1 for i in range(5000)]
test = xipai(test)
print(a.isMagic([5,4,3,2,1]))

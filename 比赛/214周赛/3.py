class Solution:
    def maxProfit(self, inventory, orders: int) -> int:
        inventory.append(0)
        inventory.sort()
        ssum = 0
        for i in range(len(inventory) - 1, 0, -1):

            if orders >= (len(inventory) - i) * (inventory[i] - inventory[i - 1]):
                ssum += (len(inventory) - i) * (inventory[i] - inventory[i - 1]) \
                        * (inventory[i] + inventory[i - 1] + 1) //2
                orders -= (len(inventory) - i) * (inventory[i] - inventory[i - 1])
                ssum = ssum % (10 ** 9 + 7)
            else:
                largenum = orders // (len(inventory) - i) + 1
                largeaccount = orders % (len(inventory) - i)
                smallnum = orders // (len(inventory) - i)
                smallaccount = (len(inventory) - i) - largeaccount

                temp = inventory[i]
                ssum += largeaccount * (largenum) * (2 * temp - largenum + 1) // 2 + \
                        smallaccount * (smallnum) * (2 * temp - smallnum + 1) // 2
                ssum = ssum % (10 ** 9 + 7)
                return ssum
        return ssum


a = Solution()
print(a.maxProfit([1000000000], orders = 1000000000))

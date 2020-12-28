class Solution:
    def maximizeXor(self, nums, queries):
        nums.sort()
        target = 0
        temp = []
        res = []
        for i in range(len(nums)):
            if nums[i] & 2 ** target >0:
                temp.append(i)
                target += 1

        for i in range(len(queries)):
            m =  bin(queries[i][0])[2:]
            if '0' in m:
                index = len(m) -  m.index('0') - 1
            else:
                index = len(m)
            max_num = -1

            if index >= len(temp):
                ranges = 0
            else:
                ranges = temp[index]
            if ranges < queries[i][1]:
                for j in range(ranges,len(nums)):
                    if nums[j] > queries[i][1]:
                        break
                    else:
                        max_num = max(max_num, queries[i][0] ^ nums[j] )
            else:
                for j in range(len(nums)):
                    if nums[j] > queries[i][1]:
                        break
                    else:
                        max_num = max(max_num, queries[i][0] ^ nums[j] )

            res.append(max_num)
        return res









a = Solution()
print(a.maximizeXor(nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]))
class Solution:
    def minDeletions(self, s: str) -> int:
        nums = [0 for i in range(26)]
        for str in s:
            nums[ord(str) - ord('a')] += 1
        nums.sort()
        print(nums)
        top, count = -1, 0
        for i in range(25, -1, -1):
            if nums[i] != -1:
                if top == -1 or top > nums[i]:
                    top = nums[i]
                elif top == 0:
                    count += nums[i] - top
                else:
                    top = top - 1
                    count += max(nums[i] - top,0)
        return count


a = Solution()
print(a.minDeletions("ceabaacb"))

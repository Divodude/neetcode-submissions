class Solution:
    def canJump(self, nums: List[int]):

        i = 0
        n = len(nums)

        while i < n:

            jump = i
            farthest = i + nums[i]

            for j in range(nums[i] + 1):
                if i + j >= n - 1:
                    return True

                if i + j + nums[i + j] > farthest:
                    farthest = i + j + nums[i + j]
                    jump = i + j

            if jump == i:
                return False

            i = jump

        return False
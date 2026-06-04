class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []
        n = len(nums)
        nums.sort()

        def rec(i, c_sum, arr):
            if c_sum > target:
                return

            if c_sum == target:
                self.ans.append(arr.copy())
                return

            if i >= n:
                return

            arr.append(nums[i])
            rec(i + 1, c_sum + nums[i], arr)
            arr.pop()

           
            j = i + 1
            while j < n and nums[j] == nums[i]:
                j += 1

            rec(j, c_sum, arr)

        rec(0, 0, [])
        return self.ans
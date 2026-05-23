class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        vote = [[0,0],[0,0]]

        for i in nums:

            if vote[0][0] == i:
                vote[0][1] += 1

            elif vote[1][0] == i:
                vote[1][1] += 1

            elif vote[0][1] <= 0:
                vote[0][0] = i
                vote[0][1] = 1

            elif vote[1][1] <= 0:
                vote[1][0] = i
                vote[1][1] = 1

            else:
                vote[0][1] -= 1
                vote[1][1] -= 1

        n = len(nums)
        ans = []

        for can in vote:
            if nums.count(can[0]) > n // 3 and can[0] not in ans:
                ans.append(can[0])

        return ans
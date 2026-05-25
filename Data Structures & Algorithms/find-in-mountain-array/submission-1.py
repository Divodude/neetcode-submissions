class Solution:
    def findInMountainArray(self, target: int, MountainArray: 'MountainArray') -> int:

        n = MountainArray.length()

        start = 0
        end = n - 1

        def bs(start, end, reverse=False):

            while start <= end:

                mid = (start + end) // 2
                val = MountainArray.get(mid)

                if val == target:
                    return mid

                if not reverse:

                    if val < target:
                        start = mid + 1
                    else:
                        end = mid - 1

                else:

                    if val < target:
                        end = mid - 1
                    else:
                        start = mid + 1

            return float("inf")

        mountain_idx = 0

        while start < end:

            mid = (start + end) // 2

            if MountainArray.get(mid) < MountainArray.get(mid + 1):
                start = mid + 1
            else:
                end = mid

        mountain_idx = start

        ans = min(
            bs(0, mountain_idx),
            bs(mountain_idx + 1, n - 1, True)
        )

        if ans == float("inf"):
            return -1

        return ans
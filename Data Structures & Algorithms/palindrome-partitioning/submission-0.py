class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)

        def rec(start, path):

            if start == n:
                ans.append(path[:])
                return

            for end in range(start, n):

                sub = s[start:end+1]

                if sub == sub[::-1]:

                    path.append(sub)

                    rec(end + 1, path)

                    path.pop()

        rec(0, [])

        return ans
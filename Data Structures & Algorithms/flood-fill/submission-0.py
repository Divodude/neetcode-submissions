class Solution:
    def floodFill(self, image, sr, sc, color):
        old_color = image[sr][sc]

       
        if old_color == color:
            return image

        m = len(image)
        n = len(image[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return

            if image[r][c] != old_color:
                return

            image[r][c] = color

          
            dfs(r - 1, c)
           
            dfs(r + 1, c)
           
            dfs(r, c - 1)
           
            dfs(r, c + 1)

        dfs(sr, sc)

        return image
from collections import Counter

class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        count = Counter(tiles)

        def dfs(counter):
            total = 0
            for ch in counter:
                if counter[ch] == 0:
                    continue
                # Choose ch
                total += 1
                counter[ch] -= 1
                total += dfs(counter)
                counter[ch] += 1  # Backtrack
            return total

        return dfs(count)

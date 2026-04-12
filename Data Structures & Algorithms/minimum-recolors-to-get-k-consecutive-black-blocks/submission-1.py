class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        left, right = 0, 0
        min_count = float("inf")
        cur_count = 0


        while right - left + 1 <= k:

            if blocks[right] == "W":
                cur_count += 1
                
            right += 1
            
        min_count = cur_count

        for right in range(k, n):

            if blocks[left] == "W":
                cur_count -= 1

            if blocks[right] == "W":
                cur_count += 1
            
            left += 1
            right += 1
            min_count = min(min_count, cur_count)
        
        return min_count
            

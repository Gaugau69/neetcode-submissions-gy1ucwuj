class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        
        while len(stones) > 1:
            print(stones)
            x = stones.pop()
            y = stones.pop()

            if x < y or y < x:
                stones.append(abs(y - x))   
                stones.sort()         

        return stones[0] if stones else 0
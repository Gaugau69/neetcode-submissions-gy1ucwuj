class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n =len(customers)
        res = 0

        for i in range(n):
            
            if grumpy[i] == 0:
                res += customers[i]
        
        left, right = 0, 0
        cur_client = res

        while right -left + 1 <= minutes:
            if grumpy[right] == 1:
                cur_client += customers[right]
            
            right += 1
        
        max_client = cur_client

        for right in range(minutes, n):

            if grumpy[left] == 1:
                cur_client -= customers[left]

            if grumpy[right] == 1:
                cur_client += customers[right]

            max_client = max(max_client, cur_client)
            
            left += 1
            right += 1
            
        return max_client







            



            
            
            


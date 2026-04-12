class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        left, right = 0, 0
        cur_sum = 0
        res = 0

        while right -left + 1 <= k:
            cur_sum += arr[right]
            right += 1
            
        if cur_sum >= k * threshold:
            res += 1
        
        for right in range(k, n):
            cur_sum -= arr[left]
            cur_sum += arr[right]

            if cur_sum >= k * threshold:
                res += 1
            
            left += 1
        
        return res

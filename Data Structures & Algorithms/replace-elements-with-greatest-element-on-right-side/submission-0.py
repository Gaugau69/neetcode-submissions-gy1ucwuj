class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi = arr[-1]

        for i in range(len(arr) - 2, -1, -1):
            c = arr[i] 
            arr[i] = maxi
            maxi = max(c, maxi)

        arr[-1] = -1

        return arr
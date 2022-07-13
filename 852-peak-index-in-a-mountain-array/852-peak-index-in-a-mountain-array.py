class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        hf = int(len(arr)/2)
        L, R = arr[:hf], arr[hf+1:]
        
        if len(arr)==1:
            return 0
        elif len(arr)==2:
            return 1 if arr[1]>arr[0] else 0
        #elif len(arr)==3:
        #    if arr[0]>arr[1]:
        #        return 0
        #    else:
        #        return 2 if arr[2]>arr[1] else 1
        elif arr[hf]>arr[hf+1] and arr[hf]>arr[hf-1]:
            return hf
        elif arr[hf]>arr[hf-1]:
            return hf + 1 + self.peakIndexInMountainArray(R)
        else:
            return self.peakIndexInMountainArray(L)
        
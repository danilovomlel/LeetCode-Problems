class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        auxj = 0
        if len(nums2)==0:
            return nums1
        
        i= 0
        while(i<m+n):
            if nums1[i]>nums2[auxj]:
                nums1[i:] = [nums2[auxj]] + nums1[i:m+n-1]
                auxj+= 1
            else:
                i+= 1
            if auxj == n:
                break
        
        if auxj<n:
            nums1[m+auxj:] = nums2[auxj:]
            

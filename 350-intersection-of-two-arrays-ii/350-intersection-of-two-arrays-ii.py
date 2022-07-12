class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        ans = []
        auxj = 0
        
        for i in range(len(nums1)):
            for j in range(auxj, len(nums2)):
                if nums1[i] == nums2[j]:
                    ans.append(nums1[i])
                    auxj = j+1
                    break
        return ans
        
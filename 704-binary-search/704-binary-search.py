class Solution:
   
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums)==1:
            return (0 if nums[0]==target else -1)
        
        hf_sz = int(len(nums)/2)
        L, R = nums[:hf_sz], nums[hf_sz:]
        
        
        if R and target>R[0]:
            if self.search(R,target)>=0:
                return (hf_sz + self.search(R, target) if len(R)>1 else -1)
            else:
                return -1
        elif L and target<L[-1]:
            print(2)
            return (self.search(L, target) if len(L)>1 else -1)
        else:
            if L and target==L[-1]:
                return hf_sz-1
            elif R and target==R[0]:
                return hf_sz
            else:
                return -1
        print(3)
        
        
            
        
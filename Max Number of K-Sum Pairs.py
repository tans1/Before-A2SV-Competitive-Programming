class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = 0
        temporaryDIC = {}
        
        for i in nums:
            j = k -i
            if j in temporaryDIC and temporaryDIC[j] >0:
                counter +=1
                temporaryDIC[j] -=1
            else:
                if i not in temporaryDIC:
                    temporaryDIC[i] = 0
                temporaryDIC[i] +=1
        return counter
                    

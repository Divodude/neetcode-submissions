class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote=[0,0]
        for i in nums:
            print(vote)
            if vote[1]==0:
                vote[0]=i
                vote[1]+=1
            if vote[0]==i:
                vote[1]+=1
            elif vote[0]!=i:
                vote[1]-=1
        return vote[0]

        
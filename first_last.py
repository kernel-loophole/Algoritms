class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if target not in nums:
            return [-1,-1]
        list_index=[]
        count_len=0
        for i in range(0,len(nums)):
            if nums[i]==target:
                count_len+=1
                list_index.append(i)
        if count_len==1:
            list_index.append(list_index[0])
            return list_index
        list_index_test=list_index[-1]
        final_list_output=[]
#        print(list_index_test)
        final_list_output.append(list_index[0])
        final_list_output.append(list_index[-1])
        return final_list_output
if __name__=="__main__":
    s=Solution()
    print(s.searchRange([3,3,3],3))
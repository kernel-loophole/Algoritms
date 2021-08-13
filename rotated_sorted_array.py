class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # sub_array_one=nums[0:3]
        # sub_array_two=nums[3::]
        # print(sub_array_one)
        # print(sub_array_two)
        # final_array=sub_array_two+sub_array_one
        # print(final_array)
        if target not in nums:
            return -1
        return nums.index(target)
if __name__=="__main__":
    s=Solution()
    print(s.search([0,1,2,4,5,6,7],23))
        
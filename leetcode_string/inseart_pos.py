class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        check=False
        if target in nums:
            check=True
        for i in range(0,len(nums)):
            if target==nums[i]:
                return i
            if not check:
                if nums[i]>target:
                    return i
        return len(nums)
if __name__=="__main__":
    s=Solution()
    print(s.searchInsert([1,3,5,6],7))            
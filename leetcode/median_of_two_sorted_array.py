class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_list=nums2+nums1
        sorted_list.sort()
        if len(sorted_list)%2!=0:
            find_index=int(len(sorted_list)//2)
            output=sorted_list[find_index]
            return output
        find_index=int(len(sorted_list)//2)
        output=sorted_list[find_index-1]+sorted_list[find_index]
        print(sorted_list[find_index-1],sorted_list[find_index])
        print("outside if",sorted_list[find_index-1],output)
        return output/2
        


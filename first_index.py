class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        return haystack.index(needle)
if __name__=="__main__":
    s=Solution()
    print(s.strStr("leetcode","leeto"))
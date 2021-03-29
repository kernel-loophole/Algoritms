class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        word_total_legth=len(words[0])
        word_i_lengt=len(words)
        Target_String=""
        for string in words:
            Target_String+=string
        # print(Target_String+Target_String)
        indexies=[]
        Target_String+=Target_String
        final_len=word_total_legth*word_i_lengt
        # if final_len>=len(s):
        #     return []
        for i in range(0,len(s)):
            try:
                #print("Target string {0} and cal string {1}".format(Target_String,s[i:final_len]))
                if s[i:final_len+i] in Target_String and len(s[i:final_len+i])==final_len:
                    print(s[i:final_len+i])

            except:
                pass    

if __name__=="__main__":
    s=Solution()
    print(s.findSubstring("foobar",['foo','bar']))
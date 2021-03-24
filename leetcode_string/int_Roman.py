"""Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M."""
def intToRoman( num: int) -> str:
    Mapping_Symbols={1:"I",5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
    Defulat_Symbols={4:"IV",9:"IX", 49:"IL", 99:"IC", 499:"ID"}
    if num in Mapping_Symbols:
        return Mapping_Symbols[num]
    Mapping_list={}
    #list for key mapping
    List_keys=[]
    #calclaute difference between each point 
    for i in Mapping_Symbols.keys():
        Mapping_list[abs(num-i)]=i
    print(Mapping_list)
    len_loops=len(Mapping_list.keys())
    # Mapping_list=sorted(Mapping_list)
    for k in range(0,len_loops):
        min_diff=min(Mapping_list.keys())
        List_keys.append(min_diff)
        Mapping_list = Mapping_list.pop(min_diff)
print(intToRoman(4))
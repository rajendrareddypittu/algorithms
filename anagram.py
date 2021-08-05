
"""
Input: strs = ["set","tub","but","tac","tab","est","cat","tes"]
Output: [["set","tes","est"],["tub","but"],["tab"],["cat","tac"],[""]]

public List<List<String>> groupAnagrams(String[] strs){
   //implementation
}


"""


def anag(str_list):
    dict_ang={}
    for ind,source_strng in enumerate(str_list):   #set
        remaining_str_list=str_list.copy()
        templist=[source_strng]
        templist.clear()
        templist=[source_strng]
        remaining_str_list.remove(source_strng)  #["tub","but","tac","tab","est","cat","tes"]]
        for target_str in remaining_str_list: #tub
            is_anag=0  # source , tager
            for each_char_source in source_strng: #s
                if each_char_source in target_str: #target_str =tub
                    is_anag=1
                    continue
                else :
                    is_anag=0
                    break
                    print("not an aangram")
            
            if is_anag==1:
                templist.append(target_str)
        print(templist)    
    return dict_ang            
            #end of this loop  we decide source_strng is anagram or not
        # This look iterate for all strings except source         
    #This loop helps to iterate through all strings to comapre and identify     
dict_ang=anag(["sett","tub","but","tac","tab","esttt","cat","tes"])   
print(dict_ang)        
            
        
        
        

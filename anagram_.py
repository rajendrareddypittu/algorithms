
# Online Python - IDE, Editor, Compiler, Interpreter

def getchar_count(word):
    char_dict={}
    for char in word:
        char_dict.setdefault(char,0)
        char_dict[char]+=1
    return char_dict  
def isanagram(sw,tw):
    res=False
    if len(sw)==len(tw):
        for k,v in sw.items():
            if sw[k]==tw[k]:
                print("sw[k]==tw[k]",sw[k],tw[k])
                #return True
            else:
                return False
    else:
        return False
    return True    
def anagramlist(string_list):
    word_char_dict={}
    if len(string_list)<1:
        return None
    else:
        for word in string_list:
            print("for word in string_list:",word)
            
            charCount=getchar_count(word)
            print("charCount",charCount)
            word_char_dict[word]=charCount
            
        print("word_char_dict",word_char_dict)
        
        anagram_dict={}
        processed_list=[]
        
        
        for source_word in word_char_dict:
            
            #del word_char_dict_copy[source_word]
            if source_word in processed_list:
                continue
            else:
                anagram_dict.setdefault(source_word,[])
                processed_list.append(source_word)
                word_char_dict_copy=word_char_dict.copy()
                for old_w in processed_list:
                    del word_char_dict_copy[old_w]
                for target_word in word_char_dict_copy:
                    print(word_char_dict[source_word],word_char_dict[target_word])
                    res=isanagram(word_char_dict[source_word],word_char_dict[target_word])
                    print("result for source_word,target_word",source_word,target_word,res)
                    if (res):
                        anagram_dict.setdefault(source_word,[]).append(target_word)
                        #del word_char_dict_copy[target_word]
                        processed_list.append(target_word)
                    else:
                        continue
        print("anagram_dict ",anagram_dict)            
                    
            
anagramlist(['eatta','aet','ate','foo'])            
            
            

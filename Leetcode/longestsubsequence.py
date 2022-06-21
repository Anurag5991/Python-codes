def longestCommonSubsequence(text1, text2):
    str1 = ""
        
    if len(text1) > len(text2):
        for i in text2:
            if i in text1:
                str1 += i
    else:           
        for i in text1:
            if i in text2:
                str1 += i
      
    return len(str1)

print((longestCommonSubsequence("abedc", "ace")))
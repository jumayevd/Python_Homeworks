
def inserting_underscore(txt):
    vowels = "aeiou"
    res = []
    counter = 0
    for i in range(len(txt)):
        counter += 1
        res.append(txt[i])
        if counter >= 3 and txt[i] not in vowels and i != len(txt) - 1:
            vowels += txt[i]
            res.append("_")
            counter = 0
        
    
    print("".join(res))
   


txt = 'abcabcdabcdeabcdefabcdefg'

inserting_underscore(txt)
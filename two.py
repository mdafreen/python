global v ; 
v= 0;
global c;   
c= 0;
str = "This is a really simple sentence";   

#Converting entire string to lower case to reduce the comparisons   

str = str.lower();   
def count(str,v,c):
    for i in range(0,len(str)):    

 #Checks whether a character is a vowel   

        if str[i] in ['a',"e","i","o","u"]:   

           v = v + 1;   

        else:   
            c= c + 1;   
    result={"vowels":v,"consonant":c}
    return result

print(count(str,0,0));   
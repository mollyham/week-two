
my_vowels=("aeiou")
my_strg =str("joel is evil")
a_strg=("")
a_int = 0

for x in my_strg:
    if x in my_vowels:
        if x in a_strg:
            a_int +=1 
            #record duplicate
            pass
        else:
            a_strg += x
my_tupple=(a_int,a_strg)                       
print(my_tupple)

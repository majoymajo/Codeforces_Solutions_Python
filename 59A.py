-- Word --
word = input()
minus = 0
mayus = 0
 
for i in word:
    if i.islower():
        minus += 1
    else:
        mayus += 1
if minus >= mayus:
    print(word.lower())
else:
    print(word.upper())

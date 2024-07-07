def ispalidrome(text):
    p1 = 0
    p2 = len(text)-1
    if len(text)==1:
        return True
    for val in range(0,len(text)-1):
         if text[p1]==text[p2]:
             text = text[p1:p2]
             print(text)
         p1+=1
         p2-=1
    return False
result= "kayakk"
output = ispalidrome(result)
print(output)
txt=input("Python is the best")
k=list(txt)
i=0
for h in k:
if (h>='a' and h<='m') or (h>='A'and h<='M'):
   k[i]= chr(ord(h)+13)
elif (h>='n' and h<='z')or(h>='N'and h<='Z'):
   k[i]=chr(ord(h)-13)
   i=i+1
txt="".join(k)
print("The encrypted text is:"+txt)
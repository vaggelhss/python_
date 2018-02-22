number=int(input("Give a number:"))
number_M=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),
          (40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]

def numbernewR(number):
   R=''
while(number>0 and number<=1.000.000):
 for i,h in number_M:
   while number >= i:
     R=R+h
     number=number-i
  return R
print (numbernewR(number))
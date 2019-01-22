#ASKISI 2

def factorization(n):
    i = 2   
    factors = []          
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


number = input("Enter a number; type 'exit' to close the program.\n")
if number == "exit": quit()
result = factorization(int(number))
printlist = list()
temp = result[0]
printlist.append([temp,result.count(temp)])
for i in result[1:]:
    if i != temp:
        printlist.append([i,result.count(i)])
        temp = i
for i in printlist:
    if i[1] > 1:
        print("(", i[0], "**", i[1], ")")
    else:
        print("(",i[0],")")

while True:
    number = input("Enter a number; type 'exit' to close the program.\n")
    if number == "exit": quit()
    result = factorization(int(number))
    printlist = list()
    temp = result[0]
    printlist.append([temp,result.count(temp)])
    for i in result[1:]:
        if i != temp:
            printlist.append([i,result.count(i)])
            temp = i
    for i in printlist:
        if i[1] > 1:
            print("(", i[0], "**", i[1], ")")
        else:
            print("(",i[0],")")
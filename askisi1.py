#ASKISI 1 
stack = [[1,5],[10,20],[1,6],[16,19],[5,11], [50,56]]

data_list = list()

for i in stack:
	data_list.append(i[0])

new_list = []

while data_list:
	counter = 0
	ccounter = 0
	minimum = data_list[0]
	for x in data_list:
		if x < minimum:
			minimum = x
			ccounter = counter
		counter += 1
	new_list.append(stack[ccounter])
	data_list.remove(minimum)
	stack.remove(stack[ccounter])

final = list()
final.append(new_list[0])
new_list.remove(new_list[0])

for i in new_list:
	if final[-1][1] < i[0]:
		final.append(i)
  	elif final[-1][1] < i[1]:
  		final[-1][1] = i[1]

sum = 0

for i in final:
	sum += i[1] - i[0]

print(sum)

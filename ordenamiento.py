x = [1,2,3,22,2003,20,39,10,5,6,7,23,54,65]
list2 = []
def getMin(list):
	temp = "a"
	for num in list:
		if(temp == "a"):
			temp = num
		if(num < temp):
			temp = num
	return temp
def getMax(list):
	temp = 0
	for num in list:
		if(num > temp):
			temp = num
	return temp
while not len(x) == 0:
	min = getMax(x)
	list2.append(min)
	x.remove(min)
print(list2)

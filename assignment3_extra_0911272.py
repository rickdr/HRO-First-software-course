number = input("choose a number!")

for i in range(0, number):
	print("*"+((number-1)-i) * '*' + i * " " + "*")

print((number+1) * '*')
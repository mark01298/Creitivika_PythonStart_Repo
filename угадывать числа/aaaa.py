import random
a = random.randint(0,1000000)
b = 1000
popitka = 0
while a != b:
	b = int(input("Какое число загадано?"))
	popitka = popitka + 1
	print(popitka,"попытка")
	if a > b:
		print("больше")
	elif a == b:
		print("БРАВО!!!")
	else:
		print("меньше")
			
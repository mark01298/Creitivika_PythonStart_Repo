import random
w = open("a.txt","r",encoding = "utf-8")
num1 = w.read()
a = random.randint(1,100)
b = random.randint(1,100)
c = random.randint(1,100)
d = random.randint(1,100)
e = random.randint(1,100)
f = random.randint(1,100)
g = random.randint(1,100)
h = random.randint(1,100)
i = random.randint(1,100)
j = random.randint(1,100)
q = input("Угадайте число от 1 до 100")
if q == str(a) or q == str(b) or q == str(c) or q == str(d) or q == str(e) or q == str(f) or q == str(g) or q == str(h) or q == str(i) or q == str(j):
    print("GOOD!")
    z = int(num1) + 1
    p = open("a.txt","w",encoding = "utf-8")
    print("Это ваша",z,"победа")
    p.write(str(z))
    p.close()



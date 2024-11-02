import time
v = input("что написать в файл?")
a = open(".txt","w",encoding = "utf-8")
print("нетушки,я напишу 1 2 3 4 5 6 7 8 9 10")
time.sleep(2)
print("хотяяяя....")
time.sleep(2)
print("я лучше напишу что люблю гулять по улице")
time.sleep(2)
print("или лучше....")
time.sleep(2)
print("напишу что люблю лето)")
a.write("я люблю лето!")
a.close()








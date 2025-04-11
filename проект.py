#Есть 10 рандомных чисел от 0 до 100.
#Человек пишет какое то число, и пока он не угадает какое то из 10 чисел
#программа будет его переспрашивать, когда он выиграет программа напишет
#"вы выиграли!" и нужно запускать код сначала.За победы будут даваться очки.
#Колличество очков зависит от колличества попыток за которое человек
#отгадал одно из чисел. Колличество побед тоже будет записываться, и после
#выигрыша будет написано какая это победа по счету.
import random
import pyautogui as p
difficultylevel = input("Какой выбираете уровень сложности? Есть легкий, средний и сложный")
if difficultylevel == "средний":
    a1 = random.randint(1,100)
    a2 = random.randint(1,100)
    a3 = random.randint(1,100)
    a4 = random.randint(1,100)
    a5 = random.randint(1,100)
    a6 = random.randint(1,100)
    a7 = random.randint(1,100)
    a8 = random.randint(1,100)
    a9 = random.randint(1,100)
    a10 = random.randint(1,100)
    popitka = 0
    chislo = 0
    ochki = 0
    win = 0
    while int(chislo) != a1 and int(chislo) != a2 and int(chislo) != a3 and int(chislo) != a4 and int(chislo) != a5 and int(chislo) != a6 and int(chislo) != a7 and int(chislo) != a8 and int(chislo) != a9 and int(chislo) != a10:
        chislo = input("Угадайте число от 1 до 100")
        popitka = popitka + 1
    print("вы выиграли! У вас на это потребовалось "+str(popitka)+" попыток")
    win = win + 1
    if popitka >= 50:
        ochki = ochki - 100
    elif popitka >= 10 and popitka < 50:
        ochki = ochki + 10
    elif popitka < 10 and popitka >= 5:
        ochki = ochki + 100
    elif popitka > 1 and popitka < 5:
        ochki = ochki + 500
    elif popitka == 1:
        ochki = ochki + 1000
    file1_0 = open("очки.txt","r", encoding = "utf-8")
    file1_1 = file1_0.read()
    ochki2 = ochki + int(file1_1)
    file1_2 = open("очки.txt","w", encoding = "utf-8")
    file1_2.write(str(ochki2))
    file1_2.close()
    print("У вас уже "+str(ochki2)+" очков")

    file2_0 = open("победы.txt","r", encoding = "utf-8")
    file2_1 = file2_0.read()
    win2 = win + int(file2_1)
    file2_2 = open("победы.txt","w", encoding = "utf-8")
    file2_2.write(str(win2))
    file2_2.close()
    print("Это ваша "+str(win2)+" победа")
if difficultylevel == "легкий":
    a1 = random.randint(1,10)
    a2 = random.randint(1,10)
    a3 = random.randint(1,10)
    a4 = random.randint(1,10)
    a5 = random.randint(1,10)
    a6 = random.randint(1,10)
    a7 = random.randint(1,10)
    a8 = random.randint(1,10)
    a9 = random.randint(1,10)
    a10 = random.randint(1,10)
    popitka = 0
    chislo = 0
    ochki = 0
    win = 0
    while int(chislo) != a1 and int(chislo) != a2 and int(chislo) != a3 and int(chislo) != a4 and int(chislo) != a5 and int(chislo) != a6 and int(chislo) != a7 and int(chislo) != a8 and int(chislo) != a9 and int(chislo) != a10:
        chislo = input("Угадайте число от 1 до 10")
        popitka = popitka + 1
    print("вы выиграли! У вас на это потребовалось "+str(popitka)+" попыток")
    win = win + 1
    if popitka >= 50:
        ochki = ochki - 10
    elif popitka >= 10 and popitka < 50:
        ochki = ochki + 1
    elif popitka < 10 and popitka >= 5:
        ochki = ochki + 10
    elif popitka > 1 and popitka < 5:
        ochki = ochki + 50
    elif popitka == 1:
        ochki = ochki + 100
    file1_0 = open("очки.txt","r", encoding = "utf-8")
    file1_1 = file1_0.read()
    ochki2 = ochki + int(file1_1)
    file1_2 = open("очки.txt","w", encoding = "utf-8")
    file1_2.write(str(ochki2))
    file1_2.close()
    print("У вас уже "+str(ochki2)+" очков")

    file2_0 = open("победы.txt","r", encoding = "utf-8")
    file2_1 = file2_0.read()
    win2 = win + int(file2_1)
    file2_2 = open("победы.txt","w", encoding = "utf-8")
    file2_2.write(str(win2))
    file2_2.close()
    print("Это ваша "+str(win2)+" победа")
if difficultylevel == "сложный":
    a1 = random.randint(1,1000)
    a2 = random.randint(1,1000)
    a3 = random.randint(1,1000)
    a4 = random.randint(1,1000)
    a5 = random.randint(1,1000)
    a6 = random.randint(1,1000)
    a7 = random.randint(1,1000)
    a8 = random.randint(1,1000)
    a9 = random.randint(1,1000)
    a10 = random.randint(1,1000)
    popitka = 0
    chislo = 0
    ochki = 0
    win = 0
    while int(chislo) != a1 and int(chislo) != a2 and int(chislo) != a3 and int(chislo) != a4 and int(chislo) != a5 and int(chislo) != a6 and int(chislo) != a7 and int(chislo) != a8 and int(chislo) != a9 and int(chislo) != a10:
        print(a1)
        chislo = input("Угадайте число от 1 до 1000")
        popitka = popitka + 1
    print("вы выиграли! У вас на это потребовалось "+str(popitka)+" попыток")
    win = win + 1
    if popitka >= 50:
        ochki = ochki - 10
    elif popitka >= 10 and popitka < 50:
        ochki = ochki + 1000
    elif popitka < 10 and popitka >= 5:
        ochki = ochki + 10000
    elif popitka > 1 and popitka < 5:
        ochki = ochki + 50000
    elif popitka == 1:
        ochki = ochki + 100000
    file1_0 = open("очки.txt","r", encoding = "utf-8")
    file1_1 = file1_0.read()
    ochki2 = ochki + int(file1_1)
    file1_2 = open("очки.txt","w", encoding = "utf-8")
    file1_2.write(str(ochki2))
    file1_2.close()
    print("У вас уже "+str(ochki2)+" очков")

    file2_0 = open("победы.txt","r", encoding = "utf-8")
    file2_1 = file2_0.read()
    win2 = win + int(file2_1)
    file2_2 = open("победы.txt","w", encoding = "utf-8")
    file2_2.write(str(win2))
    file2_2.close()
    print("Это ваша "+str(win2)+" победа")
    


    



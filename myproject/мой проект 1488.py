#гугл x=572, y=1047
#поисковая строка x=893, y=442
#файл x=718, y=165
#где снова открыть этот запрос x=761, y=1047
#открыть окно x=823, y=944
import time
import pyautogui as p
druzhit = input("Привет! Давай дружить?")
if druzhit == "нет":
    input("Ну тогда пока")
if druzhit == "давай":
    ima = input("Как тебя зовут?")
    old = input("А сколько тебе лет?")
    gugl = input("Давай что-нибудь загуглим?")
    if gugl == "нет":
        game = input("тогда давай поиграем в игру?")
        if game == "давай":
            print("Как только я напишу 'go!' ты должен быстро что-то ответить")
            gotovnost = input("готов?")
            if gotovnost == "да":
                time.sleep(11)
                input("go!")
                print("А ты быстрый!")
            if gotovnost == "нет":
                input("Тогда напиши когда будешь готов")
                input("Точно готов?")
                time.sleep(11)
                input("go!")
                print("А ты быстрый!")
                time.sleep(3)
    if gugl == "давай":
        chtoguglit = input("Что будем гуглить?")
        time.sleep(3)
        p.moveTo(572,1047)
        time.sleep(2)
        p.doubleClick()
        time.sleep(2)
        p.moveTo(893,500)
        time.sleep(2)
        p.click()
        time.sleep(2)
        p.write(chtoguglit)
        time.sleep(2)
        p.press("enter")
        time.sleep(10)
        writeinfile = input("Записать ли в файл всю информацию?")
        if writeinfile == "да":
            time.sleep(2)
            p.moveTo(761,1047)
            time.sleep(2)
            p.moveTo(823,944)
            time.sleep(2)
            p.click()
            time.sleep(2)
            p.hotkey("ctrl","a")
            time.sleep(2)
            p.hotkey("ctrl","c")
            
print("Ну все, я устал! Ну все равно уже позно, так что до завтра!")
        
        
    
    
















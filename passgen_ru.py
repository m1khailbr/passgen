import random
import time
file = open("pass.txt", "w")
num_words = ["1","2","3","4","5","6","7","8","9","0"]
words = ["1","2","3","4","5","6","7","8","9","0","A","B","C","D","E","F","G","H",
         "I","J","K","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a",
         "b","c","d","e","f","g","h","i","j","k","m","n","o","p","q","r","s","t",
         "u","v","w","x","y","z","!","@","#","$","*","(",")"]
print("1 Пароль из букв, цифр и символов")
print("2 Пароль из цифр")
choose = int(input("Выберите режим: "))
if (choose == 1):
    le = int(input("Введите длину пароля: "))
    for i in range(le):
        a = random.randint(0,65)
        b = words[a]
        file.write(b)
if (choose == 2):
    le = int(input("Введите длину пароля: "))
    for i in range(le):
        a = random.randint(0,9)
        b = num_words[a]
        file.write(b)


file.close()
file = open("pass.txt")
f_read = file.read()
print("Ваш пароль:")
print(f_read)
print("Пароль записан в файл 'pass.txt'")
time.sleep(5)

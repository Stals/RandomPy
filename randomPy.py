import random

word1 = open('word1.txt','r').readlines()
word2 = open('word2.txt','r').readlines()
word3 = open('word3.txt','r').readlines()
word4 = open('word4.txt','r').readlines()

# Бесконечный цикл пока не получим число строк
while True:
    numberOfLines = input("Веедите кол-во строк которое хотите получить:")
    if numberOfLines.isdigit():
        break

for i in range(int(numberOfLines)):
    # Выводит на печать случайные слова из того списка что мы только что прочитали
    # [:-1] используется для того чтобы не печатать последний символ - которым является символ переноса строки
    randomWord1 = random.choice(word1)[:-1]
    randomWord2 = random.choice(word2)[:-1]
    randomWord3 = random.choice(word3)[:-1]
    randomWord4 = random.choice(word4)[:-1]
    print("{0} {1}, который любит {2} {3}.".format(randomWord1, randomWord2, randomWord3, randomWord4))

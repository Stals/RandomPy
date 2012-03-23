import random
# read().splitlines() позволяет получить список строк без '\n' на конце в отличии от просто readlines()
word1 = open('word1.txt','r').read().splitlines()
word2 = open('word2.txt','r').read().splitlines()
word3 = open('word3.txt','r').read().splitlines()
word4 = open('word4.txt','r').read().splitlines()

# Бесконечный цикл пока не получим число строк
while True:
    numberOfLines = input("Веедите кол-во строк которое хотите получить:")
    if numberOfLines.isdigit():
        break

for i in range(int(numberOfLines)):
    # Выводит на печать случайные слова из того списка что мы только что прочитали
    randomWord1 = random.choice(word1)
    randomWord2 = random.choice(word2)
    randomWord3 = random.choice(word3)
    randomWord4 = random.choice(word4)
    print("{0} {1}, который любит {2} {3}.".format(randomWord1, randomWord2, randomWord3, randomWord4))

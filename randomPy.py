import random
# Читаем файлы и получаем случайное слово
word1 = random.choice( open("word1.txt").read().splitlines() )
word2 = random.choice( open("word2.txt").read().splitlines() )
word3 = random.choice( open("word3.txt").read().splitlines() )
word4 = random.choice( open("word4.txt").read().splitlines() )	
# Напечатаем случайную фразу 
print("{0} {1}, который любит {2} {3}.".format(word1, word2, word3, word4))

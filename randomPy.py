import random;

f = open('numb1.txt', 'r');
word1=f.readlines();

f = open('numb2.txt','r');
word2=f.readlines();

f = open('numb3.txt','r');
word3=f.readlines();

f = open('numb4.txt','r');
word4=f.readlines();

#Выводит на печать случайные слова из того списка что мы только что прочитали
#[:-1] используется для того чтобы не печатать последний символ - которым является символ переноса строки
print("{0} {1}, который любит {2} {3}.".format(random.choice(word1)[:-1],random.choice(word2)[:-1],random.choice(word3)[:-1],random.choice(word4)[:-1]));

f.close();
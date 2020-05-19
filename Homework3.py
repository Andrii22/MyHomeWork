zen="""The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
print("Задание 1.1")
print(zen.find('better'))
print(zen.find('never'))
print(zen.find('is'))
print('----------------------')
print("Задание 1.2")
print(zen.upper())
print('----------------------')
print("Задание 1.3")
print(zen.replace('i','&'))
print('----------------------')
print("Задание 2.1")
n=int(input())
ch4=n%10
ch3=n%100//10
ch2=n%1000//100
ch1=n//1000
print(ch4)
print(ch3)
print(ch2)
print(ch1)
n2 = ch1 * ch2 * ch3 * ch4
print('Добуток числа:',n2)
print('----------------------')
print("Задание 2.2")
print('Вариант 1')
n2 = 0 
while n >0:
	digit = n % 10;
	n = n // 10;
	n2 = n2 * 10
	n2 = n2 + digit
print('Перевернутое число:',n2)
print('----------------------')
print('Вариант 2')
list=[ch1,ch2,ch3,ch4]
list.reverse()
print('Мое число сейчас:',list)
print('----------------------')
print("Задание 2.3")
list.sort()
print('Мое отсортированое число в порядке увеличения сейчас:',list)
list.sort(reverse = True)
print('Мое отсортированое число в порядке убывания сейчас:',list)
print('----------------------')
print("Задание 3.1")
zmin1 = input()
zmin2= input()
zmin1,zmin2 = zmin2,zmin1
print('Вот мои переменные,(zmin1 потом zmin2(но уже переставленны)):',zmin1,',',zmin2)
'''
#print(zmin2)
print('----------------------')
print('Вариант 2')
print("Введите значения переменных содержащие не мение 2-х символов в строке(это могут быть как числа ,так и слова ,так и буквы)")
zminna=input()
print(zminna.replace('три','два'))
'''

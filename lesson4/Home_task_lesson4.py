# Работа с переменными:
# 1. Переменной var_int присвойте значение 10, var_float - значение 8.4, var_str - "No"
#from Lesson_2.aqa_project1.Home_task_lesson3 import reversed_name, number

var_int = 10
var_float = 8.4
var_str = "No"
print(type(var_int))
print(type(var_float))
print(type(var_str))

# 2. Измените значение, хранимое в переменной var_int, увеличив его в 3.5 раза,результат свяжите с переменной big_int.

var_int = 10
big_int = (var_int*3.5)
print(big_int)
print(type(big_int))

# 3. Измените значение, хранимое в переменной var_float, уменьшив его на единицу,результат свяжите с той же переменной.

var_float = 8.4
var_float2 = (var_float-1)
print(var_float2)
print(type(var_float2))

# 4. Разделите var_int на var_float, а затем big_int на var_float. Результат данных выражений не привязывайте ни к каким переменным.

var_int = 10
var_float = 8.4
big_int = 35
print(var_int/var_float)
print(big_int/var_float)
print(type(var_int))
print(type(var_float))
print(type(big_int))

# 5. Измените значение переменной var_str на "NoNoYesYesYes". При формировании нового значения используйте операции конкатенации (+) и повторения строки (*).

var_str = "No"
repeated_var_str2 = var_str * 2
var_str1 = "Yes"
repeated_var_str3 = var_str1 * 3
finish_var = repeated_var_str2 + repeated_var_str3
print(finish_var)
print(type(finish_var))

# 6. Выведите значения всех переменных

print(big_int)
print(var_float2)
print(var_int/var_float)
print(big_int/var_float)
print(finish_var)


# Строки:
# 1. Свяжите переменную с любой строкой, состоящей не менее чем из 8 символов.Извлеките из строки первый символ, затем последний, третий с начала и третий с конца. Измерьте длину вашей строки.

sentence = "Hello my friend"
first = sentence[0]
last = sentence[14]
third_start = sentence[2]
third_end = sentence[12]
print(first, last, third_start, third_end)
print(type(sentence))
print(type(first))
print(type(last))
print(type(third_start))
print(type(third_end))
string = len(sentence)
print(string)
print(type(string))

# 2. Присвойте произвольную строку длиной 10-15 символов переменной и извлеките из нее следующие срезы:
#● первые восемь символов
# четыре символа из центра строки
#● символы с индексами кратными трем
#● переверните строку

name_sens = "Soft kitty warm kitty"
eight_char = name_sens[0:8]
print(eight_char)
print(type(eight_char))

name_sens = "Soft kitty warm kitty"
center_chars = name_sens[len(name_sens) // 2 - 2 : len(name_sens) // 2 + 2]
print(center_chars)
print(type(center_chars))

name_sens = "Soft kitty warm kitty"
count = len(name_sens)
print(count)
ind_three = name_sens[0:20:3]
print(ind_three)
print(type(ind_three))

name_sens = "Soft kitty warm kitty"
new_sens = name_sens.split()
reversed1 = " ".join(reversed(new_sens))
print(reversed1, type(reversed1))

# 3. Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name” вставьте ваше имя.

i = "my name is name"
new_i = i.replace("is name", "is ina")
print(new_i, type(new_i))

# 4. Есть строка: test_tring = "Hello world!", необходимо
#● напечатать на каком месте находится буква w
#● кол-во букв l
#● Проверить начинается ли строка с подстроки: “Hello”
#● Проверить заканчивается ли строка подстрокой: “qwe”

test_string = "Hello world!"
test_one = test_string.index("w")
print(test_one, type(test_one))

print(test_string.count("l"))
print(type(test_string))

print(test_string.startswith("Hello"))

print(test_string.endswith("qwe"))

# Списки:
# 1. Создайте два любых списка и свяжите их с переменными

number_list = [1, 2, 3, 4, 5, 6]
words_list = ["a", "b", "c", "d", "f", "g"]
print(type(number_list), type(words_list))

# 2. Извлеките из первого списка второй элемент.

print(number_list[1])

# 3. Измените во втором списке последний элемент. Выведите список на экран.

words_list[5] = "h"
print(words_list)

# 4. Соедините оба списка в один, присвоив результат новой переменной. Выведите получившийся список на экран.

general_list = (number_list+words_list)
print(general_list, type(general_list))

# 5. "Снимите" срез из соединенного списка так, чтобы туда попали некоторые части
# обоих первых списков. Срез свяжите с очередной новой переменной. Выведите
#значение этой переменной.

new_general_list = general_list[0:11:3]
print(new_general_list, type(new_general_list))

# 6. Добавьте в список два новых элемента и снова выведите его.

new_general_list.append(9)
new_general_list.append("w")
print(new_general_list)

# 7. Даны списки:
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].Нужно вернуть список, который состоит из элементов, общих для этих двух
#списков. -- !не использовать циклы

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
from collections import Counter
common_elements = list((Counter(a) & Counter(b)).elements())
print(common_elements, type(common_elements))

# 8. Есть список: [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3] оставить в нем только уникальные значения. !не использовать циклы

l = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
unique_number = set(l)
print(unique_number, type(unique_number))

# Логические операции:
# 1. Присвойте двум переменным любые числовые значения

c = 7
d = 32
print(c,d, type(c), type(d))

# 2. Составьте четыре сложных логических выражения с помощью оператора and, два из которых должны давать истину, а два других - ложь.

c_1 = c<10 and c>3
print(c_1, type(c_1))
d_1 = d>45 and d<25
print(d_1, type(d_1))

# 3. Аналогично выполните п. 2, но уже используя оператор or.

c_2 = c<9 or c>9
print(c_2, type(c_2))
d_2 = d>36 or d<25
print(d_2, type(d_2))

#4. Попробуйте использовать в сложных логических выражениях работу с переменными строкового типа.

#email = input("Enter email: ")

#if "@" in email and "." in email:
  #print("Correct email")
#else:
  #print("Wrong email")

 # Словари:
 # 1.Создайте словарь, связав его с переменной school, и наполните его данными,которые бы отражали количество учащихся
# в десяти разных классах(например, 1а, 1б,2б, 6а, 7в и т.д.).

school = {"1a":15, "1b":18, "1c":21, "2a":25, "2b":17, "2c":19, "3a":22, "3b":26, "4a":20, "4b":22}
print(school, type(school))

# 2. Узнайте сколько человек в каком-нибудь классе

print(school["2a"])

# 3. Представьте, что в школе произошли изменения, внесите их в словарь:
#◦ в трех классах изменилось количество учащихся;
#◦ в школе появилось два новых класса;
#◦ в школе расформировали один из классов.

school["1b"] = 20
school["1a"] = 17
school["1c"] = 10
school["5a"] = 13
school["5b"] = 17
del school["2a"]
school["2b"] += 12
school["2c"] += 13

# 4. Выведите содержимое словаря на экран.

print(school)

# Преобразование типов
# 1. Перевести строку в массив "Robin Singh" => ["Robin”, “Singh"]
# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]

name_str = "Robin Singh"
name_list = name_str.split()
print(name_list, type(name_list))
sentence_str = "I love arrays they are my favorite"
sentence_list = sentence_str.split()
print(sentence_list, type(sentence_list))

#2. Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
#Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”

con1 = ["Ivan", "Ivanou"]
city = "Minsk"
country = "Belarus"
new_con = " ".join(con1)
print(f"Привет, {new_con}! Добро пожаловать в {city} {country}")

# 3. Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него
#строку => "I love arrays they are my favorite"

my_love = ["I", "love", "arrays", "they", "are", "my", "favorite"]
new_my_love = " ".join(my_love)
print(new_my_love, type(new_my_love))

# 4. Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6

elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elements[2] = 11
del elements[6]
print(elements, type(elements))

# 5.Есть 2 словаря
#a = { 'a': 1, 'b': 2, 'c': 3}
#b = { 'c': 3, 'd': 4,'e': 5}
#Необходимо их объединить по ключам, а значения ключей поместить в список, если у
#одного словаря есть ключ "а", а у другого нету, то поставить значение None на
#соответствующую позицию(1-я позиция для 1-ого словаря, вторая для 2-ого)
#ab = {'a': [1, None], 'b': [2, None], 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}

a = { 'a': 1, 'b': 2, 'c': 3}
b = { 'c': 3, 'd': 4,'e': 5}
merged_dict = {}
for key in set(b.keys()) | set(a.keys()):
  merged_dict[key] = [a.get(key), b.get(key)]

print(merged_dict, type(merged_dict))

#*1) Вам передан массив чисел. Известно, что каждое число в этом массиве имеет пару,
#кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
#Напишите программу, которая будет выводить уникальное число

def find_unique_number (arr):
    count = {}
    for number in arr:
        if number in count:
            count [number] += 1
        else:
            count [number] = 1
    for number, cnt in count.items():
        if cnt == 1:
            return number

a = [1, 5, 2, 9, 2, 9, 1]
un = find_unique_number(a)
print(un)

#Условия
#1. Дано целое число. Если оно является положительным, то прибавить к нему 1; в
#противном случае не изменять его. Вывести полученное число.

n = 50
n_1 = n + 1
print(n_1, type(n_1))

#2. Даны три целых числа. Найти количество положительных чисел в исходном наборе.

def count_positive(num1, num2, num3):
 return sum(1 for num in [num1, num2, num3] if num > 0)
print(count_positive(-1, 2, 3))

#3. Дан номер года (положительное целое число). Определить количество дней в
#этом году, учитывая, что обычный год насчитывает 365 дней, а високосный — 366
#дней. Високосным считается год, делящийся на 4, за исключением тех годов, которые
#делятся на 100 и не делятся на 400 (например, годы 300, 1300 и 1900 не являются
#високосными, а 1200 и 2000 являются).

input = 1989
output = 0
if input % 4 != 0:
    output = 365
else:
    if input % 100 != 0:
        output = 366
    else:
        if input % 400 != 0:
            output = 365
        else:
            output = 366
print(f"Количество дней в {input} = {output}")

#4. Дано целое число в диапазоне 1–7. Вывести строку — название дня недели,
#соответствующее данному числу (1 — «понедельник», 2 — «втор- ник» и т. д.).

number_day = 3
day = 0
if number_day == 1:
    day = "понедельник"
elif number_day == 2:
    day = "вторник"
elif number_day == 3:
    day = "среда"
elif number_day == 4:
    day = "четверг"
elif number_day == 5:
    day = "пятница"
elif number_day == 6:
    day = "суббота"
elif number_day == 7:
    day = "воскресенье"
print(day)
print(type(day))

#5. Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 —
#миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер. Дан номер едини- цы массы (целое
#число в диапазоне 1–5) и масса тела в этих единицах (вещественное число). Найти
#массу тела в килограммах.

big = 4.15
item = 3 # от 1 до 5
total = 0
if item == 1:
    total = big * 1
elif item ==2:
    total = big * 0.0000001
elif item == 3:
    total = big * 0.0001
elif item == 4:
    total = big * 1000
elif item == 5:
    total = big * 100
print(total)
print(type(total))

#Цикл for
#1. Даны два целых числа A и B (A < B). Найти сумму всех целых чисел от A до B включительно.

A = 5
B = 9
count = 0
for i in range(A, B+1):
    count = count + i
print(count)
print(type(count))

#2. Найти сумму всех натуральных чисел в от A до B

count_1 = 0
for i in range (2, 15):
    count_1 = count_1 + i
print(count_1)
print(type(count_1))

#3. Найти произведение положительных, сумму и количество отрицательных из 10 введенных целых значений.

m = 1
s = 0
c = 0
numbers = [-2, 5, 9, -5, 8, 2, 3, -9, 1, -1]
for x in numbers:
    if x >= 0:
        m = m * x
    elif x < 0:
        s = s + x
        c = c + 1
print(m, s, c)

#4. Дан словарь пловцов с их результатами. Напечатать лучший результат заплыва среди 6 участников.
#Бекиш Александр - 21,07
#Будник Алексей - 20,34
#Гребень Анастасия - 22,12
#Давидович Татьяна - 30
#Дешук Дмитрий - 24.01
#Казак Анна - 28,17

swim = {"Бекиш Александр": 21.07, "Будник Алексей": 20.34, "Гребень Анастасия": 22.12, "Давидович Татьяна": 30,
        "Дедук Дмитрий": 24.01, "Казак Анна": 28.17}

fastest = list(swim.values())[0]
for x in swim:
    if swim[x] < fastest:
        fastest = swim[x]
print(fastest)

#Цикл while
#1. Дано число N. Найти произведение всех чисел от 0 до N.

N = 4
m_1 = 1
while N > 0:
    m_1 = m_1 * N
    N = N - 1
print(m_1)
print(type(m_1))

#2. Поле засеяли цветами двух сортов на площади S1 и S2. Каждый год
#площадь цветов первого сорта увеличивается вдвое, а площадь второго сорта
#увеличивается втрое. Через сколько лет площадь первых сортов будет
#составлять меньше 10% от площади вторых сортов.

s1 = 500
s2 = 100
year_count = 0
while s1 >= s2 * 0.1:
    s1 = s1 * 2
    s2 = s2 * 3
    year_count = year_count + 1
print(year_count)

#3. Дано целое число N (>0). Используя операции деления нацело и взятия
#остатка от деления, найти количество и сумму его цифр.

Na = 123
summ = 0
count = 0
while Na > 0:
    residue = Na % 10
    summ = summ + residue
    count = count + 1
    Na = Na // 10
print(summ, count)

#4. Деду M лет, а внуку N лет. Через сколько лет дед станет вдвое старше
#внука. И сколько при этом лет будет деду и внуку

d = 63
v = 30
year = 0
while d > v * 2:
   year = year + 1
   d = d + 1
   v = v + 1
print(year, d, v)

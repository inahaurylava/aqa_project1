# 1. Привести к целому типу -1.6, 2.99
from enum import unique

number = int (-1.6)
print(number)
number_2 = int (2.99)
print(number_2)

# 2. Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
web = 'www.my_site.com#about'
new_web = web.replace("#","/")
print(new_web)

# 3. Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’
word = 'stroka'
new_word = 'ing'
print(word + new_word)

# 4. В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
name = "Ivanou Ivan"
words = name.split()
reversed_name = " ".join(reversed(words))
print(reversed_name)

# 5. Напишите программу которая удаляет пробел в начале, в конце строки
stroka = "   Hello, Minsk      "
new_stroka = stroka.strip()
print(stroka)
print(new_stroka)

# 6. Создайте словарь, связав его с переменной school, и наполните его данными которые бы отражали количество учащихся в десяти разных классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).
school = {"1a":15, "1b":18, "1c":21, "2a":25, "2b":17, "2c":19, "3a":22, "3b":26, "4a":20, "4b":22}
print(school)

# 7. Создайте список и извлеките из него списка второй элемент
array = [ 3, 4, 7, 9, 6 ]
print(array[1])

# 8. Вывести входит ли строка1 в строку2 (пример: employ и employment )
test_1 = "employ"
test_2 = "enploy"
test_3 = "employment"
print(test_1 in test_3)
print(test_2 in test_3)

# 9. Вывести нужные символы x = "My name is Agent Smith" print(x[?]) #y print(x[?:?:?]) #nesgt
x = "My name is Agent Smith"
print(x[1])
print(x[3:17:3])

# 10*. Есть массив чисел. Известно, что каждое число в этом массиве имеет пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
# Напишите программу, которая будет выводить уникальное число
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

# 2. Измените значение, хранимое в переменной var_int, увеличив его в 3.5 раза,результат свяжите с переменной big_int.

def multiplication():
    var_int = 10
    big_int = (var_int*3.5)
    return big_int

print(multiplication())

 # 1.Создайте словарь, связав его с переменной school, и наполните его данными,которые бы отражали количество учащихся
# в десяти разных классах(например, 1а, 1б,2б, 6а, 7в и т.д.).

def classes():
    school = {"1a":15, "1b":18, "1c":21, "2a":25, "2b":17, "2c":19, "3a":22, "3b":26, "4a":20, "4b":22}
    return school

print(classes())

#2. Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
#Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”

def hi(city, country):
    con1 = ["Ivan", "Ivanou"]
    new_con = " ".join(con1)
    return f"Привет, {new_con}! Добро пожаловать в {city} {country}"

result = hi("Minsk", "Belarus")
print(result)


#3. Дан номер года (положительное целое число). Определить количество дней в
#этом году, учитывая, что обычный год насчитывает 365 дней, а високосный — 366
#дней. Високосным считается год, делящийся на 4, за исключением тех годов, которые
#делятся на 100 и не делятся на 400 (например, годы 300, 1300 и 1900 не являются
#високосными, а 1200 и 2000 являются).

def year(date):
    output = 0
    if date % 4 != 0:
        output = 365
    else:
        if date % 100 != 0:
            output = 366
        else:
            if date % 400 != 0:
                output = 365
            else:
                output = 366

    return f"Количество дней в {date} = {output}"

result = year(1859)
print(result)

# 3. Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’

def new_word1(words):
    ending = 'ing'
    return words + ending

result = new_word1("runn")
print(result)

# 5. Напишите программу которая удаляет пробел в начале, в конце строки

def sentence(stroka):
    new_stroka = stroka.strip()
    return new_stroka

result = sentence("           hi,world        ")
print(result)


import pickle

#1 Дан файл целых чисел, содержащий не менее четырех элементов.
#Вывести первый, второй, предпоследний и последний элементы данного
#файла. Если чисел меньше 3 выводить ошибку


with open('task_6.txt', 'w') as file:
    numbers = list(range(1, 8))
    for num in numbers:
        file.write(str(num) + ' ')

content = ''
with open("task_6.txt", "r") as file:
    content = file.read()

content=content.strip()
digits_array = content.split(' ')
if len(digits_array) < 3:
    print(f"Error.Чисел меньше 3")
print(digits_array[0])
print(digits_array[1])
print(digits_array[len(digits_array) - 1])
print(digits_array[len(digits_array) - 2])

#2 Дан файл целых чисел. Создать два новых файла, первый из которых
#содержит четные числа из исходного файла, а второй — нечетные (в том
#же порядке). Если четные или нечетные числа в исходном файле
#отсутствуют, то соответствующий результирующий файл оставить пустым

with open('task_6_chot.txt', 'w') as file:
    file.write('')
with open('task_6_nechot.txt', 'w') as file:
    file.write('')

with open("task_6.txt", "r") as file:
    for line in file:
        digits_array1 = line.split(' ')
        for item in digits_array1:
            if item != " " and item != "":
                value = int(item)
                if value % 2 == 0:
                    with open('task_6_chot.txt', 'a') as file:
                        file.write(item + " ")
                else:
                    with open('task_6_nechot.txt', 'a') as file:
                        file.write(item + " ")

#3 Дан файл вещественных чисел. Заменить в нем все элементы на их квадраты.

with open('task_6_float.txt', 'w') as file:
    numbers = [1.5, 2.3, 8.1]
    for num in numbers:
        file.write(str(num) + ' ')

result_arr = []
with open('task_6_float.txt', 'r') as file:
    for line in file:
        digits_array1 = line.split(' ')
        for item in digits_array1:
            if item != " " and item != "":
                value = float(item)
                new_value = value * value
                result_arr.append(str(new_value))

with open('task_6_float.txt', 'w') as file:
    file.write(" ".join(result_arr))

#4 Даны два файла произвольного типа. Поменять местами их содержимое. Файлы должны быть бинарного типа

content_file1 = "Content from file 1"
content_file2 = "Content from file 2"

#создали
with open('task_6_bin1.dat', 'wb') as file:
    pickle.dump(content_file1, file)

with open('task_6_bin2.dat', 'wb') as file:
    pickle.dump(content_file2, file)

#прочитали
with open('task_6_bin1.dat', 'rb') as file:
    content_file2 = pickle.load(file)

with open('task_6_bin2.dat', 'rb') as file:
    content_file1 = pickle.load(file)

#записали
with open('task_6_bin1.dat', 'wb') as file:
    pickle.dump(content_file1, file)

with open('task_6_bin2.dat', 'wb') as file:
    pickle.dump(content_file2, file)

# проверили, напечатали результат
with open('task_6_bin1.dat', 'rb') as file:
    cont = pickle.load(file)
    print(cont)

with open('task_6_bin2.dat', 'rb') as file:
    cont = pickle.load(file)
    print(cont)

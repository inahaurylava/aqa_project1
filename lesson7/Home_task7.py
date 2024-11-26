#1. Создать lambda функцию, которая принимает на вход имя и выводит его в формате "Hello, {name}"

sentence = lambda name: f"Hello, {name}"
print(sentence("World"))

#2. Создать lambda функцию , которая принимает на вход список имён и выводит их в формате "Hello, {name}"
#в другой список.

list_name = lambda input_name: ["Hello," + str(item) for item in input_name]

my_list = ["Sasha", "Masha", "Pasha"]
new_list = list_name(my_list)
print(new_list)

#3. Напишите генератор который принимает список numbers =[34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
#и возвращает новый список только с положительными числами

def positive_numbers():
    numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
    for x in numbers:
        if x > 0:
            yield x

mygenerator = positive_numbers()
print(mygenerator)
for x in mygenerator:
    print(x)


#4. Необходимо составить список чисел которые указывают на длину слов в строке:
# sentence = "thequick brown fox jumps over the lazy dog" но только если слово не "the" с обработкой исключений.

def words_lengths(input_str):
    result = []
    for x in input_str.split(" "):
        try:
            if x == "the":
                raise Exception("the")
            result.append(len(x))
        except Exception as error:
            print(error)
    return result

print(words_lengths("thequick brown fox jumps over the lazy dog"))



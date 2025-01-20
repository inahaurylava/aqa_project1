# Написать обычную функцию для факториала, генератор и рекурсию. Сравнить их время работы.
import time


def factorial_recursive(x):
    if x == 0:
        return 1
    else:
        return x * factorial_recursive(x-1)

print(factorial_recursive(15))

def factorial_generator(x):
    if x == 0:
        yield 1
    else:
        result = 1
        for i in range(1, x + 1):
            result *= i
            yield result

for i in factorial_generator(15):
    print(i)

def call_generator(fact_len):
    result = list(factorial_generator(fact_len))

    return result[-1]

def timeit(func, *args):
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    return end - start, result

x = 15

time_generator, result_generator = timeit(call_generator, x)
time_recursive, result_recursive = timeit(factorial_recursive, x)

print(f"Генератор:{time_generator:.6f} сек., результат: {result_generator}")
print(f"Рекурсия: {time_recursive:.6f} сек., результат: {result_recursive}")


# Напишите декоратор , который проверял бы тип параметров функции , конвертировал их если надо и складывал.

def typed(type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            new_args = []
            try:
                if type == "str":
                    check_type = str
                elif type == "int":
                    check_type = int
                elif type == "float":
                    check_type = float
                else:
                    raise ValueError("Неподдерживаемый тип")

                for arg in args:
                    new_args.append(check_type(arg))


                return func(*new_args, **kwargs)
            except ValueError as e:
                return f"Ошибка преобразования типа: {e}"
        return wrapper
    return decorator

@typed(type="str")
def add_two_simbols(a, b):
    return a + b

print(add_two_simbols("3", 5))
print(add_two_simbols(5, 5))
print(add_two_simbols("a", "b"))

@typed(type="float")
def add_tree_symbols(a, b, c):
    return a + b + c

print(add_tree_symbols(5, 6, 7))
print(add_tree_symbols("3", 5, 0))
print(add_tree_symbols(0.1, 0.2, 0.4))


# На вход подаётся некоторое количество (не больше сотни) разделённых пробелом целых чисел (каждое не меньше 0 и не больше 19)
# Выведите их через пробел в порядке лексиграфического возрастания названий этих чисел в английском языке. Т.е. скажем
# числа 1,2,3 должны быть выведены в порядке 1,3,2 поскольку слово two в словаре встречается позже слова three , а слово three
# - позже слова one (иначе говоря, поскольку выражение "one"<"three"<"two"является истинным)


def sort_numbers_lexicographically(input_string):

    numbers_name = {
    0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten"
    }
    try:
        numbers = [int(x) for x in input_string.split()]
        if not all(0 <= num <= 10 for num in numbers):
            return "Error: Numbers must be between 0 and 10"
        if len(numbers) > 100:
            return "Error: Too many numbers"

        sorted_numbers = sorted(numbers, key=lambda x: numbers_name[x])
        return " ".join(map(str, sorted_numbers))

    except ValueError:
        return "Error: Invalid input.  Please enter integers separated by spaces."

input_str = "1 2 3 4 5 6 7 8 9"
result = sort_numbers_lexicographically(input_str)
print(result)









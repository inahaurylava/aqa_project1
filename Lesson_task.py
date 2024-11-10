# Алёна,Валерия,Лиана,Инна
# Привести к целому типу - 3.7, 4.2
a = -3.7
b = 4.2
print(int(a))
print(int(b))

# Заменить символ “@” на символ “&” в строке 'user@domain.com'
mail = 'user@domain.com'
new_mail = mail.replace("@","&")
print(new_mail)

# Напишите программу, которая добавляет ‘ly’ к слову 'text'
word = 'text'
new_word = 'ly'
print(word + new_word)

# В строке “Doe John” поменяйте местами слова, чтобы получилось “John Doe”
name = "Doe John"
name2 =  name.split(None,2)
print(name2[1]+ name[0])

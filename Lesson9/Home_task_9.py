# Придумать класс и метод к нему.

class Medicine:

    method_of_administration_default = "inside"
    medicine_count = 0

    def __init__(self, name, dosage, form, method_of_administration=None):
        self.name = name
        self.dosage = dosage
        self.form = form
        self.method_of_administration = Medicine.method_of_administration_default if method_of_administration == None else method_of_administration
        Medicine.medicine_count += 1

print(Medicine.medicine_count)
tablet = Medicine("Enalapril", "10", "tablet", "Outside")
print(tablet.name, tablet.dosage, tablet.form, tablet.method_of_administration)
print(Medicine.medicine_count)
pulveris = Medicine("Nimesil", "100", "pulver")
print(pulveris.name, pulveris.dosage, pulveris.form, pulveris.method_of_administration)
print(Medicine.medicine_count)
sirups = Medicine("Lazolvan", "30 mg/ml", "sirup")
print(sirups.name, sirups.dosage, sirups.form, sirups.method_of_administration)
print(Medicine.medicine_count)

# Использовать инкапсуляцию

class Plants:
    tax_amount = 0.15

    def __init__(self, name, color, price = 0):
        self.name = name
        self.color = color
        self.__price = price

    def set_price(self, user_p):
        if user_p > 0:
            self.__price = user_p + user_p * Plants.tax_amount
            print(f"Цена {user_p}, новая цена {self.__price} ")
        else:
            print("Цена должна быть положительной")

    def get_price(self):
        return self.__price

type_1 = Plants("orhid", "white")
type_1.set_price(100)
print(f"Ваша стоимость {type_1.get_price()}")


# Использовать полиморфизм

class Phone:
    def start(self):
        raise NotImplementedError("Error")

class Mobile(Phone):
    def start(self):
        return "Hi, Samsung"

class HomePhone(Phone):
    def start(self):
        return "Sound"

def start_phone(phone):
    print(phone.start())

samsung = Mobile()
philips = HomePhone()

start_phone(samsung)
start_phone(philips)

# Использовать наследование

class Coffee:
    condition = "seed"

    def __init__(self, name, roasting, condition=None):
        self.name = name
        self.roasting = roasting
        if condition is None:
            self.condition = Coffee.condition
        else:
            self.condition = condition

type_1 = Coffee("arabica", "medium")
print(type_1.name, type_1.roasting, type_1.condition)
type_2 = Coffee("robusta", "high", "ground")
print(type_2.name, type_2.roasting, type_2.condition)

class Cacao(Coffee):

    def __init__(self, name, roasting, condition, taste ):
        super().__init__(name, roasting, condition)
        self.taste = taste


cacao_1 = Cacao("Nesquik", "light", "ground", "vanilla")
print(cacao_1.name, cacao_1.roasting, cacao_1.condition, cacao_1.taste)





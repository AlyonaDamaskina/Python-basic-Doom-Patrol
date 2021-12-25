
# 1.
import dataclasses
from collections import namedtuple


class Laptop:
   def __init__(self):
       battery = Battery('It shows the level of charge')
       self.battery = battery


class Battery:
   def __init__(self, energy):
    self.energy = energy


laptop = Laptop()
print(laptop.battery.energy)



# 2
class Guitar:
   def __init__(self, strings):
       self.strings = strings

class GuitarString:
   def __init__(self):
      pass

string = GuitarString()
guitar = Guitar(string)

# 3
class Calc:
    pass
    @staticmethod
    def add_nums(a, b, c):
        return (a + b + c)

sum = Calc()
print(sum.add_nums(28, 975, -3))


# 4
class Pasta:
   def __init__(self, ingredients):
      self.ingredients = ingredients

   @classmethod

   def carbonara(cls):
       return cls(['forcemeat', 'tomatoes'])

   @classmethod

   def bolognaise(cls):
       return cls(['bacon', 'parmesan', 'eggs'])

Pasta_carb = Pasta.carbonara()
Pasta_bol = Pasta.bolognaise()
print(Pasta_carb)
print(Pasta_bol)


# 5
class Concert:
    def __init__(self, max_visitors_num):
        self.max_visitors_num = max_visitors_num

    def visitors_check(self, visitors_count):
        self.visitors_count = visitors_count
        if self.visitors_count > concert_arena.max_visitors_num:
            self.visitors_count = concert_arena.max_visitors_num


concert_arena = Concert(5000)
concert_arena .visitors_check(400)

print(concert_arena.visitors_count)
print(concert_arena.max_visitors_num)

# 6
@dataclasses.dataclass

class AddressBookDataClass:
   key: int
   name: str
   phone_number: str
   address: str
   email: str
   birthday: str
   age: int

address_book = AddressBookDataClass(key=13,
                                   name='OLENKA',
                                   phone_number='0675944975',
                                   address='Street No Name 2',
                                   email='gorgona.7707@gmail.com',
                                   birthday='30.07.1995',
                                   age=26)
print(address_book)

# 7
AddressTuple = namedtuple('AddressBookDataClass',
                         ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])


address_book_tuple = AddressTuple(28, 'Olenka', '0675944975', 'Red Sun', 'gorgona1@gmail.com', '30.07.1995', 26)
print(address_book_tuple)

# 8
class AddressBook:
   def __init__(self, key, name, phone_number, address, email, birthday, age):
       self.key = key
       self.name = name
       self.phone_number = phone_number
       self.address = address
       self.email = email
       self.birthday = birthday
       self.age = age
   def __str__(self):
       return (f'AddressBook(key={self.key}, name={self.name}, '
               f'phone_number={self.phone_number}, address={self.address},'
               f'email={self.email}, birthday={self.birthday}, '
               f'age={self.age})')

address_book_1 = AddressBook(key=12,
                            name='Askold',
                            phone_number='034768532',
                            address='Stryiska Street',
                            email='red.sun71@gmail.com',
                            birthday='12.06.77',
                            age=44)
print(address_book_1)


# 9
class Person:
   def __init__(self, name, age, country):
       self.name = name
       self.age = age
       self.county = country
   @property

   def print_age(self):
       return f'It is {self.name}, and he is {self.age} years old'

person = Person('John', 36, 'USA')
print(person.print_age)
person.age = 39
print(person.print_age)




# 10
class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

Myroslav = Student(27, 'Myroslav')
setattr(Myroslav, 'personal_email', 'myroslav12345@gmail.com')
print(getattr(Myroslav, 'personal_email'))



#11
class Celsius:
    def __init__(self, temperature):
        self.temperature = temperature

    @property
    def fahrenheit(self):
        print(self.temperature * 1.8 + 32)


t_cel = Celsius(27)
t_cel.fahrenheit
















































































# 11


class Celsius:


   def __init__(self, temperature=0):


       self._temperature = temperature







   @property


   def print_temperature(self):


       return self._temperature







   @print_temperature.setter


   def temperature(self, new_t):


       self._temperature = new_t












f_temperature = Celsius(10)


f_temperature.temperature = f_temperature.temperature * 1.8 + 32


print(f_temperature.temperature)



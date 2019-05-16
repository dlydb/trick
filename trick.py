# tip 1   one_sentence

condition = True
x = 1 if condition else 0



# tip 2   many digits

num1 = 100_000_000
num2 = 100_000

total = num1 + num2

# print(f'{total:,}')
# will print 100,100,000



# tip 3    enumerater
names = ['abc', 'jhds', 'duhe', 'fsdl']
for index, name in enumerater(names, start = 1): # start at position 1
    # print(index, name)



# tip 4    loop two list
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson']
heros = ['Spiderman', 'Superman', 'Deadpool']
universes = ['Marvel', 'DC', 'Marvel']

for name, hero, universe in zip(names, heros, universes):
    # print(f'{name} is actually {hero} from {universe}')

for value in zip(names, heros, universes):
    # print(value)



# tip 5    unpacking
a, b = (1, 2)
a, _ = (1, 2)
a, b, *c = (1, 2, 3, 4, 5)
# a = 1, b = 2, c = [3, 4, 5]
a, b, *c, d = (1, 2, 3, 4, 5)
# a = 1, b = 2, c = [3, 4], d = 5



# tip 6    set attr
class Person():
    pass

person = Person()

first_key = 'first'
first_val = 'Corey'

setattr(person, first_key, first_val)

# print(person.first)

first = getattr(person, first_key)
# print(first)

# implementation

person_info = {'first': 'Corey', 'last': 'Schafer'}

for key, value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    # print(getattr(person, key))


# tip 7   secret information
from getpass import getpass

username = input('Username: ')
password = getpass('Password: ')

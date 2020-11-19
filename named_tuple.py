from collections import namedtuple

Car = namedtuple('Авто', ['цвет', 'пробег'])
# Car = namedtuple('Авто', 'цвет пробег')  # Можно писать и так, внутри произойдет split

my_car = Car('красный', 3812.4)
print(my_car.цвет)  # Можем читать данные по имени
print(my_car[1])    # или по индексу, как в обычном tuple

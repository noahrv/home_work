# задача №1
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        """расчет площади прямоугольника"""
        return self.width * self.height

    def calculate_perimeter(self):
        """расчет периметра прямоугольника"""
        return 2 * (self.width + self.height)

rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)
rect3 = Rectangle(8, 4)

print(f'прямоугольник 1 (ширина={rect1.width}, высота={rect1.height}):')
print(f'площадь: {rect1.calculate_area()}')
print(f'периметр: {rect1.calculate_perimeter()}\n')

print(f'прямоугольник 2 (ширина={rect2.width}, высота={rect2.height}):')
print(f'площадь: {rect2.calculate_area()}')
print(f'периметр: {rect2.calculate_perimeter()}\n')

print(f'прямоугольник 3 (ширина={rect3.width}, высота={rect3.height}):')
print(f'площадь: {rect3.calculate_area()}')
print(f'периметр: {rect3.calculate_perimeter()}')


# задача №2
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b

math_operations = Math(10, 20)

print('сложение: ', math_operations.addition())
print('умножение: ', math_operations.multiplication())
print('деление: ', math_operations.division())
print('вычитание: ', math_operations.subtraction())

# или:
# addition_object = Math(10,20)
# multiplication_object = Math(10,20)
# division_object = Math(10,20)
# subtraction_object = Math(10,20)

# print('сложение: ', addition_object.addition())
# print('умножение: ', multiplication_object.multiplication())
# print('деление: ', division_object.division())
# print('вычитание: ', subtraction_object.subtraction())


# задача №3
class Button:
    def __init__(self, text):
        self.text = text
        self.type = 'Кнопка'
        self.locator = ''

    def click(self):
        return f'Клик по кнопке {self.text}'

text_box = Button('Text Box')
check_box = Button('Check Box')
radio_button = Button('Radio Button')
web_tables = Button('Web Tables')
buttons = Button('Buttons')
links = Button('Links')
broken_links = Button('Broken Links - Images')
upload_download = Button('Upload and Download')
dynamic_properties = Button('Dynamic Properties')

buttons_list = [text_box, check_box, radio_button, web_tables, buttons, links, broken_links, upload_download, dynamic_properties]

for button in buttons_list:
    print(f'Текст кнопки: {button.text}')
    print(f'Тип: {button.type}')
    print(f'Локатор: {button.locator}')
    print(button.click())

# --------------------------------------------------------------------------------------------------------------------------------

# доп задача с двумя файлами:

# в файлике car.py:
class Car:
    def __init__(self, color: str = None, type: str = None, year: int = None):
        self.color = color
        self.type = type
        self.year = year
        self.engine_on = False

    def start_engine(self):
        if not self.engine_on:
            self.engine_on = True
            return 'автомобиль заведён'
        return 'ошибка'

    def stop_engine(self):
        if self.engine_on:
            self.engine_on = False
            return 'автомобиль заглушен'
        return 'ошибка'

    def set_year(self, year: int) -> None:
        self.year = year
        print(f'год выпуска установлен: {year}')

    def set_type(self, type: str) -> None:
        self.type = type
        print(f'тип автомобиля установлен: {type}')

    def set_color(self, color: str) -> None:
        self.color = color
        print(f'цвет автомобиля установлен: {color}')

    def __str__(self) -> str:
        return f'автомобиль: {self.color} {self.type} {self.year} года'

# в файлике 4_hw.py:
from car import Car

car_1 = Car(color='красный', type='седан', year=2020)

print(car_1)
print(car_1.start_engine())

car_2 = Car(color='чёрный', type='внедорожник', year=2024)

print(car_2)
print(car_2.stop_engine())

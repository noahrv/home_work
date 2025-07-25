# задача №2
def print_max_number (a, b):
    if a > b:
        print(a)
    elif b > a:
        print(b)

print_max_number(5, 33)


# задача №3
def check_difference (a, b):
    if (a - b == 135) or (b - a == 135):
        print('yes')
    else:
        print('no')

check_difference (100, 235)


# задача №4
def seasons_of_the_year (month):
    if month in [12, 1, 2]:
        print('зима')
    elif month in [3, 4, 5]:
        print('весна')
    elif month in [6, 7, 8]:
        print('лето')
    elif month in [9, 10, 11]:
        print('осень')
    else:
        print('неверный номер месяца')

seasons_of_the_year (10)


# задача №5
def check_ten  (a, b, c):
    if a > 10 and b > 10 and c > 10:
        print('yes')
    else:
        print('no')

check_ten(11, 12, 9)


# задача №6
def positive_numbers(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count = count + 1
    print(count)

positive_numbers([-1, 2, 3, -4, -5])


# задача №7
def days(years:int, months:int):
    total_days = years * 12 * 29 + months * 29
    print('общее количество дней: ' + str(total_days))

days(2, 3)


# ответы при выбранных значениях:
# 33
# yes
# осень
# no
# 2
# общее количество дней: 783

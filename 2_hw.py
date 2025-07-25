# задача №1:
def task_1() -> None:

    a: int = 1
    print(a, 'относится к типу ', type(a))

    b: float = 0.1
    print(b, 'относится к типу ', type(b))

    c: str = 'привет, python'
    print(c, 'относится к типу ', type(c))

    d: list = [10, 20, 30]
    print(d, 'относится к типу ', type(d))

    e: bool = False
    print(e, 'относится к типу ', type(e))

task_1()


# задача №2:
def task_2() -> None:
    a = [1, 2, 3, 5, 8, 13, 21] # эта последовательность чисел называется "числа Фибоначчи"
    print("первые 3 значения списка:", a[:3])

task_2()


# задача № 3:
def task_3(number: int) -> int:
    """возвращает квадрат переданного числа."""
    return number ** 2

print(task_3(5))

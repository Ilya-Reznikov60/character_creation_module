from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculate_square_root(Number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number: float) -> None:
    """Производит вычисление."""
    if your_number <= 0:
        return
    calc_result = calculate_square_root(your_number)
    print('Мы вычислили квадратный корень из введённого вами числа.'
          f'Это будет: {calc_result}')


print(message)
calc(25.5)

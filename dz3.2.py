import re


def generator_numbers(text: str):
    matches = re.finditer(r'\b\d+(?:\.\d+)?\b', text) # Шукаємо всі дійсні числа в тексті
    for word in matches:
        yield float(word.group()) # Повертаємо кожне число по одному як float


def sum_profit(text: str, func):
    generator = func(text) # Отримуємо генератор через передану функцію та рахуємо суму
    return sum (generator)

text = "Загальний дохід працівника складається з декількох частин: 1350 як основний дохід, доповнений додатковими надходженнями 2700.50 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

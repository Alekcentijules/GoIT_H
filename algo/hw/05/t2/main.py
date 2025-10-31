from typing import Callable, Generator
import re

def generator_numbers(text: str) -> Generator[float, None, None]:
    pattern = r"\d+\.\d+"
    for num in re.findall(pattern, text):
        yield float(num)

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими " \
       "надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")

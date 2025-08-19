from pathlib import Path

def total_salary(path):
    try:
        salaries = []
        with open(Path(path), "r", encoding="utf-8") as file:
            lines = [el.strip() for el in file.readlines()]
            salaries = [int(line.split(",")[1]) for line in lines]
        average_sum = sum(salaries) / len(salaries)
    except FileNotFoundError:
        return f"File {path} not found!"
    except (ValueError, IndexError):
        return "File format is incorrect!"
    return (sum(salaries), average_sum)


filename = input("Enter a filename: ")
salaries = total_salary(filename)

print(salaries)
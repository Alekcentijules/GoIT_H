from pathlib import Path

def total_salary(path):
    try:
        salaries = []
        if not salaries:
                return "File {path} is empty!"
        with open(Path(path), "r", encoding="utf-8") as file:
            for line in file:
                name, salary = line.strip().split(",")
                salaries.append(int(salary)) 
        average_sum = sum(salaries) / len(salaries)
    except FileNotFoundError:
        return f"File {path} not found!"
    except (ValueError, IndexError):
        return "File format is incorrect!"
    return (sum(salaries), average_sum)

filename = input("Enter a path to file: ")
salaries = total_salary(filename)

print(salaries)
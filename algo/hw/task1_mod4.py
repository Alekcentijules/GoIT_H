from pathlib import Path

def search_path(filename):
    relative_path = Path(filename)
    absolute_path = relative_path.absolute()
    return absolute_path

def total_salary(path):
    salaries = []
    with open(path, "r") as file:
        lines = [el.strip() for el in file.readlines()]
        print(lines)
        for line in lines:
            num = ""
            for el in line:
                if el in "0123456789":
                    num = num + el
            salaries.append(num)
    return salaries


filename = input("Enter a filename: ")
absolute_path = search_path(filename)
salaries = total_salary(absolute_path)

print(f"It's absolute path: {absolute_path}")
print(salaries)
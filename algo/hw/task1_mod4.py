from pathlib import Path

def total_salary(path):
    try:
        relative_path = Path(path)
        absolute_path = relative_path.absolute()
        salaries = []
        total_sum = 0
        quality = 0
        with open(absolute_path, "r", encoding="utf-8") as file:
            lines = [el.strip() for el in file.readlines()]
            print(lines)
            for line in lines:
                num = ""
                for el in line:
                    if el in "0123456789":
                        num = num + el
                salaries.append(num)
        for el in salaries:
            total_sum += int(el)
            quality = quality + 1
        average_sum = total_sum / quality
        result = (total_sum, average_sum)
    except FileNotFoundError:
        return f"File {path} not found!"
    return result


filename = input("Enter a filename: ")
salaries = total_salary(filename)

print(salaries)
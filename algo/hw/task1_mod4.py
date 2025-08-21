from pathlib import Path

# def total_salary(path):
#     try:
#         salaries = []
#         if not salaries:
#                 return "File {path} is empty!"
#         with open(Path(path), "r", encoding="utf-8") as file:
#             for line in file:
#                 name, salary = line.strip().split(",")
#                 salaries.append(int(salary))
#         average_sum = sum(salaries) / len(salaries)
#     except FileNotFoundError:
#         return f"File {path} not found!"
#     except (ValueError, IndexError):
#         return "File format is incorrect!"
#     return (sum(salaries), average_sum)

# filename = input("Enter a filename: ")
# salaries = total_salary(filename)

# print(salaries)

#  C:\Users\ohala\VSCodeProjects\GoIT_H\algo\hw\cats_file.txt

def get_cats_info(path):
    cats = []
    print(f"Path received: '{path}'")
    with open(Path(path), "r") as file:
        for line in file:
            print(line)
            id, name, age = line.strip().split(",")
            cat = {"id":id, "name":name, "age":age}
            cats.append(cat)
    if not cats:
            return f"File {path} is empty!"
    return cats

cats_file = input("Enter a cats file: ")
cats_info = get_cats_info(cats_file)
print(cats_info)
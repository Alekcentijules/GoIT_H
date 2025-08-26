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
    try:
        cats = []
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    id, name, age = parts
                    cats.append({"id":id, "name":name, "age":age})
    except FileNotFoundError:
         return []
    return cats

cats_file = input("Enter a cats file: ")
cats_info = get_cats_info(cats_file) 
print(cats_info)
from pathlib import Path
from colorama import init, Fore, Style
import sys

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

# def get_cats_info(path):
#     try:
#         cats = []
#         with open(path, "r", encoding="utf-8") as file:
#             for line in file:
#                 parts = line.strip().split(",")
#                 if len(parts) == 3:
#                     id, name, age = parts
#                     cats.append({"id":id, "name":name, "age":age})
#     except FileNotFoundError:
#          return []
#     return cats

# cats_file = input("Enter a cats file: ")
# cats_info = get_cats_info(cats_file) 

# print(cats_info)


init(autoreset=True)

def show_directory(path, indent=0):
    try:
        directory = Path(path).resolve()

        if not directory.exists():
            print(f"{Fore.RED} Error: Path {directory} not exist!")
            return
        if not directory.is_dir():
            print(f"{Fore.RED} Error: {directory} is not a directory!")
            return
        
        for item in directory.iterdir():
            indent_str = " " * indent

            if item.is_dir():
                print(f"{indent_str}{Fore.BLUE}📂 {item.name}{Style.RESET_ALL}")
                show_directory(item, indent + 1)
            else:
                print(f"{indent_str}{Fore.GREEN}📜 {item.name}{Style.RESET_ALL}")
        
    except PermissionError:
        print(f"{Fore.RED} Error: not access to {path}")
    except Exception as e:
        print(f"{Fore.RED} There was an error: {str(e)}")

def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED} Error: Specify the path to the directory!")
        sys.exit(1)

    path = sys.argv[1]
    print(f"Directory structure: {path}")
    show_directory(path)

if __name__ == "__main__":
    main()
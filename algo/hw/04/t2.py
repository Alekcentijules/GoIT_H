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

cats_file = input("Enter a path to cats file: ")
cats_info = get_cats_info(cats_file) 

print(cats_info)
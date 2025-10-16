def get_cats_info(path): #def get_cats_info(path):
    cats = [] #cats = []
    try: #try:
        with open(path, 'r', encoding='utf-8') as file: #with open(path, 'r', encoding='utf-8') as file:
            for line in file: #for line in file:
                line = line.strip() #line = line.strip()
                if not line: #if not line:
                    continue
                try: 
                    cat_id, name, age = line.split(',') #cat_id, name, age = line.split(',')
                    cats.append({
                        "id": cat_id,
                        "name": name,
                        "age": age 
                    })
                except ValueError:
                    print(f"Неправильний формат рядка: {line}")
        return cats
    except FileExistsError:
        print(f"Файл не знайдено: {path}")
        return []
    except Exception as e: 
        print(f"Помилка при читанні файлу: {e}") 
        return []

if __name__ == "__main__":
    cats_info = get_cats_info("cats_file.txt")
    print(cats_info)
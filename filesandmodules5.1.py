def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0
            for line in file: 
                line = line.strip()
                if not line:
                    continue
                
                try:
                    name, salary = line.split(',')
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Помилка у рядку: {line}")
                    continue
            if count == 0:
                return 0, 0 
            return total, total // count
    except FileExistsError:
        print("Файл не знайдено.")
        return 0, 0


if __name__ == "__main__":
    total, average = total_salary("salary_file.txt")
    print (f'Загальна сумма заробітної плати: {total}, Середня заробітна плата: {average}') 
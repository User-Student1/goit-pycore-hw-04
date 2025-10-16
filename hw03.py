import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def print_directory_tree(path: Path, prefix: str = "", is_last=True, max_depth=2, current_depth=0):
    if current_depth > max_depth:
        return #обмеження до 2-го рівння

    connector = "┗ " if is_last else "┣ "
    folder_icon = "📂"
    file_icon = "📜"

    if prefix == "":
        print(Fore.BLUE + f"📦{path.name}" + Style.RESET_ALL) 
    else:
        if path.is_dir():
            print(prefix + connector + Fore.BLUE + folder_icon + path.name + "/" + Style.RESET_ALL)
        else:
            print(prefix + connector + Fore.GREEN + file_icon + path.name + Style.RESET_ALL) 

    if path.is_dir():
        # Можна додати фільтр для виключення непотрібних папок
        ignore_dirs = {'.git', 'venv', '__pycache__'}
        items = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower())) 
        items = [item for item in items if item.name not in ignore_dirs]

        count = len(items) 
        for index, item in enumerate(items):
            last = (index == count - 1) 
            new_prefix = prefix + ("   " if is_last else "┃  ") 
            print_directory_tree(item, new_prefix, last, max_depth, current_depth + 1) 

def main(): 
    if len(sys.argv) == 2: 
        dir_path = Path(sys.argv[1])
    else:
        user_input = input(Fore.CYAN + "🔹 Введіть шлях до директорії: " + Style.RESET_ALL) 
        dir_path = Path(user_input.strip('"').strip())

    if not dir_path.exists(): 
        print(Fore.RED + f"[Помилка] Шлях '{dir_path}' не шснує." + Style.RESET_ALL)
        return
    if not dir_path.is_dir(): 
        print (Fore.RED + f"[Помилка] Шлях '{dir_path}' не є директорією." + Style.RESET_ALL) 

    print(Fore.YELLOW + f"\n📁 структура директорії: {dir_path}\n" + Style.RESET_ALL) 
    print_directory_tree(dir_path) 

if __name__ == "__main__":     
    main() 

# шлях до директорії: C:\goit-pycore-hw-04\Picture
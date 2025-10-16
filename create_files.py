from pathlib import Path

def create_demo_structure(base_path):
    base = Path(base_path)
    logo = base / "Logo"

    # Створюємо папки
    logo.mkdir(parents=True, exist_ok=True)

    # Файли в кореневій директорії
    (base / "bot-icon.png").touch()
    (base / "mongodb.jpg").touch()

    # Файли в папці Logo
    (logo / "IBM+Logo.png").touch()
    (logo / "ibm.svg").touch()
    (logo / "logo-tm.png").touch()

    print(f"✅ Структура створена за шляхом: {base.resolve()}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Використання: python create_files.py <шлях_до_picture>")
        sys.exit(1)

    create_demo_structure(sys.argv[1])

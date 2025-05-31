import shutil
import argparse
from pathlib import Path

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_dir", type=str, help="Шлях до вихідної директорії")
    parser.add_argument("dest_dir", type=str, nargs="?", default="dest", help="Шлях до цільової директорії (за замовчуванням 'dest')")
    return parser.parse_args()

def copy_files_recursive(source_dir, dest_dir):
    try:
        source_path = Path(source_dir).resolve()
        dest_path = Path(dest_dir).resolve()

        if not source_path.exists():
            print(f"Помилка: Початкова директорія '{source_path}' не існує !")
            return
        if not source_path.is_dir():
            print(f"Помилка: Шлях '{source_path}' не є директорією !")
            return

        dest_path.mkdir(parents=True, exist_ok=True)

        for item in source_path.iterdir():
            try:
                if item.is_dir():

                    copy_files_recursive(item, dest_path)
                elif item.is_file():
                    extension = item.suffix.lower().lstrip('.')
                    if not extension:
                        extension = 'no_extension' 

                    extension_dir = dest_path / extension
                    extension_dir.mkdir(exist_ok=True)
                    dest_file_path = extension_dir / item.name

                    shutil.copy2(item, dest_file_path)
                    print(f"Скопійований файл: {item} -> {dest_file_path}")

            except PermissionError as e:
                print(f"Помилка доступу: {e} : {item})")
            except shutil.Error as e:
                print(f"Помилка копіювання: {e} : {item})")
            except Exception as e:
                print(f"Несподівана помилка при обробці {item}: {e}")

    except PermissionError as e:
        print(f"Помилка доступу до директорії {source_dir}: {e}")
    except Exception as e:
        print(f"Несподівана помилка при обробці директорії {source_dir}: {e}")

def main():
    args = parse_arguments()
    copy_files_recursive(args.source_dir, args.dest_dir)

if __name__ == "__main__":
    main()
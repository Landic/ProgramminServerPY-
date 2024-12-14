import json

def load_config(*file_paths):
    combined_config = {}
    
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                config = json.load(file)
                combined_config.update(config)
        except FileNotFoundError:
            print(f"Файл {file_path} не знайдено.")
        except json.JSONDecodeError as e:
            print(f"Помилка парсингу JSON у файлі {file_path}: {e}")
    
    return combined_config


def main():
    config = load_config("file1.json", "file2.json")
    print(config)

if __name__ == "__main__": main()

import json
import configparser
# import io

def update_json_hybrid(ini_path, json_path, output_path):
    # 1. Читаем INI файл вручную, чтобы обработать строки ДО первой секции
    translations = {}
    current_section = "common" # Секция по умолчанию для строк в начале файла
    
    try:
        with open(ini_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith(';') or line.startswith('#'):
                    continue
                
                # Если встретили заголовок секции [section]
                if line.startswith('[') and line.endswith(']'):
                    current_section = line[1:-1].strip()
                    continue
                
                # Если это строка с ключом key=value
                if '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip()
                    
                    # Формируем ключ: если секция common — просто ключ, иначе section.key
                    full_key = f"{current_section}.{key}" if current_section != "common" else key
                    translations[full_key] = value
                    # Также сохраняем вариант без common. для надежности
                    translations[key] = value 

    except Exception as e:
        print(f"Ошибка при чтении INI: {e}")
        return

    # 2. Загружаем JSON
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
    except Exception as e:
        print(f"Ошибка при чтении JSON: {e}")
        return

    updated_count = 0

    # 3. Замена TODO
    for key, value in json_data.items():
        if isinstance(value, str) and value.startswith("TODO:"):
            # Ищем: 1. Точное совпадение 2. Совпадение в нижнем регистре
            found_val = translations.get(key) or translations.get(key.lower())
            
            if found_val:
                json_data[key] = found_val
                updated_count += 1

    # 4. Сохранение
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
    
    print(f"Готово! Обновлено строк: {updated_count}")

INI_PATH = 'ini/locale_ru-RU.ini'
JSON_PATH = 'locale_ru-RU.json'
OUTPUT_PATH = 'locale_ru-RU_updated.json'

if __name__ == "__main__":
    update_json_hybrid(INI_PATH, JSON_PATH, OUTPUT_PATH)

#!/usr/bin/env python3
import re
import sys

def parse_locale_file(file_path):
    locale = {}
    current_section = None
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            
            # Skip empty lines and comments
            if not line or line.startswith(';') or line.startswith('#'):
                continue
                
            # Handle sections
            if line.startswith('[') and line.endswith(']'):
                current_section = line[1:-1]
                continue
                
            # Handle key-value pairs
            if '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                
                # Handle multi-line values
                if value.startswith('`') and not value.endswith('`'):
                    value_parts = [value[1:]]  # Remove the starting backtick
                    for next_line in f:
                        next_line = next_line.strip()
                        if next_line.endswith('`'):
                            value_parts.append(next_line[:-1])  # Remove the ending backtick
                            break
                        value_parts.append(next_line)
                    value = '\n'.join(value_parts)
                
                # Store the key with its section prefix if available
                full_key = f"{current_section}.{key}" if current_section else key
                locale[full_key] = value
    
    return locale

def main():
    if len(sys.argv) != 3:
        print("Usage: python compare_locales.py <en_file> <ru_file>")
        return
    
    en_file = sys.argv[1]
    ru_file = sys.argv[2]
    
    print("Loading English locale...")
    en_locale = parse_locale_file(en_file)
    print("Loading Russian locale...")
    ru_locale = parse_locale_file(ru_file)
    
    # Find missing keys in Russian locale
    missing_keys = []
    for key in en_locale:
        if key not in ru_locale:
            missing_keys.append(key)
    
    print(f"\nTotal keys in English: {len(en_locale)}")
    print(f"Total keys in Russian: {len(ru_locale)}")
    print(f"Missing keys in Russian: {len(missing_keys)}")
    
    # Group missing keys by section for better readability
    missing_by_section = {}
    for key in sorted(missing_keys):
        if '.' in key:
            section, subkey = key.split('.', 1)
            if section not in missing_by_section:
                missing_by_section[section] = []
            missing_by_section[section].append(subkey)
        else:
            if 'root' not in missing_by_section:
                missing_by_section['root'] = []
            missing_by_section['root'].append(key)
    
    # Print missing keys by section
    print("\nMissing keys by section:")
    for section in sorted(missing_by_section.keys()):
        print(f"\n[{section}]")
        for key in sorted(missing_by_section[section]):
            full_key = f"{section}.{key}" if section != 'root' else key
            print(f"{key}={en_locale[full_key]}")
    
    # Save missing keys to a file for easier translation
    with open('missing_translations.txt', 'w', encoding='utf-8') as f:
        f.write("# Missing Russian translations\n# Format: key=English translation\n# Add your translations after the equals sign\n\n")
        for section in sorted(missing_by_section.keys()):
            f.write(f"\n# [{section}]\n")
            for key in sorted(missing_by_section[section]):
                full_key = f"{section}.{key}" if section != 'root' else key
                f.write(f"{key}={en_locale[full_key]}\n")
    
    print("\nMissing keys have been saved to 'missing_translations.txt'")
    print("Please add the translations after the equals signs and save the file.")

if __name__ == "__main__":
    main()


# python compare_locales.py locale_en-US.ini locale_ru-RU.ini
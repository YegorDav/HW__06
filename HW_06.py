import os
import sys
import shutil

# список розширень для кожної категорії
IMAGE_EXT = ('JPEG', 'JPG', 'PNG', 'SVG')
VIDEO_EXT = ('AVI', 'MP4', 'MOV', 'MKV')
DOCUMENT_EXT = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
MUSIC_EXT = ('MP3', 'OGG', 'WAV', 'AMR')
ARCHIVE_EXT = ('ZIP', 'GZ', 'TAR')

# функція для перевірки розширення файлу та повернення категорії


def get_category(filename):
    ext = os.path.splitext(filename)[1][1:].upper()
    if ext in IMAGE_EXT:
        return 'images'
    elif ext in VIDEO_EXT:
        return 'videos'
    elif ext in DOCUMENT_EXT:
        return 'documents'
    elif ext in MUSIC_EXT:
        return 'music'
    elif ext in ARCHIVE_EXT:
        return 'archives'
    else:
        return 'unknown'

# функція для нормалізації імен файлів


def normalize(filename):
    # Створюємо словник для транслітерації
    translit_dict = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ie',
                     'ж': 'zh', 'з': 'z', 'и': 'y', 'і': 'i', 'ї': 'i', 'й': 'i', 'к': 'k', 'л': 'l',
                     'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
                     'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ь': '', 'ю': 'iu', 'я': 'ia'}

    # Перетворюємо всі літери рядка в нижній регістр
    filename = filename.lower()

    # Проходимося по кожному символу у рядку та перевіряємо, чи є він латинською літерою або цифрою
    # Якщо символ не є латинською літерою або цифрою, замінюємо його на "_"
    normalized_filename = ''
    for char in filename:
        if char.isalpha() and char.isascii():
            normalized_filename += char
        elif char.isdigit():
            normalized_filename += char
        else:
            normalized_filename += '_'

    # Проходимося по кожній букві у рядку та замінюємо кириличні символи на латинські за допомогою словника
    for cyrillic_char, latin_char in translit_dict.items():
        normalized_filename = normalized_filename.replace(
            cyrillic_char, latin_char)

    return normalized_filename

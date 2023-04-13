import os
import sys
import shutil

# список розширень файлів для кожної категорії
IMAGES = ('JPEG', 'JPG', 'PNG', 'SVG')
VIDEOS = ('AVI', 'MP4', 'MOV', 'MKV')
DOCUMENTS = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
MUSIC = ('MP3', 'OGG', 'WAV', 'AMR')
ARCHIVES = ('ZIP', 'GZ', 'TAR')

# функція для нормалізації імен файлів


def normalize(name):
    # транслітерація кириличних символів на латинські
    name = name.encode('translit/long')
    # заміна всіх символів крім латинських літер та цифр на _
    name = ''.join([c if c.isalnum() else '_' for c in name.decode()])
    return name

# функція для обробки папок та файлів


def process_folder(folder_path):
    # ініціалізація змінних для збереження списку файлів кожної категорії
    images_list = []
    videos_list = []
    documents_list = []
    music_list = []
    archives_list = []
    unknown_list = []
    # ініціалізація змінних для збереження списку відомих та невідомих розширень
    known_extensions = set()
    unknown_extensions = set()

    # прохід по всіх елементах в папці
    for item in os.listdir(folder_path):
        # повний шлях до елемента
        item_path = os.path.join(folder_path, item)
        # якщо це папка, рекурсивно обробляємо її
        if os.path.isdir(item_path):
            process_folder(item_path)
        # якщо це файл, обробляємо його
        elif os.path.isfile(item_path):
            # отримуємо розширення файлу
            extension = os.path.splitext(item)[1][1:].upper()
            # якщо розширення відоме, то додаємо файл до відповідної категорії
            if extension in IMAGES:
                images_list.append(item)
            elif extension in VIDEOS:
                videos_list.append(item)
            elif extension in DOCUMENTS:
                documents_list.append(item)
            elif extension in MUSIC:
                music_list.append(item)
            elif extension in ARCHIVES:
                archives_list.append(item)
            else:
                unknown_list.append(item)
                unknown_extensions.add(extension)

            # додаємо розширення до списку відомих розширень
            known_extensions.add(extension)


# створення папок для кожної категорії файлів
if images_list:
    images_folder = os.path.join(folder_path, 'Images')
    os.makedirs(images_folder, exist_ok=True)
    for file_name in images_list:
        file_path = os.path.join(folder_path, file_name)
        new_file_name = normalize(file_name)
        new_file_path = os.path.join(images_folder, new_file_name)
        shutil.move(file_path, new_file_path)

if videos_list:
    videos_folder = os.path.join(folder_path, 'Videos')
    os.makedirs(videos_folder, exist_ok=True)
    for file_name in videos_list:
        file_path = os.path.join(folder_path, file_name)
        new_file_name = normalize(file_name)
        new_file_path = os.path.join(videos_folder, new_file_name)
        shutil.move(file_path, new_file_path)

if documents_list:
    documents_folder = os.path.join(folder_path, 'Documents')
    os.makedirs(documents_folder, exist_ok=True)
    for file_name in documents_list:
        file_path = os.path.join(folder_path, file_name)
        new_file_name = normalize(file_name)
        new_file_path = os.path.join(documents_folder, new_file_name)
        shutil.move(file_path, new_file_path)

if music_list:
    music_folder = os.path.join(folder_path, 'Music')
    os.makedirs(music_folder, exist_ok=True)
    for file_name in music_list:
        file_path = os.path.join(folder_path, file_name)
        new_file_name = normalize(file_name)
        new_file_path = os.path.join(music_folder, new_file_name)
        shutil.move(file_path, new_file_path)

if archives_list:
    archives_folder = os.path.join(folder_path, 'Archives')
    os.makedirs(archives_folder, exist_ok=True)
    for file_name in archives_list:
        file_path = os.path.join(folder_path, file_name)
        new_file_name = normalize(file_name)
        new_file_path = os.path.join(archives_folder, new_file_name)
        shutil.move(file_path, new_file_path)

if unknown_list:
    unknown_folder = os.path.join(folder_path, 'Unknown')
    os.makedirs(unknown_folder, exist_ok=True)
    for file_name in unknown_list:
        file_path = os.path.join(folder_path, file_name)
        new_file_name = normalize(file_name)
        new_file_path = os.path.join(unknown_folder, new_file_name)
        shutil.move(file_path, new_file_path)

# виведення результатів
print(f'Processed folder: {folder_path}')
print(f'Number of files in each category:')
print(f'Images: {len(images_list)}')
print(f'Videos: {len(videos_list)}')
print(f'Documents: {len(documents_list)}')
print(f'Music: {len(music_list)}')
print(f'Archives: {len(archives_list)}')
print(f'Unknown: {len(unknown_list)}')
print(f'Known extensions: {", ".join(known_extensions)}')
print(f'Unknown extensions: {", ".join(unknown_extensions)}')

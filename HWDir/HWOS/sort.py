import os


source_dir = 'D:\DevProjects\PythonHW\PythonGIProject1\HWDir\HWOS\Sorting'

destinations = {
    'IMG': ['.png', '.jpg', '.jpeg', '.gif'],
    'TXT': ['.txt', '.doc',],
    'SOUND': ['.mp3',],
    'EXE': ['.exe', '.bat'],
    'OTHER': []}

def create_directories(base_dir, dest_folders):
    for folder in dest_folders:
        path = os.path.join(base_dir, folder)
        if not os.path.exists(path):
            os.makedirs(path)

def sort_files(source_dir, destinations):
    for file_name in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file_name)

        if os.path.isdir(file_path):
            continue

        ext = os.path.splitext(file_name)[1].lower()

        moved = False
        for folder, extensions in destinations.items():
            if ext in extensions:
                dest_folder = os.path.join(source_dir, '..', folder)
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                new_file_path = os.path.join(dest_folder, file_name)
                os.rename(file_path, new_file_path)
                print(f'Файл {file_name} перемещен в {folder}')
                moved = True
                break

        if not moved:
            dest_folder = os.path.join(source_dir, '..', 'OTHER')
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            new_file_path = os.path.join(dest_folder, file_name)
            os.rename(file_path, new_file_path)
            print(f'Файл {file_name} перемещен в OTHER')

base_dir = 'C:/Users/Ateyl/PycharmProjects/HWOS'

create_directories(base_dir, destinations.keys())

sort_files(source_dir, destinations)
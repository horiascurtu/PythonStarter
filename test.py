import os

# Calea de bază unde sunt folderele day1...day30
base_path = './'  # modifică dacă folderele sunt în altă parte

# Maparea pentru redenumirea fișierelor
file_rename_map = {
    'exercitii.py': 'exercises.py',
    'readme (1).md': 'README.md',
    'solutii.py': 'solutions.py'
}

for i in range(1, 31):
    old_folder_name = f'Day_{i:02d}'
    new_folder_name = f'Day_{i:02d}'

    old_folder_path = os.path.join(base_path, old_folder_name)
    new_folder_path = os.path.join(base_path, new_folder_name)

    # Redenumirea folderului dacă există
    if os.path.exists(old_folder_path):
        os.rename(old_folder_path, new_folder_path)
        print(f'Folder renamed: {old_folder_name} -> {new_folder_name}')
    else:
        print(f'Folder not found: {old_folder_name}')
        continue  # sărim dacă folderul nu există

    # Acum redenumim fișierele din folder
    for old_filename, new_filename in file_rename_map.items():
        old_file_path = os.path.join(new_folder_path, old_filename)
        new_file_path = os.path.join(new_folder_path, new_filename)

        if os.path.exists(old_file_path):
            os.rename(old_file_path, new_file_path)
            print(f'  File renamed: {old_filename} -> {new_filename}')
        else:
            print(f'  File not found: {old_filename} in {new_folder_name}')

import os
import shutil

# Set source and destination folders
source_folder = '/Users/your_username/Desktop/source_images'
destination_folder = '/Users/your_username/Desktop/moved_images'

# Create destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Loop through all files in the source folder
for filename in os.listdir(source_folder):
    if filename.lower().endswith('.jpg'):
        # Build full path
        src_path = os.path.join(source_folder, filename)
        dest_path = os.path.join(destination_folder, filename)

        # Move file
        shutil.move(src_path, dest_path)
        print(f'Moved: {filename}')

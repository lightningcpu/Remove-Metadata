import os
from PIL import Image

def remove_metadata(folder_path):
    # Define image file extensions to consider
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']

    # Iterate over each file in the folder
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            # Check if it's a file and if it has an image extension
            if os.path.isfile(file_path) and os.path.splitext(file_path)[1].lower() in image_extensions:
                # Load the image and remove its Exif data
                try:
                    img = Image.open(file_path)
                    img.save(file_path)  # This will remove the Exif data
                    print(f"Metadata removed from {file_path}")
                except Exception as e:
                    print(f"Failed to remove metadata from {file_path}: {e}")

# Specify the folder containing the files
folder_path = r"/path"
# Call the function to remove metadata from all files in the folder
remove_metadata(folder_path)
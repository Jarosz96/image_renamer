from PIL import Image
import os
import datetime

def get_datetime_and_device_from_metadata(image_path):
    try:
        with Image.open(image_path) as img:
            exif_data = img._getexif()
            if exif_data is not None:
                # Exif data tags for DateTimeOriginal and Make (camera make)
                date_time_original_tag = 36867
                make_tag = 271

                date_time = None
                device = None

                if date_time_original_tag in exif_data:
                    date_time_str = exif_data[date_time_original_tag]
                    date_time = datetime.datetime.strptime(date_time_str, '%Y:%m:%d %H:%M:%S')

                if make_tag in exif_data:
                    device = exif_data[make_tag]

                return date_time, device
    except Exception as e:
        print(f"Error while reading metadata for {image_path}: {e}")
    return None, None

def rename_images_with_datetime_and_device(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
            file_path = os.path.join(directory, filename)
            date_time, device = get_datetime_and_device_from_metadata(file_path)
            if date_time and device:
                new_filename = date_time.strftime('%Y%m%d_%H%M%S') + f"_{device}" + os.path.splitext(filename)[1]
                new_file_path = os.path.join(directory, new_filename)
                os.rename(file_path, new_file_path)
                print(f"Renamed {filename} -------> {new_filename}")

if __name__ == "__main__":
    # Replace 'your_directory_path' with the directory containing the pictures.
    # Make sure to back up your files before running the script.
    your_directory_path = "C:/Users/jaros/OneDrive/Skrivbord/New folder"
    rename_images_with_datetime_and_device(your_directory_path)
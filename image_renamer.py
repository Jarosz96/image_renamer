from PIL import Image
import os
import datetime

def get_datetime_and_device_from_metadata(image_path):
    try:
        with Image.open(image_path) as img:
            exif_data = img._getexif()
            if exif_data is not None:
                date_time_original_tag = 36867
                make_tag = 271
                image_date_time = 306
                image_timezoneoffset = 34858

                date_time = None
                device = None

                if make_tag in exif_data:
                    device = exif_data[make_tag]

                if date_time_original_tag in exif_data:
                    date_time_str = exif_data[date_time_original_tag]
                    date_time = datetime.datetime.strptime(date_time_str, '%Y:%m:%d %H:%M:%S')
                    return date_time, device
                elif image_date_time in exif_data:
                    date_time_str = exif_data[image_date_time]
                    date_time = datetime.datetime.strptime(date_time_str, '%Y:%m:%d %H:%M:%S')
                    return date_time, device
                elif image_timezoneoffset in exif_data:
                    date_time_str = exif_data[image_timezoneoffset]
                    date_time = datetime.datetime.strptime(date_time_str, '%Y:%m:%d %H:%M:%S')
                    return date_time, device

    except Exception as e:
        print(f"Error while reading metadata for {image_path}: {e}")
    return None, None

def check_image_file(filename):
    return filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', 'orf'))

def rename_images_with_datetime_and_device(directory):
    renamed_files = set()

    for filename in os.listdir(directory):
        if check_image_file(filename):
            file_path = os.path.join(directory, filename)
            date_time, device = get_datetime_and_device_from_metadata(file_path)
            if date_time and device:
                new_filename = date_time.strftime('%Y%m%d_%H%M%S') + f"_{device}" + os.path.splitext(filename)[1]
                new_file_path = os.path.join(directory, new_filename)
                try:
                    os.rename(file_path, new_file_path)
                    print(f"Renamed {filename} -------> {new_filename}")
                    renamed_files.add(new_filename)
                except Exception as e:
                    print(f"Error renaming {filename}: {e}")

    return renamed_files

def rename_images_with_creation_date(directory, renamed_files):
    for filename in os.listdir(directory):
        if check_image_file(filename):
            file_path = os.path.join(directory, filename)
            if filename not in renamed_files:
                creation_time = os.path.getctime(file_path)
                formatted_time = datetime.datetime.fromtimestamp(creation_time).strftime('%Y%m%d_%H%M%S')

                ignoremepls, file_extension = os.path.splitext(filename)
                new_file_name = f"{formatted_time}{file_extension}"
                new_file_path = os.path.join(directory, new_file_name)

                try:
                    os.rename(file_path, new_file_path)
                    print(f"Renamed {filename} -------> {new_file_name}")
                except Exception as e:
                    print(f"An error occurred: {e}")

if __name__ == "__main__":
    your_directory_path = "C:/Users/jaros/downloads/image_renamer"
    renamed_files = rename_images_with_datetime_and_device(your_directory_path)
    rename_images_with_creation_date(your_directory_path, renamed_files)
# image_renamer

## Introduction

This tool primarily focuses on standardizing image file names within a directory, making it easier to manage pictures from different sources, such as various cameras, screenshots, and downloaded files. It can also be used for other file types in the same directory.
![example](https://github.com/Jarosz96/image_renamer/blob/main/image.png?raw=true)

## Features

- **File Type Flexibility:** The tool supports various file types, allowing the user to select specific file extentions.
- **Bulk Renaming:** It efficiently renames multiple files at once, saving time and effort.

## Files

- `ORIGINAL_image_renamer.py`: my first iteration of which the code will be built on
- `image_renamer.py`: main file
- `image.png`: example picture

## Installation

1. Clone this repository:

```
git clone https://github.com/Jarosz96/image_renamer.git
```

2. Navigate to the project directory:

```
cd image_renamer
```

3. Install the required packages:

```
pip install -r requirements.txt
```

4. Copy the `.env.template` to a new file named `.env`. 

```
cp .env.template .env
```

5. Modify the `.env` file to specify the directory containing the images you want to rename. Save and exit.

6. Run the code:

```
python image_renamer.py
```

## Future Plans

This project is intended to undergo further development and add following features in future versions:

### Smarter Date Format

The code will choose the best date format for images with limited exif data, making file renaming based on their dates more accurate.

### Automated File Renaming

Future update will bring an automatic file renaming feature, cutting down manual work and making file naming easier for users.

### Log File Creation

The tool will create a log file to show what it's done, giving users transparency and a reference for the changes made during renaming.

### Customized naming format

Personalize and customize the file naming format according to your preferences.


## Known issues

- Duplicate files not named properly

## Author

- [Sebastian Jarosz](sebastian.jarosz96@gmail.com)

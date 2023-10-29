# image_renamer

This tool is designed to bring uniformity to file names within a directory by converting them to a standard format. 

## Introduction

This tool primarily focuses on standardizing image file names within a directory, making it easier to manage pictures from different sources, such as various cameras, screenshots, and downloaded files. It can also be used for other file types in the same directory.

## Features

- **File Type Flexibility:** The tool accommodates various file types, allowing the user to select specific types for standardization.
- **Bulk Renaming:** It efficiently renames multiple files at once, saving time and effort.

## Installation

To use the File Naming Format Standardizer, follow these steps:

1. Clone this repository:
`git clone https://github.com/Jarosz96/image_renamer.git`

2. Install PIL
`pip install Pillow`

3. Modify the code to specify the files whose naming format you want to change and select the directory of your choice. Save and exit.

4. Enter the directory:
`cd image_renamer`

5. Run the tool:
`python image_renamer.py`

## Future Plans

This project is intended to undergo further development and add following features in future versions:

### Work with All Types of Files

Future updates will extend the tool's capability to work with a wide range of file types beyond images, enabling users to standardize the naming format for various file categories within a directory.

### Smarter Date Format

The code will choose the best date format for images with limited date info, making file renaming based on their dates more accurate.

### Automated File Renaming

Future update will bring an automatic file renaming feature, cutting down manual work and making file naming easier for users.

### Log File Creation

The tool will create a log file to show what it's done, giving users transparency and a reference for the changes made during renaming.

### Smart Features Based on Exif Data

The tool will use image details like the type of camera used, location info, and other data from the images to help make better choices when renaming files.


## Known issues

- Duplicate files not named properly

## Author

- [Sebastian Jarosz](sebastian.jarosz96@gmail.com)

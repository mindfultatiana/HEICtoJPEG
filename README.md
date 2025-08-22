# HEICtoJPEG
I created an HEIC to JPEG converter script in python. Sometimes iphone is preset to save files in HEIC which can be frustrating when uploading them to applications. This converter can be run in python to instantly convert all HEIC files in a folder to JPEG.

## Dependancies
1. You need to have python and pip installed.
2. Install Pillow with pip in the command line.
```
pip install Pillow pillow-heif
```
## Instructions
1. Update the proper file paths in the script.
```
# Predefined folder paths
source_folder = r"C:\Users\Username\Downloads\OldPhotos"
destination_folder = r"C:\Users\Username\Downloads\NewPhotos"
```
2. Find the correct folder in the command line.
```
Users\Username cd Downloads
```
3. Run the python script.
```
Users\Username\Downloads python.exe heic_converter.py
```
```
✓ Converted: IMG_7228.HEIC → IMG_7228.jpg
✓ Converted: IMG_7229.HEIC → IMG_7229.jpg
✓ Converted: IMG_7230.HEIC → IMG_7230.jpg
✓ Converted: IMG_7231.HEIC → IMG_7231.jpg
✓ Converted: IMG_7232.HEIC → IMG_7232.jpg
✓ Converted: IMG_7233.HEIC → IMG_7233.jpg
✓ Converted: IMG_7234.HEIC → IMG_7234.jpg
✓ Converted: IMG_7235.HEIC → IMG_7235.jpg
✓ Converted: IMG_7236.HEIC → IMG_7236.jpg
------------------------------
Conversion complete!
Successful: 142
Failed: 0
Total processed: 142
```
Your converted files should be in your new location.
## Optional
When running the program you can choose the quality you want the outcoming JPEG to be from a 1-100 scale
```
Users\Username\Downloads python.exe heic_converter.py 90
```

#requirements: pip install Pillow
import os
from PIL import Image

def resize_image(input_path, output_path, target_size):
    with Image.open(input_path) as image:
        resized_image = image.resize(target_size)
        resized_image.save(output_path)

input_dir = input("Enter the path of the input directory: ")
output_dir = input("Enter the path of the output directory: ")
width = int(input("Enter the desired width in pixels: "))
height = int(input("Enter the desired height in pixels: "))
target_size = (width, height)

for filename in os.listdir(input_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        resize_image(input_path, output_path, target_size)
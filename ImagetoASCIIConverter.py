import PIL.Image

# Define ASCII character set
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    """Resize the image to a new width and return as a PIL.Image object."""
    width, height = image.size
    new_height = new_width * height // width
    resized_image = image.resize((new_width, new_height))
    return resized_image

def convert_to_grayscale(image):
    """Convert the image to grayscale and return as a PIL.Image object."""
    grayscale_image = image.convert("L")
    return grayscale_image

def convert_to_ascii(image):
    """Convert the image to ASCII art and return as a string."""
    # get pixel data from image
    pixels = image.getdata()

    # determine scaling factor to fit pixel values within range of ASCII_CHARS
    scale_factor = 255 / (len(ASCII_CHARS) - 1)

    # convert each pixel to an ASCII character based on its brightness
    ascii_chars = [ASCII_CHARS[int(pixel / scale_factor)] for pixel in pixels]

    # group the ASCII characters into rows and return as a string
    rows = ["".join(ascii_chars[i:i+image.width]) for i in range(0, len(ascii_chars), image.width)]
    ascii_image = "\n".join(rows)

    return ascii_image

def main():
    # prompt user to input path of image file
    image_path = input("Enter path of image file: ")

    # open image and convert to ASCII art
    with PIL.Image.open(image_path) as image:
        resized_image = resize_image(image)
        grayscale_image = convert_to_grayscale(resized_image)
        ascii_image = convert_to_ascii(grayscale_image)

        # display ASCII art
        print(ascii_image)

if __name__ == '__main__':
    main()

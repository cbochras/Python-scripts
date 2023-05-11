from PIL import Image, ImageFilter

# Open the image file
image = Image.open("example.jpg")

# Resize the image
new_size = (image.size[0]//2, image.size[1]//2)
resized_image = image.resize(new_size)

# Apply a filter to the image
filtered_image = resized_image.filter(ImageFilter.BLUR)

# Save the edited image
filtered_image.save("edited.jpg")

import os
from PIL import Image, ImageDraw, ImageFont

# Open image file
image = Image.open("image.jpg")

# Define font and font size
font_path = "Muroslant.otf"
# Set font size proportional to image height
font_size = int(image.size[1] / 3)

# Create font object
font = ImageFont.truetype(font_path, font_size)

# Define text to be added to image
text = "mr beast"

# Create text layer
text_layer = Image.new('RGBA', image.size, (255, 255, 255, 0))
text_draw = ImageDraw.Draw(text_layer)

# Calculate text size and position
text_width, text_height = text_draw.textsize(text, font=font)
x = (image.size[0] - text_width) / 2
y = (image.size[1] - text_height) / 2

# Add text to text layer
text_draw.text((x, y), text, font=font, fill=(255, 255, 255, 255))

# Merge text layer with image
result = Image.alpha_composite(image.convert('RGBA'), text_layer)

# Save result image as PNG
filename = "result.png"
if os.path.exists(filename):
    i = 1
    while True:
        new_filename = f"result_{i}.png"
        if not os.path.exists(new_filename):
            filename = new_filename
            break
        i += 1
result.save(filename)

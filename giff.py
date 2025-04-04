import imageio.v3 as imageio
import numpy as np
from PIL import Image  # To resize images

fn = ['t1.png', 't2.png']
img = []

# Load and resize images to the same size
def resize_image(image, size):
    return np.array(Image.fromarray(image).resize(size))

# Read first image to get the target size
first_img = imageio.imread(fn[0])
target_size = first_img.shape[:2][::-1]  # (width, height)

img.append(first_img)  # Add first image
for f in fn[1:]:
    img.append(resize_image(imageio.imread(f), target_size))

# Save GIF
imageio.imwrite('t.gif', img, duration=500, loop=0)

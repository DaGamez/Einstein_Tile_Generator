from pattern_generator import *
from graphics_cv2 import *
import numpy as np

SCALAR = 30
OUTPUT_FILE = "einstein_pattern.png"

# Generate pattern
for i in range(6):
    next_generation()

# Create output image
output_image = np.full((2000, 2000, 3), 255)  # White background

# Draw all tiles
for tile in vertices_to_draw:
    output_image = draw_tile(tile, output_image)

# Save the image
cv2.imwrite(OUTPUT_FILE, output_image)
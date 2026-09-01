#!/usr/bin/env python3
"""Regenerate hiro_marker.png from the .patt file with correct RGB mode."""
from PIL import Image

patt = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1],  # Hiro ID 2: position of the "hole" varies by ID
    [1, 1, 1, 1, 1, 1],
]

# Hiro ID 2 has the dot at position (4,3) - bottom row, 4th column
# Hiro ID 1: (4,3)
# Hiro ID 2: (4,3)  
# Hiro ID 3: (4,2)
# Hiro ID 4: (4,2)

# Let's check the actual Hiro marker patterns
# Hiro ID 2 pattern (from ARToolKit):
# 1 1 1 1 1 1
# 1 0 0 0 0 1
# 1 0 0 0 0 1
# 1 0 0 0 0 1
# 1 0 0 0 1 1
# 1 1 1 1 1 1

size = 120
grid_size = 6
cell_size = size // grid_size  # 20

img = Image.new('RGB', (size, size), (255, 255, 255))
pixels = img.load()

for y in range(grid_size):
    for x in range(grid_size):
        if patt[y][x] == 0:
            for dy in range(cell_size):
                for dx in range(cell_size):
                    pixels[x * cell_size + dx, y * cell_size + dy] = (0, 0, 0)

img.save('hiro_marker.png')
print(f"hiro_marker.png regenerated: {size}x{size}, mode=RGB")

# Also verify
img2 = Image.open('hiro_marker.png')
print(f"Verify: format={img2.format}, size={img2.size}, mode={img2.mode}")

import os
from datetime import datetime

from generate import generate_hierarchical_tile_image

time = datetime.now()
day_percentage = time.hour / 24 + time.minute / 60 / 24
image = generate_hierarchical_tile_image((3840, 2160), 5, 0.0, 1.0, 0.7, 1.0, 0.0, 1.0 - day_percentage)
with open(os.path.expanduser('~/Desktop/time-dependent-background.png'), 'wb') as fout:
    image.save(fout, 'PNG')
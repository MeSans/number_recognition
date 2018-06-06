# 64 bit with pillow:
from PIL import Image
import numpy as np
# open up the image
i = Image.open('images/floy.png')
# convert our image to a pixel array
iar = np.asarray(i)
# print that stuff out
print(iar)

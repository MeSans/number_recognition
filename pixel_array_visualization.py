####
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

###
i = Image.open('images/dot.png')

iar = np.asarray(i)


plt.imshow(iar)
print(iar)
plt.show()
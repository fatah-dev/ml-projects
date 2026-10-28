import numpy as np
x=np.random.rand(64,64)

import matplotlib.pyplot as plt
plt.clf()

plt.imshow(x,cmap='hot')
plt.colorbar()
plt.show()

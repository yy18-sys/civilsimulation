from matplotlib import pyplot
import numpy as np
from Code.element import Element

world = np.ndarray(shape=(20, 20), dtype=Element)

world[1][1] = Ground()

print(world)

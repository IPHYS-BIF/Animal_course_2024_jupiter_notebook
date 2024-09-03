import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


if __name__ == '__main__':
    x = np.linspace(-89.5, 89.5, 180)
    y = pd.read_clipboard(header=None)
    y = y.to_numpy().flatten()
    print(y.shape)
    plt.bar(x, y, width=1.0, facecolor='blue', edgecolor='blue')
    plt.xlabel("Orientation (degrees)")
    plt.ylabel("Frequency")
    plt.show()
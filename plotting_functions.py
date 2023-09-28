import numpy as np
import matplotlib.pyplot as plt

import main


def plot_eval_over_n(max_n: int):
    outputs = []
    for i in np.arange(100, max_n, 100):
        out1 = main.first_integration(i)
        outputs.append([out1])

    plt.plot(outputs)
    plt.show()


if __name__ == "__main__":
    plot_eval_over_n(100000)

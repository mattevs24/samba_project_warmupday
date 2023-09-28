import numpy as np
import matplotlib.pyplot as plt
import typing

import main


def plot_eval_over_n(max_n: int):
    outputs = []
    for i in np.arange(100, max_n, 100):
        out1 = main.first_integration(i)
        outputs.append([out1])

    labels = np.arange(100, max_n, 100)
    plt.plot(labels, outputs, 'r')
    plt.show()


def plot_more_efficient(integrand: typing.Callable[[np.ndarray, np.ndarray], np.ndarray], max_n: int, samples: int):
    outputs = []
    running_total_samples = samples
    running_sum = 0.0
    for _ in np.arange(100, max_n, samples):
        out1 = main.first_integration(integrand, samples)
        out1 *= float(samples)
        running_sum += out1
        running_total_samples += samples
        out1 = running_sum / float(running_total_samples)
        outputs.append([out1])

    labels = np.arange(100, max_n, samples)
    plt.plot(labels, outputs, 'r')
    plt.show()


if __name__ == "__main__":
    plot_more_efficient(main.func1, 20000, samples=100)

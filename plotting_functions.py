import numpy as np
import matplotlib.pyplot as plt
import typing
import scipy.stats as stats

import main


def plot_eval_over_n(max_n: int):
    outputs = []
    for i in np.arange(100, max_n, 100):
        out1 = main.first_integration(i)
        outputs.append([out1])

    labels = np.arange(100, max_n, 100)
    plt.plot(labels, outputs, 'r')
    plt.show()


def plot_more_efficient(integrand: typing.Callable[[np.ndarray, np.ndarray], np.ndarray],
                        density: stats.rv_continuous, max_n: int, samples: int):
    outputs = []
    running_total_samples = samples
    running_sum = 0.0
    for _ in np.arange(100, max_n, samples):
        out1 = main.first_integration(integrand, density, 0.0, 1.0, samples)
        out1 *= float(samples)
        running_sum += out1
        running_total_samples += samples
        out1 = running_sum / float(running_total_samples)
        outputs.append([out1])

    labels = np.arange(100, max_n, samples)
    plt.plot(labels, outputs, 'r')
    plt.show()


def plot_unif_norm_convergences(integrand: typing.Callable[[np.ndarray, np.ndarray], np.ndarray],
                                max_n: int, samples: int, **kwargs):
    outputs_unif = []
    outputs_norm = []
    running_total_samples = samples
    running_sum_unif = 0.0
    running_sum_norm = 0.0
    for _ in np.arange(100, max_n, samples):
        out_unif = main.first_integration(integrand, stats.uniform, {}, 0.0, 1.0, samples)
        out_norm = main.first_integration(integrand, stats.norm, kwargs, 0.0, 1.0, samples)
        out_unif *= float(samples)
        out_norm *= float(samples)
        running_sum_unif += out_unif
        running_sum_norm += out_norm

        out_unif = running_sum_unif / float(running_total_samples)
        out_norm = running_sum_norm / float(running_total_samples)
        outputs_unif.append([out_unif])
        outputs_norm.append([out_norm])

        running_total_samples += samples

    labels = np.arange(100, max_n, samples)
    plt.plot(labels, outputs_unif, 'r')
    plt.plot(labels, outputs_norm, 'g')
    plt.savefig("output1.png")
    plt.show()


if __name__ == "__main__":
    plot_unif_norm_convergences(main.func1, 50000, samples=100)

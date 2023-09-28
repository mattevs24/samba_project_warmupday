import numpy as np


def rand_vec(n: int) -> np.ndarray:
    """
    Function to generate a vector of length $n$ with uniformly distributed variabels between 0 and 1
    :param n:
    :return:
    """
    return np.random.uniform(size=n)


if __name__ == "__main__":
    vec = rand_vec(10)
    print(vec)

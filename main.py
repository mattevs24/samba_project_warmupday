import numpy as np


def rand_vec(n: int) -> np.ndarray:
    """
    Function to generate a vector of length $n$ with uniformly distributed variabels between 0 and 1
    :param n:
    :return:
    """
    return np.random.uniform(size=n)


def first_integration(n: int = 10000) -> float:

    def func1(x, y):
        return 1.0 / (1.0 + np.sin(x)**2 + np.sin(y)**2)

    vec_x, vec_y = rand_vec(n), rand_vec(n)

    _eval = func1(vec_x, vec_y)
    _eval = _eval.mean()

    return _eval


if __name__ == "__main__":
    out = first_integration()
    print(out)

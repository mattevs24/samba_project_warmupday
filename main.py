import numpy as np
import typing
import scipy.stats as stats


def naive_points_generation(density: stats.rv_continuous,
                            lower_bound: float, upper_bound: float, n: int, **kwargs) -> np.ndarray:
    points = density.rvs(size=n, **kwargs)
    lower_check = points >= lower_bound
    upper_check = points <= upper_bound
    pointsin = np.logical_and(lower_check, upper_check)
    points = points[pointsin]
    while len(points) < n:
        supplementary_points = density.rvs(size=n, **kwargs)
        lower_check = supplementary_points >= lower_bound
        upper_check = supplementary_points <= upper_bound
        pointsin = np.logical_and(lower_check, upper_check)
        supplementary_points = supplementary_points[pointsin]

        points = np.r_[points, supplementary_points]

    points = points[:n]
    return points


def func1(x, y):
    return 1.0 / (1.0 + np.sin(x)**2 + np.sin(y)**2)


def first_integration(integrand: typing.Callable[[np.ndarray, np.ndarray], np.ndarray],
                      density: stats.rv_continuous, lower_bound: float = 0.0,
                      upper_bound: float = 1.0, n: int = 100000) -> float:

    vec_x = naive_points_generation(density, lower_bound, upper_bound, n)
    vec_y = naive_points_generation(density, lower_bound, upper_bound, n)

    _eval_top = integrand(vec_x, vec_y)
    _eval_bottom = density.pdf(vec_x) * density.pdf(vec_y)
    correction_term = (density.cdf(upper_bound) - density.cdf(lower_bound))**2

    _eval = _eval_top / _eval_bottom * correction_term
    _eval = _eval.mean()

    return _eval


if __name__ == "__main__":
    out = first_integration(func1, stats.norm)
    print(out)

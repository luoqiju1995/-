import numpy as np
import matplotlib.pyplot as plt


def gradient_descent(grad_fn, x0, learn_rate, n_iter=50, tolerance=1e-6, verbose=False):
    x = x0
    xs = [x0]
    for i in range(n_iter):
        diff = -learn_rate * grad_fn(x)
        if np.all(np.abs(diff) <= tolerance):
            break
        x += diff
        xs.append(x)
        if verbose:
            print(f'{i}: {xs[-2]:.3f}, {diff:.2f}={learn_rate:.3f}*{grad_fn(xs[-2]):.3f}, {xs[-1]:.3f}')
    return x, xs


def gradient_ascent(grad_fn, x0, learn_rate, n_iter=50, tolerance=1e-6, verbose=False):
    x = x0
    xs = [x0]
    for i in range(n_iter):
        diff = learn_rate * grad_fn(x)
        if np.all(np.abs(diff) <= tolerance):
            break
        x += diff
        xs.append(x)
        if verbose:
            print(f'{i}: {xs[-2]:.3f}, {diff:.2f}={learn_rate:.3f}*{grad_fn(xs[-2]):.3f}, {xs[-1]:.3f}')
    return x, xs


def draw(xs):
    plt.plot(np.arange(-3, 3, 0.01), [f(x) for x in np.arange(-3, 3, 0.01)])
    plt.plot(xs, [f(x) for x in xs], 'o-', color='g')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()


if __name__ == '__main__':
    f = lambda x: x**4 - 5*x**2 - 3*x
    grad_fn = lambda x: 4 * x**3 - 10*x -3
    # x, xs = gradient_descent(grad_fn=grad_fn, x0=0, learn_rate=0.2, verbose=True)
    # x, xs = gradient_descent(grad_fn=grad_fn, x0=0, learn_rate=0.1, verbose=True, n_iter=1000)
    x, xs = gradient_descent(grad_fn=grad_fn, x0=0, learn_rate=0.01, verbose=True, n_iter=1000)
    draw(xs)

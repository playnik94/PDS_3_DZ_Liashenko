import numpy as np
import matplotlib.pyplot as plt

x = np.array([5, 15, 25, 35, 45, 55])
y = np.array([5, 20, 14, 32, 22, 38])


class Grad:

    def __init__(self, x, y, start, learn_r, n_iter, tolerance=1e-06):
        self.tolerance = tolerance
        self.x = x
        self.y = y
        self.start = start
        self.learn_r = learn_r
        self.n_iter = n_iter

    def gradient_descent(self):

        vector = self.start
        for i in range(self.n_iter):
            diff = -self.learn_r * np.array(self.ssr_gradient(self.x, self.y, vector))
            if np.all(np.abs(diff) <= self.tolerance):
                break
            vector += diff
        return vector

    def ssr_gradient(self, x, y, b):
        res = b[0] + b[1] * x - y
        return res.mean(), (res * x).mean()

#
# g = Grad(x=x, y=y, start=[0.5,0.5], learn_r=0.0008, n_iter=100_000)
# print(g.gradient_descent())


# def ssr_gradient(x, y, b):
#     res = b[0] + b[1] * x - y
#     return res.mean(), (res * x).mean()
#
#
# def sgd(
#     gradient, x, y, start, learn_rate=0.1, batch_size=1, n_iter=50,
#     tolerance=1e-06, dtype="float64", random_state=None
# ):
#     # Checking if the gradient is callable
#     if not callable(gradient):
#         raise TypeError("'gradient' must be callable")
#
#     # Setting up the data type for NumPy arrays
#     dtype_ = np.dtype(dtype)
#
#     # Converting x and y to NumPy arrays
#     x, y = np.array(x, dtype=dtype_), np.array(y, dtype=dtype_)
#     n_obs = x.shape[0]
#     if n_obs != y.shape[0]:
#         raise ValueError("'x' and 'y' lengths do not match")
#     xy = np.c_[x.reshape(n_obs, -1), y.reshape(n_obs, 1)]
#
#     # Initializing the random number generator
#     seed = None if random_state is None else int(random_state)
#     rng = np.random.default_rng(seed=seed)
#
#     # Initializing the values of the variables
#     vector = np.array(start, dtype=dtype_)
#
#     # Setting up and checking the learning rate
#     learn_rate = np.array(learn_rate, dtype=dtype_)
#     if np.any(learn_rate <= 0):
#         raise ValueError("'learn_rate' must be greater than zero")
#
#     # Setting up and checking the size of minibatches
#     batch_size = int(batch_size)
#     if not 0 < batch_size <= n_obs:
#         raise ValueError(
#             "'batch_size' must be greater than zero and less than "
#             "or equal to the number of observations"
#         )
#
#     # Setting up and checking the maximal number of iterations
#     n_iter = int(n_iter)
#     if n_iter <= 0:
#         raise ValueError("'n_iter' must be greater than zero")
#
#     # Setting up and checking the tolerance
#     tolerance = np.array(tolerance, dtype=dtype_)
#     if np.any(tolerance <= 0):
#         raise ValueError("'tolerance' must be greater than zero")
#
#     # Performing the gradient descent loop
#     for _ in range(n_iter):
#         # Shuffle x and y
#         rng.shuffle(xy)
#
#         # Performing minibatch moves
#         for start in range(0, n_obs, batch_size):
#             stop = start + batch_size
#             x_batch, y_batch = xy[start:stop, :-1], xy[start:stop, -1:]
#
#             # Recalculating the difference
#             grad = np.array(gradient(x_batch, y_batch, vector), dtype_)
#             diff = -learn_rate * grad
#
#             # Checking if the absolute difference is small enough
#             if np.all(np.abs(diff) <= tolerance):
#                 break
#
#             # Updating the values of the variables
#             vector += diff
#             print(vector)
#
#     return vector if vector.shape else vector.item()


# x = sgd(ssr_gradient, x, y, start=[0.5, 0.5], learn_rate=0.0008, batch_size=3, n_iter=100_000, random_state=0)

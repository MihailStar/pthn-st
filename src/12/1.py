import numpy as np

# 1
l = [12.23, 13.32, 100, 36.32]
a = np.array(l)

print("Original List:", l)
print("One-dimensional NumPy array: ", a)

assert str(a) == "[ 12.23  13.32 100.    36.32]"


# 2
x = np.arange(2, 11).reshape(3, 3)
print(x)

assert (
    str(x)
    == """[[ 2  3  4]
 [ 5  6  7]
 [ 8  9 10]]"""
)


# 3
x = np.ones((3, 3))
print("Исходный массив:")
print(x)

x = np.pad(x, pad_width=1, mode="constant", constant_values=0)
print("0 по краям и 1 внутри массива:")
print(x)

assert (
    str(x)
    == """[[0. 0. 0. 0. 0.]
 [0. 1. 1. 1. 0.]
 [0. 1. 1. 1. 0.]
 [0. 1. 1. 1. 0.]
 [0. 0. 0. 0. 0.]]"""
)


# 4
import numpy.typing as npt

x = np.ones((5, 5))
print("Исходный массив")
print(x)


def border_ones(x: npt.NDArray[np.float64]) -> None:
    x[1:-1, 1:-1] = 0


border_ones(x)
print("1 по краям и 0 внутри массива:")
print(x)

assert (
    str(x)
    == """[[1. 1. 1. 1. 1.]
 [1. 0. 0. 0. 1.]
 [1. 0. 0. 0. 1.]
 [1. 0. 0. 0. 1.]
 [1. 1. 1. 1. 1.]]"""
)

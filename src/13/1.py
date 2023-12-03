import matplotlib.pyplot as plt

# 1
x1 = [10, 20, 30]
y1 = [20, 40, 10]

x2 = [10, 20, 30]
y2 = [40, 10, 30]


a = plt.plot(x1, y1, color="blue", linewidth=3)

b = plt.plot(
    x2,
    y2,
    color="red",
    linestyle="dashdot",
    linewidth=3,
    marker="o",
    markerfacecolor="blue",
    markersize=12,
)

plt.xlabel("x")
plt.ylabel("y")


plt.show()

assert a[0].get_color() in ["b", "blue"]
assert b[0].get_color() in ["r", "red"]

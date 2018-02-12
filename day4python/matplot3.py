import matplotlib.pyplot as plot

def f(x):
    if x % 2 == 0:
        print(-1)
    else:
        print(1)
xs = list(range(-5, 5))
ys = []
for x in xs:
    ys.append(f(x))
plot.plot (xs, ys)
plot.show()
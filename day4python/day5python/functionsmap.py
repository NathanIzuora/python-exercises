import  matplotlib.pyplot as plt

x_ = []
y_ = []
for x in range(-5,6):
    x_.append(x)
    if x % 2 == 0:
        y_.append(-1)
    else:
        Y_.append(1)

plt.bar(x_, y_)



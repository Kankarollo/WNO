import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

r = input("Podaj promien okregu: ").split()
r = float(r[0])


def cykloida1(i):
    x = r * (i / 100 - np.sin(i / 100))
    y = r * (1 - np.cos(i / 100))
    return x, y


def cykladwa(i):
    x = (r * (i / 100 - np.sin(i / 100)) - np.sin(r * (i / 100 - np.sin(i / 100))))
    y = 1 + (r * (1 - np.cos(i / 100)) - np.cos(r * (i / 100 - np.sin(i / 100))))
    return x, y


def okrag(i):
    t = np.arange(0, 7, 0.01)
    x = r * np.sin(t) + r * i / 100
    y = r * np.cos(t) + r
    return x, y


def okrag2(i):
    t = np.arange(0, 7, 0.01)
    x = 1 * np.sin(t) + r * (i / 100 - np.sin(i / 100))
    y = 1 * np.cos(t) + 1 + r * (1 - np.cos(i / 100))
    return x, y


def linia(i):
    x_p = r * i / 100
    y_p = r
    x_k = r * (i / 100 - np.sin(i / 100))
    y_k = r * (1 - np.cos(i / 100))
    x = [x_p, x_k]
    y = [y_p, y_k]
    return x, y


def linia2(i):
    x_p = r * (i / 100 - np.sin(i / 100))
    y_p = r * (1 - np.cos(i / 100))
    x_k = (r * (i / 100 - np.sin(i / 100)) - np.sin(r * (i / 100 - np.sin(i / 100))))
    y_k = r + (r * (1 - np.cos(i / 100)) - np.cos(r * (i / 100 - np.sin(i / 100))))
    x = [x_p, x_k]
    y = [y_p, y_k]
    return x, y


fig, ax = plt.subplots()
plt.xlim(-2, 6 * 3 * r)
plt.ylim(0, 6 * 3 * r)

x_c, y_c = [cykloida1(0)[0]], [cykloida1(0)[1]]
line_c, = ax.plot(x_c, y_c)
x_c1, y_c1 = [cykladwa(0)[0]], [cykladwa(0)[1]]
line_c1, = ax.plot(x_c1, y_c1, 'c')
line_o, = ax.plot(okrag(0)[0], okrag(0)[1])
line_l, = ax.plot(linia(0)[0], linia(0)[1])
line_o2, = ax.plot(okrag2(0)[0], okrag2(0)[1], 'k')


def animacja(i, line_c, line_o, line_l, line_c1, line_o2):
    x_c.append(cykloida1(i)[0])
    y_c.append(cykloida1(i)[1])
    line_c.set_data(x_c, y_c)
    x_c1.append(cykladwa(i)[0])
    y_c1.append(cykladwa(i)[1])
    line_c1.set_data(x_c1, y_c1)
    x_o = okrag(i)[0]
    y_o = okrag(i)[1]
    line_o.set_data(x_o, y_o)
    x_o2 = okrag2(i)[0]
    y_o2 = okrag2(i)[1]
    line_o2.set_data(x_o2, y_o2)
    x_l = linia(i)[0]
    y_l = linia(i)[1]
    line_l.set_data(x_l, y_l)
    return line_c, line_o, line_l, line_c1, line_o2


ani = animation.FuncAnimation(fig, animacja, fargs=[line_c, line_o, line_l, line_c1, line_o2], blit=True, interval=10)

plt.show()
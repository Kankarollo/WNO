import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

# N = input("Ile losowych punktow ma byc narysowanych?: ")
N = 30
punkty = np.random.rand(N, 2) * 100

punkty2 = []

for i in range(N):
    punkty2.append([punkty[i, 0], punkty[i, 1]])
punkty2.sort(key=lambda x: x[0])


def kierunek(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])


lower = []
for p in punkty2:
    while len(lower) >= 2 and kierunek(lower[-2], lower[-1], p) <= 0:
        lower.pop()
    lower.append(p)

upper = []
for p in reversed(punkty2):
    while len(upper) >= 2 and kierunek(upper[-2], upper[-1], p) <= 0:
        upper.pop()
    upper.append(p)

otoczka = np.asarray(lower + upper)

fig, ax = plt.subplots()
line, = ax.plot(otoczka[:, 0], otoczka[:, 1])

line.axes.axis([0, 100, 0, 100])


def animated_otoczka(num):
    line.set_data(otoczka[:, 0][:num], otoczka[:, 1][:num])
    return line,


plt.plot(punkty[:, 0], punkty[:, 1], linestyle="None", marker='o')

# plt.plot(otoczka[:, 0], otoczka[:, 1])

animacja = ani.FuncAnimation(fig, animated_otoczka, len(otoczka)+1, interval=200, repeat=False)

plt.show()

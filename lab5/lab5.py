import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.arange(1,100)
    y = np.arange(1,100)

    print(x)
    print(y)

    X,Y = np.meshgrid(x,y)
    print(X)
    print(Y)

    plt.plot(X,Y,marker = '.',linestyle='None')
    plt.show()

def test():
    pass

if __name__ == '__main__':
    test()
    main()
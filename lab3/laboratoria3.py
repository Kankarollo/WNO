from itertools import product

import matplotlib.pyplot as plt
import matplotlib.image as img
import matplotlib.colors as col
import numpy as np

image_name = "lenna.png"

img_data = img.imread(image_name)[:, :, :3]


def test():
    pass


def rgb2hsvMINE(r, g, b):
    MAX = np.maximum(r, g)
    MAX = np.maximum(MAX, b)
    MIN = np.minimum(MAX, b)
    df = MAX - MIN
    if MAX.all() == MIN.all():
        h = 0
    elif MAX == r:
        h = (60 * ((g - b) / df) + 360) % 360
    elif MAX == g:
        h = (60 * ((b - r) / df) + 120) % 360
    elif MAX == b:
        h = (60 * ((r - g) / df) + 240) % 360
    if MAX.all() == 0:
        s = 0
    else:
        s = df / MAX
    v = MAX
    return h, s, v


def image_to_sobel(image):
    sobel_image = np.zeros(image.shape)
    for i, j in product(range(image.shape[0] - 2), range(image.shape[1] - 2)):
        pixel_mask = image[i:i + 3, j:j + 3]
        g_x = pixel_mask[0, 0, 0] + 2 * pixel_mask[1, 0, 0] + pixel_mask[2, 0, 0] - pixel_mask[0, 2, 0] - 2 * \
              pixel_mask[1, 2, 0] - pixel_mask[2, 2, 0]
        g_y = pixel_mask[0, 0, 0] + 2 * pixel_mask[0, 1, 0] + pixel_mask[0, 2, 0] - pixel_mask[2, 0, 0] - 2 * \
              pixel_mask[2, 1, 0] - pixel_mask[2, 2, 0]
        g = np.sqrt(g_x ** 2 + g_y ** 2)
        sobel_image[i, j, 0] = g
    sobel_image[:, :, 1] = sobel_image[:, :, 0]
    sobel_image[:, :, 2] = sobel_image[:, :, 0]
    return sobel_image


def hist_converter(image):
    """
NOT ENDED
    :param image:
    """
    y = 0
    x = 0
    lista_punktow = []
    for number in image:
        if number is not x:
            lista_punktow.append([x, y])
            x = number
        else:
            y += 1
        return np.asarray(lista_punktow)


def main():
    r = img_data[:, :, 0]
    g = img_data[:, :, 1]
    b = img_data[:, :, 2]

    [h, s, v] = rgb2hsvMINE(r, g, b)
    hsv = np.zeros(img_data.shape)
    hsv[:, :, 0] = h
    hsv[:, :, 1] = s
    hsv[:, :, 2] = v

    hsv2 = col.rgb_to_hsv(img_data.copy())
    rgb2 = col.hsv_to_rgb(hsv)
    rgb3 = col.hsv_to_rgb(hsv2)
    sobel_image = image_to_sobel(img_data.copy())
    # hist_plot = hist_converter(img_data.copy())

    plt.subplot(331)
    plt.imshow(img_data)
    plt.axis('off')
    plt.subplot(332)
    plt.imshow(hsv)
    plt.axis('off')
    plt.subplot(333)
    plt.imshow(hsv2)
    plt.axis('off')
    plt.subplot(334)
    plt.imshow(sobel_image)
    plt.axis('off')
    plt.subplot(335)
    plt.imshow(rgb2)
    plt.axis('off')
    plt.subplot(336)
    plt.imshow(rgb3)
    plt.axis('off')
    # plt.subplot(337)
    # plt.bar(hist_plot[0],hist_plot[1])
    # plt.axis('off')
    plt.show()


if __name__ == '__main__':
    main()

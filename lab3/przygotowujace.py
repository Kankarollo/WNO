from itertools import product
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from PIL import Image

image_name = 'anime.jpg'

"""PNG"""
img_data = img.imread(image_name)[:,:,:3]

"""JPG"""
# im_obj = Image.open(image_name)
# img_data = np.asarray(im_obj)

# Y = 0.2126R + 0.7152G + 0.0722B


def grayscale_converter(image):
    r, g, b = image[:, :, 0], image[:, :, 1], image[:, :, 2]
    converted_image = np.zeros(image.shape)
    converted_image[:, :, 0] = 0.2989 * r + 0.5870 * g + 0.1140 * b
    converted_image[:, :, 1] = 0.2989 * r + 0.5870 * g + 0.1140 * b
    converted_image[:, :, 2] = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return converted_image


def roberts_cross(image):
    roberts_image = np.zeros(image.shape)
    for i, j in product(range(image.shape[0] - 1), range(image.shape[1] - 1)):
        pixel_mask = image[i:i + 2, j:j + 2, 0]
        Gx = pixel_mask[0, 0] - pixel_mask[1, 1]
        Gy = pixel_mask[0, 1] - pixel_mask[1, 0]
        G = np.sqrt(Gx ** 2 + Gy ** 2)
        roberts_image[i, j, 0] = G
    roberts_image[:, :, 1] = roberts_image[:, :, 0]
    roberts_image[:, :, 2] = roberts_image[:, :, 0]
    return roberts_image


def extract_r_g_b(image, rgb_index):
    tmp = image[:, :, rgb_index].copy()
    image[:, :, :] = 0
    image[:, :, rgb_index] = tmp.copy()
    return image


def main():
    print("len ", len(img_data))
    print("shape: ", np.shape(img_data))
    print("type: ", type(img_data))

    red_data = extract_r_g_b(img_data.copy(), 0)
    green_data = extract_r_g_b(img_data.copy(), 1)
    blue_data = extract_r_g_b(img_data.copy(), 2)
    grey_image = grayscale_converter(img_data.copy())
    roberts_image = roberts_cross(grey_image)

    plt.subplot(241)
    plt.imshow(img_data, cmap='gray')
    plt.axis('off')
    plt.subplot(242)
    plt.imshow(red_data)
    plt.axis('off')
    plt.subplot(243)
    plt.imshow(green_data)
    plt.axis('off')
    plt.subplot(244)
    plt.imshow(blue_data)
    plt.axis('off')
    plt.subplot(245)
    plt.imshow(grey_image)
    plt.axis('off')

    plt.subplot(246)
    plt.imshow(roberts_image)
    plt.axis('off')
    plt.subplot(247)
    # plt.hist(grey_image[:, :, 0])
    plt.axis('off')

    # plt.subplot(247)
    # plt.hist(green_data[:, :, 1])
    # plt.subplot(248)
    # plt.hist(blue_data[:, :, 2])

    plt.show()


def test():
    testarrayX = np.array([[1, 0], [0, -1]])
    testarrayY = np.array([[1, 2], [-30, 0]])
    test = np.array([[2, 45, 5, 1, 6, 6, 1, 2, 3],
                     [2, 45, 5, 1, 6, 6, 1, 2, 3]])
    print(test[0, -3])


if __name__ == '__main__':
    main()
    # test()

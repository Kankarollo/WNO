import itertools

import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np

img_bez_krasnala = 'src_0.png'
img_z_krasnalem = 'src_1.png'
img1 = 'img1.png'
img2 = 'img2.png'
img3 = 'img3.png'
img4 = 'img4.png'
img5 = 'img5.png'

img_bez_krasnala_data = img.imread(img_bez_krasnala)[:, :, :3]
img_z_krasnalem_data = img.imread(img_z_krasnalem)[:, :, :3]


def find_dwarf(image_oryg, image_with):
    which_stays = (image_with - image_oryg) != 0
    which_stays = which_stays.astype(np.int)
    return image_with * which_stays


def border_points(image):
    cos = np.nonzero(image)
    gorny_punkt = cos[0].min()
    dolny_punkt = cos[0].max()
    lewy_punkt = cos[1].min()
    prawy_punkt = cos[1].max()
    return np.array([gorny_punkt, dolny_punkt, lewy_punkt, prawy_punkt])


def frame_dwarf(image, points):
    gorny_punkt = points[0]
    dolny_punkt = points[1]
    lewy_punkt = points[2]
    prawy_punkt = points[3]
    image[gorny_punkt:dolny_punkt, lewy_punkt - 3:lewy_punkt, :3] = np.array([255, 0, 0])
    image[gorny_punkt:dolny_punkt, prawy_punkt:prawy_punkt + 3, :3] = np.array([255, 0, 0])
    image[gorny_punkt - 3:gorny_punkt, lewy_punkt:prawy_punkt, :3] = np.array([255, 0, 0])
    image[dolny_punkt:dolny_punkt + 3, lewy_punkt:prawy_punkt, :3] = np.array([255, 0, 0])
    return image


def slice_dwarf(image, points):
    gorny_punkt = points[0]
    dolny_punkt = points[1]
    lewy_punkt = points[2]
    prawy_punkt = points[3]
    return image[gorny_punkt:dolny_punkt, lewy_punkt:prawy_punkt, :3]


def grayscale_converter(image):
    r, g, b = image[:, :, 0], image[:, :, 1], image[:, :, 2]
    converted_image = np.zeros(image.shape)
    converted_image[:, :, 0] = 0.2989 * r + 0.5870 * g + 0.1140 * b
    converted_image[:, :, 1] = 0.2989 * r + 0.5870 * g + 0.1140 * b
    converted_image[:, :, 2] = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return converted_image


def check_correctness(hist1, hist2):
    difference = hist1 - hist2
    sum = 0
    for element in difference:
        sum += abs(element)
    return sum


def wheres_waldo(dwarf, wallpaper):
    kontur = dwarf != 0

    correctness_table = np.array([])
    rows = np.array([])
    collumns = np.array([])
    hist_of_dwarf = np.histogram(dwarf, bins=100)[0]

    for i in range(0, wallpaper.shape[0] - 148, 5):
        for j in range(0, wallpaper.shape[1] - 106, 5):
            slice_of_wallpaper = wallpaper[i:i + 148, j:j + 106, :3]
            slice_of_wallpaper = slice_of_wallpaper * kontur
            hist_of_wallpaper = np.histogram(slice_of_wallpaper, bins=100)[0]
            correctness = check_correctness(hist_of_dwarf.copy(), hist_of_wallpaper.copy())
            correctness_table = np.append(correctness_table, correctness)
            rows = np.append(rows, i)
            collumns = np.append(collumns, j)

    min_index = correctness_table.argmin()
    print(rows[min_index], collumns[min_index])

    coordinates = np.array(
        [int(rows[min_index]), int(rows[min_index]) + 150, int(collumns[min_index]), int(collumns[min_index]) + 150])
    mam_cie = frame_dwarf(wallpaper.copy(), coordinates)

    return mam_cie

def main():
    dwarf = find_dwarf(img_bez_krasnala_data.copy(), img_z_krasnalem_data.copy())
    points = border_points(dwarf.copy())
    sliced_dwarf = slice_dwarf(dwarf, points)

    plansza_do_szukania = img.imread(img_z_krasnalem)[:, :, :3]
    znaleziony0 =wheres_waldo(sliced_dwarf, plansza_do_szukania)
    plansza_do_szukania = img.imread(img1)[:, :, :3]
    znaleziony1 =wheres_waldo(sliced_dwarf, plansza_do_szukania)
    plansza_do_szukania = img.imread(img2)[:, :, :3]
    znaleziony2 =wheres_waldo(sliced_dwarf, plansza_do_szukania)
    plansza_do_szukania = img.imread(img3)[:, :, :3]
    znaleziony3 =wheres_waldo(sliced_dwarf, plansza_do_szukania)
    plansza_do_szukania = img.imread(img4)[:, :, :3]
    znaleziony4 =wheres_waldo(sliced_dwarf, plansza_do_szukania)
    plansza_do_szukania = img.imread(img5)[:, :, :3]
    znaleziony5 =wheres_waldo(sliced_dwarf, plansza_do_szukania)
    plt.imshow(znaleziony0)
    plt.axis('off')
    plt.show()
    plt.imshow(znaleziony1)
    plt.axis('off')
    plt.show()
    plt.imshow(znaleziony2)
    plt.axis('off')
    plt.show()
    plt.imshow(znaleziony3)
    plt.axis('off')
    plt.show()
    plt.imshow(znaleziony4)
    plt.axis('off')
    plt.show()
    plt.imshow(znaleziony5)
    plt.axis('off')
    plt.show()



def test():
    pass


if __name__ == '__main__':
    main()
    # test()

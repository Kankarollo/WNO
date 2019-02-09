import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import itertools

img_name = 'dwarf.png'
testing_image = 'src_1.png'
img1 = 'img1.png'
img2 = 'img2.png'
img3 = 'img3.png'
img4 = 'img4.png'
img5 = 'img5.png'
dwarf = img.imread(img_name)[58:425,196:480,:3]
wallpaper = img.imread(testing_image)[:,:,:3]

def grayscale_converter(image):
    r, g, b = image[:, :, 0], image[:, :, 1], image[:, :, 2]
    converted_image = np.zeros(image.shape)
    converted_image[:, :, 0] = 0.2989 * r + 0.5870 * g + 0.1140 * b
    converted_image[:, :, 1] = 0.2989 * r + 0.5870 * g + 0.1140 * b
    converted_image[:, :, 2] = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return converted_image

def check_correctness(hist1,hist2):
    difference = hist1-hist2
    sum = 0
    for element in difference:
        sum += abs(element)
    return sum

def searching_for_dwarf(image,slice_of_dwarf):
    pass



def main():

    greyscale_dwarf = grayscale_converter(dwarf.copy())
    slice_of_dwarf = greyscale_dwarf[135:330,48:209,:3]
    #(195,161,3)

    greyscale_wallpaper = grayscale_converter(wallpaper.copy())

    correctness_table = np.array([])
    rows = np.array([])
    collumns = np.array([])
    hist_of_dwarf = np.histogram(slice_of_dwarf)[0]
#row: 600 column: 1665
    for i in range(0, greyscale_wallpaper.shape[0] - 195,100):
        for j in range(0, greyscale_wallpaper.shape[1] - 161,100):
            slice_of_wallpaper = greyscale_wallpaper[i:i+195,j:j+161,:3]
            hist_of_wallpaper = np.histogram(slice_of_wallpaper,100)[0]
            correctness=check_correctness(hist_of_dwarf.copy(), hist_of_wallpaper.copy())
            correctness_table = np.append(correctness_table,correctness)
            rows = np.append(rows,i)
            collumns = np.append(collumns,j)
    min_index = correctness_table.argmin()
    print(rows[min_index],collumns[min_index])

    plt.imshow(greyscale_wallpaper)
    plt.show()

def test():
    test_slice = wallpaper[540:]

if __name__ == '__main__':
    # test()
    main()
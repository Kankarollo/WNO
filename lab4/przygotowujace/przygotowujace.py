import matplotlib.pyplot as plt
import matplotlib.image as img
from PIL import Image
import numpy as np

path_to_img = 'db.jpg'
path_to_garden = 'xp_garden.jpg'

def red_frame(image,points):
    gorny_punkt = points[0]
    dolny_punkt = points[1]
    lewo_punkt = points[2]
    prawo_punkt = points[3]
    image[gorny_punkt:dolny_punkt,lewo_punkt-10:lewo_punkt,:] = np.array([255,0,0])
    image[gorny_punkt:dolny_punkt,prawo_punkt:prawo_punkt+10,:] = np.array([255,0,0])
    image[gorny_punkt-10:gorny_punkt,lewo_punkt:prawo_punkt,:] = np.array([255,0,0])
    image[dolny_punkt:dolny_punkt+10,lewo_punkt:prawo_punkt,:] = np.array([255,0,0])
    return image

def slicing_framed_picture(image,points):
    gorny_punkt = points[0]
    dolny_punkt = points[1]
    lewo_punkt = points[2]
    prawo_punkt = points[3]
    return image[gorny_punkt:dolny_punkt,lewo_punkt:prawo_punkt,:]

def leaveOnlyDb(image_oryg,image_db):
    which_stays = (image_oryg - image_db)!=0
    [1,0,1,0]
    which_stays = which_stays.astype(np.int)
    return image_db*which_stays

def search_for_coordinates(image):
    cos = np.nonzero(image)
    gorny_punkt = np.amin(cos[0])
    dolny_punkt = np.amax(cos[0])
    lewo_punkt = np.amin(cos[1])
    prawo_punkt = np.amax(cos[1])
    points = np.array([gorny_punkt,dolny_punkt,lewo_punkt,prawo_punkt])
    return points

def main():
    im = Image.open(path_to_img)
    imageDB_array = np.asarray(im)
    imageDB_array.setflags(write=1)
    im = Image.open(path_to_garden)
    imageGD_array = np.asarray(im)
    imageGD_array.setflags(write=1)
    im_bg = imageGD_array.copy()

    imageGD_array[500:785,900:1185,:3] = imageDB_array[:285,:285,:3]

    black_BG = leaveOnlyDb(im_bg,imageGD_array.copy())
    points = search_for_coordinates(black_BG.copy())
    final_img = red_frame(black_BG.copy(),points)
    thumbnail = slicing_framed_picture(black_BG.copy(),points)

    plt.imshow(im_bg)
    plt.axis('off')
    plt.show()
    plt.imshow(black_BG)
    plt.axis('off')
    plt.show()
    plt.imshow(final_img)
    plt.axis('off')
    plt.show()
    plt.imshow(thumbnail)
    plt.axis('off')
    plt.show()

def test():
    tablica = np.array([[1,2,3,4,5],[1,2]])
    tablica2 = np.array([[5,6,7,8,9,10,11,12,13,14],[1,2,3,4,5]])

    # tablica2[B] = tablica[B][tablica.shape]
    print(tablica2[tablica.shape[:]])
    x = np.arange(9.).reshape(3, 3)


    # tablica3[1,:] = tablica[2,:]
    # print(tablica3)

if __name__ == '__main__':
    main()
    # test()
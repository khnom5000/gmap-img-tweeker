from PIL import Image
import numpy as np
import cv2
from scipy import ndimage
from matplotlib import pyplot as plt



def find_clusters(array, water_tolerance):
    #Invert image array
    array = (255 - array)

    labelling, label_count = ndimage.label(array)

    water_areas = np.array(ndimage.sum(array, labelling, np.arange(labelling.max() + 1)))

    # Identify clusters greater than threshold
    for i, area in enumerate(water_areas):
        if area > water_tolerance:
            labelling[labelling == i] = 0

    # Convert labelled clusters back to binary mask
    labelling[labelling > 0] = 1

    return labelling



if __name__ == '__main__':

    # Dont quite know what this means but ~20000 best on the test google image...
    # 3000 worked on the simple test images
    water_tolerance = 20000

    im = cv2.imread('3e.png')[:,:,::-1]
    # im = cv2.imread('t3_2w_c_bw_o.png')[:,:,::-1]

    # Convert to Greyscale - Would probably need tweaking when full image is provided
    gray_image = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)



    # plt.imshow(gray_image)
    # plt.show()

    im_bw = np.full(gray_image.shape, 255)

    for i in range(205, 210):
        im_bw[gray_image == i] = 0

    # plt.imshow(im_bw)
    # plt.show()

    labelling = find_clusters(im_bw, water_tolerance)


    im[labelling>0]=(198,226,187)

    cv2.imwrite('pk_out1.png', im[:,:,::-1])

    #Cv2 seems to have some weird colour displaying issue...
    # plt.imshow(im)
    # plt.show()


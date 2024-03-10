from PIL import Image
import numpy as np
import cv2
from scipy import ndimage
from matplotlib import pyplot as plt



def find_clusters(array):
    #Invert image array
    array = (255 - array)

    labelling, label_count = ndimage.label(array)

    water_areas = np.array(ndimage.sum(array, labelling, np.arange(labelling.max() + 1)))

    # Identify clusters greater than threshold
    for i, area in enumerate(water_areas):
        if area > 3000:
            labelling[labelling == i] = 0

    # Convert labelled clusters back to binary mask
    labelling[labelling > 0] = 1

    return labelling



if __name__ == '__main__':

    im = cv2.imread('t3_2w_c_bw_o.png')[:,:,::-1]

    # Convert to Greyscale - Would probably need tweaking when full image is provided
    gray_image = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    (thresh, im_bw) = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)



    labelling = find_clusters(im_bw)


    im[labelling>0]=(198,226,187)

    cv2.imwrite('pk_out1.png', im)

    #Cv2 seems to have some weird colour displaying issue...
    plt.imshow(im)
    plt.show()


from PIL import Image
import numpy as np
import cv2
from scipy import ndimage
from matplotlib import pyplot as plt



# find unique clusters of identical RGB codes
def find_clusters(array):
    array = (255 - array)
    labelling, label_count = ndimage.label(array)



    sand_areas = np.array(ndimage.sum(array, labelling, np.arange(labelling.max() + 1)))

    mask = sand_areas > 3000

    remove_large_water = mask[labelling.ravel()].reshape(labelling.shape)

    plt.imshow(remove_large_water, interpolation='nearest')
    plt.show()



im = cv2.imread('t3_2w_c_bw_o.png', cv2.IMREAD_GRAYSCALE)

(thresh, im_bw) = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# cv2.imshow('image',im_bw)
# cv2.waitKey(0)

#change all color values in im to a single int (mask)
# im_with_ints = arr_to_int(im, mask_GBR_int)
#print('pic with mask values: \n', im_with_ints, '\n')

# due to replacing array of 3 values to a single int, new array has one dimension less

clusters, cluster_count = find_clusters(im_bw)
print(f'Found {cluster_count} clusters', '\n')

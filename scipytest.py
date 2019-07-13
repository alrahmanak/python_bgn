# path for image C:\Users\haame\DSND_Term1\projects/python_bgn
# Python script using Scipy 
# for image manipulation , 

# from scipy.misc import   
from scipy.misc.pilutil import imread, imsave, imresize
# from scipy.misc.pilutil import Image as img
# import Image

# Read a JPEG image into a numpy array 
img = imread('C:/Users/haame/DSND_Term1/projects/python_bgn/drgnfly.jpg') # path of the image 
print(img.dtype, img.shape) 

# Tinting the image 
img_tint = img * [1, 0.45, 0.3] 

# Saving the tinted image 
imsave('C:/Users/haame/DSND_Term1/projects/python_bgn/drgnfly_2.jpg', img_tint) 

# Resizing the tinted image to be 300 x 300 pixels 
img_tint_resize = imresize(img_tint, (300, 300)) 

# Saving the resized tinted image 
imsave('C:/Users/haame/DSND_Term1/projects/python_bgn/drgnfly_tinted_resized.jpg', img_tint_resize) 

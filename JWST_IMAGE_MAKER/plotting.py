import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os

def plot_data(processed_data,filename,save_image):
    """This module visualizes the processed data and saves it to the users computer if desired.

    Args:
        processed_data (np.array): A 2D or 3D numpy array of JWST that has been processed (not exactly sure how yet). The array will be 2D if the user gives a single .fits file and will be 3D otherwise.
        filename (list of strings): contains the names of the data files provided by the user
        save_image (T/F): Tells the code whether the user wants the figure to be saved to their computer
    """
    #Looping over all data files provided by the user (even if they only provide 1)
    for i in range(len(processed_data[0,0,:])): 
        img = processed_data[:,:,i]
        vmin,vmax=np.percentile(img.flatten(), [12,99])  #12 and 99 were determined by trial and error
        plt.figure(i,figsize=(5,5),dpi=175)
        plt.imshow(img, vmin=vmin, vmax=vmax, cmap='bone')
        #saving image if desired by user
        if save_image==True:
            name = os.path.splitext(filename[i])[0].lower()
            new_ext='.png'
            plt.savefig(name+new_ext,format='png',dpi=1200,bbox_inches='tight')
        plt.show()



    pass


# #Playing around with Pillow
# path='JWST_IMAGE_MAKER/Output Figures/'
# picturename='jw02739-o002_t001_miri_f1130w_i2d-1.png'

# #this snippet shows a .png that is already loaded into the directory
# image1=Image.open(path+picturename)
# image1.show()

# #This snippet will combine two png's
# image2=Image.open(path+'jw02739-o002_t001_miri_f1500w_i2d-1.png')

# print(image2.mode,image1.mode)

# intermediate= Image.alpha_composite(image1,image2)

# #intermediate.show()
   

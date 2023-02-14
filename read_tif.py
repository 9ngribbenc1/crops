# This script uses Python to read in .tif files I downloaded from 
# https://croplandcros.scinet.usda.gov/
#import tifffile and pillow to use this script


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from tifffile import imread, TiffFile, memmap
from PIL import Image


def main():


    directory = r"C:\Users\Neil\Documents\github\crops\Berks\rect\2022"
    os.chdir(directory)
    print("About to read in .tif file")
    image2022 = imread("clipped.tif")
    directory =  r"C:\Users\Neil\Documents\github\crops\Berks\rect\2021"
    
    os.chdir(directory)
    image2021 = imread("clipped.tif")
    tif = TiffFile("clipped.tif") # 1 page, series 1,
    print(len(tif.series[0].axes))

 
    change = image2022 - image2021
    data = Image.fromarray(change)
    data.save("change.png")

    '''
    numcorn22 = len(np.where(image2022 == 1)[0])
    numcorn21 = len(np.where(image2021 == 1)[0])
    print("num corn 22 ", numcorn22)
    print("num corn 21 ", numcorn21)
    numsoy22 = len(np.where(image2022 == 5)[0])
    numsoy21 = len(np.where(image2021 == 5)[0])
    print("num soy 22 ", numsoy22)
    print("num soy 21 ", numsoy21)
    print(image2021.shape)
    print(image2021.dtype)
    #print(change[560:601, 720:741])
    #df_image=pd.DataFrame(image)
    #print(df_image.describe())
    '''



if __name__ == "__main__":
    main()

import os
import cv2
# local library modules
from lib.crop import crop2KRustConsoleSeedImage, crop4kRustConsoleSeedImage;
from lib.ffc import setupFlatFieldCorrection, applyFlatFieldCorrection;

"""This is a processing script meant to be run directly.
This script takes one or many seed packet(s) and "germinates" it/them.
Every image for a [seed]/packet will be cropped, and flat-field corrected.
This will result in a /seedling folder, containing all processed images."""

print('\nYou are running the script (germinate.py) directly.')

# Load both vignetting template images for 2K and 4K respectively...
vig2k = setupFlatFieldCorrection('lib/vig/2k-value-desat.png')
vig4k = setupFlatFieldCorrection('lib/vig/4k-value-desat.png')

# Grab all directories (seeds) in /live, skip all files
cwd = os.getcwd(); print('Current Working Directory:\n    ', cwd,'\n')
seeds = os.listdir(f'{cwd}/live/'); print("Total Seeds:", len(seeds), '\n')
print("Total Seeds:", len(seeds))

# For every [cwd]/live/[seed]:
for seed in seeds:
    # Check if [cwd]/live/[seed]/packet exists...
    seedPath = f'{cwd}/live/{seed}/packet'; print(seedPath)
    if os.path.isdir(seedPath):
        pass
    else:
        print(f'{seed}/packet does not exist...')
    
    # Check if [cwd]/live/[seed]/packet/[images] exist...
    seedImages = os.listdir(seedPath)
    if not seedImages:
        print(f'{seed}/packet/[images] do not exist...')
        continue

    # Check if [cwd]/live/[seed]/seedling exists...
    seedTarget = f'{cwd}/live/{seed}/seedling'; print(seedTarget)
    if os.path.isdir(seedTarget):
        pass
    else:
        print(f'{seed}/seedling does not exist...')

    # For every [filename] in [cwd]/live/[seed]/packet:
    for count, imageName in enumerate(seedImages):
        cvImg = cv2.imread(f'{seedPath}/{imageName}')
        cvVig = None

        # Determine size of image, and crop accordingly...
        h, w, _ = cvImg.shape
        if (w == 1920) and (h == 1080):
            cvImg = crop2KRustConsoleSeedImage(cvImg)
            cvVig = vig2k
        elif (w == 3840) and (h == 2160):
            cvImg = crop4kRustConsoleSeedImage(cvImg)
            cvVig = vig4k

        # Perform FFC with correct vignetting template...
        cvImg = applyFlatFieldCorrection(cvImg, cvVig)

        # Save processed [i]-[width]x[height].png within /seedling...
        filename = f'({w} x {cvImg.shape[0]}) {seed} | {count}.png'
        path = f'{seedTarget}/{filename}'
        cv2.imwrite( path, cvImg )
        print(f'{path} saved.')

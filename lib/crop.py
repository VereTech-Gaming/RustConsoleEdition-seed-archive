def cropRustConsoleSeedImage(cvImg):
    """Handles uniform cropping of "patch" images for a Seed.
    It crops all non-UI content to reduce workload when Stitching."""

    # Decide crop based on image dimensions
    imgHeight, imgWidth, _ = cvImg.shape # reversed dims...
    topContentStart = 80 # just after top UI
    bottomContentEnd = 947 # just before bottom UI
    artifactingBuffer = 2 # artifacting minimum-buffer-zone; important

    # Set 2K standard here for possible use in 4K
    top = topContentStart + artifactingBuffer
    bottom = bottomContentEnd - artifactingBuffer
    
    # 2K Standard Resolution
    if (imgWidth == 1920) and (imgHeight == 1080):
        # Contentful Y-Range: (80, 947)
        # Artifact Buffer Zone: 2 pixels
        pass

    # 4K UHD Resolution
    elif (imgWidth, imgHeight) == [3840, 2160]:
        # Contentful Y-Range: (160, 1894)
        # Artifact Buffer Zone: 4 pixels
        top = top * 2; bottom = bottom * 2

    # Guard Clause
    else:
        print(f"Error: image dimensions {cvImg.shape} not supported.")
        exit()

    # Return the max contentful crop of the image to outer scope.
    return cvImg[top:bottom, 0:imgWidth] # contentful height, full width

def crop2KRustConsoleSeedImage(cvImg):
    return cvImg[82:945, 0:1920] # contentful height, full width

def crop4kRustConsoleSeedImage(cvImg):
    return cvImg[164:1890, 0:3840] # contentful height, full width

def prompt():
    # Enter image filename
    filename = input(
f"""\nYou are running the script (crop.py) directly.\n
Provide the filename of a 2K or 4K image to proceed.
(You may also enter nothing to exit this script.)\n
Image: {os.getcwd()}/"""
    )
    if filename == "": # empty
        exitPrompt()
    elif not os.path.isfile(filename):
        print(f"{os.getcwd()}/{filename} does not exist...")
        exitPrompt()

    # Perform the crop, and show the results
    croppedImage = cropRustConsoleSeedImage(cv2.imread(filename))
    #print("\nImage was cropped to:", croppedImage.shape)
    cv2.imshow("Cropped from: {filename}", croppedImage)
    cv2.waitKey(2500) # milliseconds; 0 = wait till key press
    cv2.destroyAllWindows()

    # Enter image savename
    savename = input(
f"""\nYou may enter nothing to skip saving the cropped image.
Otherwise, enter a filename to save the cropped image.\n
Crop: """
    )
    if savename == "": # empty
        exitPrompt()

    # Save the cropped image file
    cv2.imwrite(savename, croppedImage)



def exitPrompt():
    print("\n(crop.py) will now exit.")
    exit()



# If script is run, prompt for image filename w/ relative path
if __name__ == "__main__":
    import cv2
    import os
    prompt()
    exitPrompt()

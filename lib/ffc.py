import cv2
import numpy

def setupFlatFieldCorrection(filename):
    """The scientific name for removing vignetting is called Flat-Field Correction.
    Median + Gaussian produces the best image. Using .max() produces a brighter image than using mean.
    GIMP/value desaturate as a template removes more vignetting than GIMP/luminance desaturate.
    
    To create a Value Desaturated image in GIMP, open up your vignetting (raw, or cropped) image.
    Next, navigate through (Colors > Desaturate > Desaturate...), and select this option.
    Now, you may choose which type of desaturation to apply. Value (HSV) is recommended.

    When checking value-mean, value-max, luminance-mean, and luminance-max, value-max wins overall."""
    vig = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    vig = cv2.medianBlur(vig, 15)
    cvVigNorm = vig.astype(numpy.float32) / 255
    cvVigNorm = cv2.GaussianBlur(cvVigNorm, (51, 51), 30)
    cvVigMaxVal = cvVigNorm.max()
    cvInvNormVig = cvVigMaxVal / cvVigNorm # inverse vignetting normal
    return cv2.cvtColor(cvInvNormVig, cv2.COLOR_GRAY2BGR)

def applyFlatFieldCorrection(cvImg, cvInvNormVig):
    """Multiplies an inverse vignetting"""
    return cv2.multiply(cvImg, cvInvNormVig, dtype=cv2.CV_8U)



def prompt():
    # https://stackoverflow.com/questions/74786867/vignette-template-subtraction-from-image-in-opencv-python
    img1 = cv2.imread('test-crop.png')

    vig = cv2.imread('vig-desat-value.png', cv2.IMREAD_GRAYSCALE)  # Read vignette template as grayscale
    vig = cv2.medianBlur(vig, 15)  # Apply median filter for removing artifacts and extreem pixels.
    vig_norm = vig.astype(numpy.float32) / 255  # Convert vig to float32 in range [0, 1]
    vig_norm = cv2.GaussianBlur(vig_norm, (51, 51), 30)  # Blur the vignette template (because there are still artifacts, maybe because SO convered the image to JPEG).

    #vig_max_val = vig_norm.max()  # For avoiding "false colors" we may use the maximum instead of the mean.
    vig_mean_val = cv2.mean(vig_norm)[0]

    #inv_vig_norm = vig_max_val / vig_norm
    inv_vig_norm = vig_mean_val / vig_norm  # Compute G = m/F
    inv_vig_norm = cv2.cvtColor(inv_vig_norm, cv2.COLOR_GRAY2BGR)  # Convert inv_vig_norm to 3 channels before using cv2.multiply. https://stackoverflow.com/a/48338932/4926757
    img2 = cv2.multiply(img1, inv_vig_norm, dtype=cv2.CV_8U)  # Compute: C = R * G

    cv2.imshow('inv_vig_norm',  cv2.resize(inv_vig_norm / inv_vig_norm.max(), (500, 250)))  # Show inv_vig_norm for testing
    cv2.imshow('img1', cv2.resize(img1, (500, 250)))
    cv2.imshow('result', img2) #cv2.resize(img2, (1000, 500)))

    cv2.waitKey()
    cv2.destroyAllWindows()



def exitPrompt():
    print("\n(ffc.py) will now exit.")
    exit()



if __name__ == "__main__":
    import os
    prompt()
    exitPrompt()

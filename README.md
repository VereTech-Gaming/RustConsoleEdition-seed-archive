# This repository is for the automatic processing, manually assembly and long-term storage of Rust Console Server Map Seed Images.
Scripts are included for cropping images, for the removing of vignetting through Flat Field Correction, and for mass image processing based upon seed.

The tracking of new seeds is not within the scope of this repository. If you want/need to keep tabs on all current seeds, you may use the [Rust Laws Seed Scanner](https:rustlaws.com/seeds).

To get started with your own seed collection, continue reading...

# First, regardless of any seed, capture a vignetting template.
A single vignetting template can be used for all current seeds. The possibility of minor changes to the game's Map UI merits a Quality Assurance task of capturing a new vignetting template every time a new batch of seeds is added to the game.

Essentially, join any server, and open the Map UI. Scroll all the way to the top-left of the map, waaay out into the ocean. Zoom-in as far as you can. You should be able to see the vignetting present in the Map UI quite clearly now, as the ocean here is a single, uniform shade of blue. Now, hide your cursor by moving it behind the top banner (yes, you can do this).

Take a "gridless, legendless, cursorless" screenshot. This image will be cropped, and used for Flat Field Correction of every image for every seed you process. The last step is to "Value Desaturate" the vignetting template, but if you can't figure this part out, up-to-date 2k and 4k vignetting templates will be maintained and accessible in this repository. Check ```/lib/vig``` for the current 2k or 4k vignetting template.

WARNING: Screenshots are always the same resolution as the "monitor, television" you have connected to your console. 2K screens will produce (1920 x 1080) resolution images. 4k screens will produce (3840 x 2160) resolution images. For the best results, do not mix resolutions between your vignetting template and seed screenshots. This mixing of resolutions will result in unnecessary artifacts, that will ultimately reduce your ability to align the images while "stitching" them together later.

# Next, "image" the entire seed.
Recommendations: Use a 2K or 4K UHD screen with a Next-Gen Console. Capture and transfer seed images in batches, so as to keep image collections separated. Perform the capture process on wipe day using a Weekly Server to avoid unwanted vending machines. If you need help finding Weekly Servers using a given seed, use the [Rust Laws Seed Scanner](https://rustlaws.com/seeds).

You "image" the seed by taking screenshots of the entire area within the in-game grid. Every image taken should have a small overlap with it's adjacent images. You should hide the cursor, toggle off the legend, and remove the grid before capturing each screenshot. It is also recommended to "bind" your console's screenshot functionality to a button on your controller, to increase the speed at which you can take screenshots.

There is a uniform process to capturing each section of the seed. While zoomed all the way in, a given number of grid tiles will fit on screen, with a small margin on either side. It only takes 3 screenshots to capture the full width of the grid (regardless of map size), but 7 screenshots to capture the full height of the grid. This is because the Map UI limits the "Contentful Area" of each screenshot.

You should be aligning each capture section to sit "just inside" of your screen bounds, such as: "top-left of screen aligned with top-left grid corner A0", then "top-right of screen aligned with top-right grid corner T18", and lastly "align the top of screen with top of grid and capture the area inbetween both corners".

This process can be extremely tedious, as you can't move the cursor (which offers more fine-grained control of scrolling). You must move the map itself to align the current capture section, toggle off the grid, and capture a screenshot. It's easy to mistakenly to move the map just as you try to toggle the grid off... However, once you get the hang of this process, it becomes managable; especially if you know the correct capture zones.

--- Standardized Map-Section Capture Zones
All Bijective Hexavigesimal (Ex. A12, X9) guides below are considered "inclusive". They signify that all referenced markers should be included. For example, (A-G.7) means to include everything from the left-border of the A Tile, to .7 of the G Tile. Essentially, you combine the horizontal and vertical ranges to produce the least amount of images necessary to "image" the entire grid area of the seed. You don't have to capture both Oil Rigs, but if you do, mark the center with your cursor. We only want to capture the island and the shore/ocean contained within the named grid bounds.

---
For 3km seeds:
  Horizontal Capture Ranges:
    (A-to-H), (I-to-P), (O-to-X)
  Vertical Capture Ranges:
    (0-3.5), (3.5-5), (7-10.5), (10.5-13), (14-17.5), (17.5-20), (21-22)

  Total Captures required for imaging:
    3 * 7 = 28 patch captures + 3 guide images
  
  Grid Dimensions:
    Grid Tiles:
      Horizontal:
        (A-X) = 24 Tiles Wide
      Vertical:
        (0-22) = 23 Tiles Long
    Grid Meters:
      X-axis: (zero included)
        (-1500, 1572) = 3073m wide
      Y-axis: (zero included)
        (-1500, 1444) = 2944m long
  
  Maximum Dimensions:
    Full X-axis: (zero included)
      (-4500, 4500) = 9001m wide
    Full Y-axis: (zero included)
      (-4500, 4500) = 9001m long

For 2.5km seeds:
  Horizontal Capture Ranges:
    (A-G.7), (G.5-N.4), (N.2-T)
  Vertical Capture Ranges:
    (0-2), (3-5), (6-8), (9-11), (12-14), (15-17), (17-18)

  Total Captures required for imaging:
    3 * 7 = 28 patch captures + 3 guide images

  Grid Dimensions:
    Grid Tiles:
      Horizontal:
        (A-T) = 20 Tiles Wide
      Vertical:
        (0-18) = 19 Tiles Long
    Grid Meters:
      X-axis: (zero included)
        (-1500, 1310) = 2811m wide
      Y-axis: (zero included)
        (-1500, 1180) = 2681m long

  Maximum Dimensions:
    Full X-axis: (zero included)
      (-3750, 3750) = 7501m wide
    Full Y-axis: (zero included)
      (-3750, 3750) = 7501m long

For all map sizes:
  The coordinate (0, 0) is of non-zero width.
  You can stand within (0, 0), it's (1m x 1m) square.
  This means all fours quadrants are zero separated.
  Full axis measurements must include +1m to acount for (0,0).
---

Every seed (currently) requires exactly 28 screenshots to image. However, it is strongly advised that you take at least two more images with the grid toggled ON:
1. zoomed all the way in containing the grid's center intersection.
2. zoomed all the way out to fit as much of the full grid as possible.

These images, especially the one of grid center, will be used to "grid align" the final crop after "stitching" is complete. This is not necessary to get a beautiful end crop, but considering the amount you're already putting in, you may as well follow this final step of Quality Assurance. If you do follow this final step, your seed image will have a 1:1 correlation with the in-game grid.


# Once the seed is fully imaged, create a seed folder in ```/live```.
All the screenshots for a given seed should be stored within a ```/packet``` folder, within a ```/[seed]``` folder. For example, ```/live/5532/packet```. Each seed, regardless of Map Size should only require 28 screenshots to fully image. However, as noted above, it is good to capture two additional images to be used as guides when "stitching".

A quick note on outdated seeds... When a seed becomes deprecated/outdated, move it's folder to the ```/vault```. This makes it easier to distinguish between current ```/live``` seeds, and deprecated ```/vault``` seeds. You may delete it, as it now has no use, but keeping them is good record keeping.

You are now ready to process the seed.


# You may now run ```germinate.py``` to "prepare" your seed(s).
If you've created:
  1. a ```/lib/vig/[res].png``` Value-Desaturated vignetting template...
  2. a ```/live/[seed]/packet``` folder, or folders, of seed images...
...Then you're ready to begin processing your captured seed(s).

Upon running ```main.py```, you'll be given a prompt...
```Would you like to prepare all /live seeds, or just one?```

If you choose to process all images, the program will iterate through every ```/packet``` image for every seed folder stored within ```/live```. This process will NEVER result in lost data, as every processed image is saved in a ```/live/[seed]/seedling``` folder. The seed "packet" has been "germinated".

WARNING: This process will effectively double your storage requirements, but storage only becomes a concern when working with 4K captures. Choosing to process all ```/live``` seeds will take longer than just processing one.

If you choose to process just one seed, you'll be prompted to enter the seed in question (ex. ```5532```). This choice will result in the same changes detailed above, but only performed for the seed that was provided; if it's folder exists.

This ```germinate.py``` process in conducted for every image in a given ```/packet``` folder. First, it performs a ```Uniform Crop```, to remove any UI elements present in the raw screenshots. Then, ```Flat Field Correction``` will be used to remove any "residual vignetting" still present in the cropped image. This Flat Field Correction is what the Value-Desaturated Vignetting image is needed for. It is effectively "multiplied" into each image, to produce a "Flat Field", or in plain english, a "uniform shading" across all pixels. This "vignetting template subtraction" code was written by a contributor on stackoverflow.

# Finally, you may perform Image Stiching.
## A quick note...
This program does not currently support Automatic Image Stitching. The creation of a standardized algorithm was attempted, but it's "computationally prohibitive" as you must compare every pixel of every axis of an image against every other pixel of a similar axis in every other image. A rough draft was created, but would run for 20-40 minutes, and still wouldn't be aligned "perfectly". In other words, you will have to manually stitch the images together using an image editor. A human touch is surprisingly more efficient for this task, than a computer.

## Image Editor Setup
*The creator of this repository suggests using the opensource editor, GIMP.
Within your image editor, load all processed ```/patch``` images, preferably "As Layers". This will allow you to overlay the images atop one another, and rapidly toggle the images to visually ensure alignment.

Before starting, make sure to increase the Canvas size accordingly. For 2K captures, your canvas should be set to [5760 x 5760]. For 4K captures, your canvas should be set to [11520 x 11520]. *WARNING: 4K images will result in a MASSIVE memory load. A 2008 8GB RAM laptop could handle this, but felt feel clunky, and would take 20-30 minutes to save the fully stitched image. Unless you need the "absolute highest quality result", just capture in 2K. Comparing the end results showed little-to-no difference from 2K to 4K. If you have a "beefier" machine, this shouldn't be a problem.

## Manual Image Stitching
The simplest way to perform this process is to first move all the images into their correct relative position to one another, and THEN start stitching the images. ```Sort, then Stitch```. The stitching itself should be performed column-by-column, not row-by-row, and only two images should be merged together at a time for Quality Assurance.

The best way to align two images, is to place them directly next to each, and then zoom-in as-far-as-necessary to begin comparing pixels. Then, you may select one image with the Move Tool, so you can move it pixel-by-pixel with your keyboard's arrow keys. It's basically a game of repeating "move top-layer image, toggle top-layer visibility" until you've reached the Half Pixel Limit. More information on this limit below...

Once you've aligned two adjacent images of a column as perfectly as you can, you may now "Merge Layers" to combine these two images into one. Repeat this for the entire column of images. Only after you've completed all columns should you begin aligning and merging columns. Once you've merged all three columns, the monotonous part. Congratulations! You now have a beautiful, super resolution image of a Seed... but don't celebrate just yet. We must perform one last alignment, and a grid-aligned crop.

*A suggested precaution is to save your progress now, then proceed...

### The Grid-Aligned Crop
Do you remember imaging the seed's grid center? You must align the Center Grid Reference image with your beautiful, "gridless, stitched" image. Note: You should NOT have to scale either image, only move them. Once you have them both aligned as perfectly as possible, you can use a Grid Crop tool in your image editor to overlay a grid on the Canvas.

This Canvas Grid's Center is to be aligned with the center intersection of the map grid present in the Center Grid Reference image.

Once you have the Canvas Grid aligned with the grid center of the Canvas Grid Reference image, you must enter the amount of divisions (1:1 ratio of in-game grid tiles) for the Canvas Grid. Once you've entered the amount, you must set the width/height of a single tile, which will be applied to all Canvas Grid divisions.

This may take some "fine-tuning" to get just right, but it's well worth it.The goal here to create a 1:1 overlay in relation to the in-game grid. Note: You may have to utilize sub-pixel amounts (ex. 342.5, 245.3) to the grid just right. When you can't reduce the difference between the two grids any further, toggle the visibility of the Center Grid Reference image and perform the final crop of your "gridless, stiched" image. Note: you should be using Crop to Selection, not Crop to Content. You may also find that the ocean edges of your image have empty blocks, but you can always just copy &paste a sliver ocean into these alpha "voids".

Congratulations, you now have a "near-pixel-perfect, grid-aligned, super resolution" image of a single Seed Map! Now, repeat this entire process for every seed currently in-game... WARNING: Seeds are released in "batches" by Double Eleven upon key updates to the game. It is recommended to only perform this process for every seed directly AFTER a new update is released, as doing so just before an update would render all your hardwork meaningless.

# Additional Information
Here is some supplementary information to that provided above.

## The Half Pixel Limit
The images used to assemble seed images undergo mutliple transfers and changes before Stitching occurs. This results in miniscule changes to the images, and effects the overlap regions of adjacent images. This effectively means that you will (most likely) never produce a "Perfect Stitch" between two images, programmatically or manually, as the images do not truly share the same pixels. This was a huge problem pre-Power Surge Update, as all seed images were slightly darker, with much more contrast in their shading, resulting in a higher degree of artifacting produced by Flat Field Correction. As of the Power Surge Update, all seed images are "flat", meaning they have a uniform shading across every pixel. Vignetting is still present when viewing the Map, regardless of the state for viewport vignetting in User Settings, but this is remedied with Flat Field Correction.

## Flat Field Correction

# Importing necessary libraries
import cv2                      # For image processing and computer vision
import easygui                  # For file selection dialog box
import sys                      # For exiting the program if needed
import matplotlib.pyplot as plt  # For displaying images
import os                       # For file handling (not directly used here but useful)

# ---------------- Function to upload image ----------------
def upload():
    ImagePath = easygui.fileopenbox()  # Opens a dialog box for the user to select an image file
    cartoonify(ImagePath)              # Calls the cartoonify function with the selected image path

# ---------------- Function to cartoonify the image ----------------
def cartoonify(ImagePath):
    # Read the image from the given path
    originalmage = cv2.imread(ImagePath)                 # Loads the image using OpenCV
    originalmage = cv2.cvtColor(originalmage, cv2.COLOR_BGR2RGB)  # Converts BGR (OpenCV default) to RGB (for Matplotlib)

    # Check if image was loaded successfully
    if originalmage is None:                             # If image is not found or invalid
        print("Cannot find any image. Choose appropriate file.")  # Print error message
        sys.exit()                                       # Exit the program safely

    # Resize the original image to make it smaller and uniform
    ReSized1 = cv2.resize(originalmage, (960, 540))      # Resize to width=960, height=540

    # Convert the image to grayscale
    grayScaleImage = cv2.cvtColor(originalmage, cv2.COLOR_BGR2GRAY)  # Convert to gray (no color)
    ReSized2 = cv2.resize(grayScaleImage, (960, 540))    # Resize grayscale image

    # Apply median blur to smooth the grayscale image
    smoothGrayScale = cv2.medianBlur(grayScaleImage, 5)  # Reduces image noise and makes edges clearer
    ReSized3 = cv2.resize(smoothGrayScale, (960, 540))   # Resize the smoothed grayscale image

    # Detect edges using adaptive thresholding
    getEdge = cv2.adaptiveThreshold(smoothGrayScale, 255, # Maximum value for white
                                    cv2.ADAPTIVE_THRESH_MEAN_C, # Adaptive method for thresholding
                                    cv2.THRESH_BINARY,     # Converts to black and white
                                    9, 9)                  # Block size and constant value for thresholding
    ReSized4 = cv2.resize(getEdge, (960, 540))             # Resize edge image

    # Apply bilateral filter to remove noise while keeping edges sharp
    colorImage = cv2.bilateralFilter(originalmage, 9, 300, 300)  # Smooths color areas but keeps edges
    ReSized5 = cv2.resize(colorImage, (960, 540))                # Resize filtered color image

    # Combine the edges with the color image to create a cartoon effect
    cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=getEdge)  # Combines edges and colors
    ReSized6 = cv2.resize(cartoonImage, (960, 540))                       # Resize the cartoon image

    # List of images and titles for display
    images = [ReSized1, ReSized2, ReSized3, ReSized4, ReSized5, ReSized6] # Store all steps
    titles = ["Original", "Gray", "Smooth Gray", "Edges", "Filtered Color", "Cartoon"] # Titles for each image

    # Create a 3x2 grid for displaying all images
    fig, axes = plt.subplots(3, 2, figsize=(8, 8),           # 3 rows, 2 columns figure
                             subplot_kw={'xticks': [], 'yticks': []}, # Remove x/y axis ticks
                             gridspec_kw=dict(hspace=0.2, wspace=0.1)) # Set spacing between images

    # Display each image in its position on the grid
    for i, ax in enumerate(axes.flat):                       # Loop through all subplots
        ax.imshow(images[i], cmap='gray' if len(images[i].shape) == 2 else None)  # Use gray colormap if image is grayscale
        ax.set_title(titles[i])                              # Set title for each subplot
    plt.show()                                               # Show all images on screen

# ---------------- Run the program ----------------
upload()  # Starts the program by calling the upload function

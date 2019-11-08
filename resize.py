from PIL import Image
import glob
import pathlib
import argparse
import sys


# Save image as the next available integer
def saveImage(image):
    i = 0
    path = pathlib.Path(f"resized/{i}.png")
    while(path.exists()):
        i += 1
        path = pathlib.Path(f"resized/{i}.png")
    image.save(f"resized/{i}.png")


# Create a list of image paths on disk
def loadImages():
    # Glob is not case sensitive so this works for PNG, etc
    extensions = ['png', 'jpg', 'jpeg', 'gif', 'tiff', 'bmp']
    paths = list()

    # Get the file names of all known image types in input folder
    for extension in extensions:
        paths += glob.glob(f"input/*.{extension}")
    return(paths)


# Create an image of size width x height
# Add black bars to ensure correct ratio
def resize(imagePaths, width, height):
    # Load all paths as Image objects
    images = [Image.open(i) for i in imagePaths]
    for image in images:
        canvas = Image.new('RGBA', (width, height), "#000000")

        # Find the smallest multiplier so that neither axis is too large
        multiplier = min(height / image.height, width / image.width)
        image = image.resize((
            int(image.width * multiplier),
            int(image.height * multiplier)))

        # Find which axis matches the required dimensions
        if(image.width == width):
            canvas.paste(image, (0, int((height / 2) - (image.height / 2))))
        else:
            canvas.paste(image, (int((width / 2) - (image.width / 2)), 0))

        saveImage(canvas)


# Create folders just to make sure they exist
pathlib.Path('input').mkdir(parents=True, exist_ok=True)
pathlib.Path('resized').mkdir(parents=True, exist_ok=True)

# If there are arguments they are width x height
# Otherwise assume 1920x1080
if(len(sys.argv) > 1):
    parser = argparse.ArgumentParser(description='Image resizer')
    parser.add_argument('Width', metavar='Width', type=int)
    parser.add_argument('Height', metavar='Height', type=int)
    args = parser.parse_args()
    Width = args.Width
    Height = args.Width
else:
    Width = 1920
    Height = 1080

paths = loadImages()
resize(paths, Width, Height)

from PIL import Image
import glob


def loadImages():
    # Glob is not case sensitive so this works for PNG, etc
    extensions = ['png', 'jpg', 'jpeg', 'gif', 'tiff', 'bmp']
    paths = list()

    # Get the file names of all images
    for extension in extensions:
        paths += glob.glob(f"resized/*.{extension}")
        paths += glob.glob(f"stitchIn/*.{extension}")
    return(paths)


def stitchImages(imagePaths):
    images = [Image.open(i) for i in imagePaths]
    for i in range(len(images)):
        # Stitch the previous and current image together
        # Using previous because -1 is not out of bounds
        size = (images[i-1].width + images[i].width,
                max(images[i-1].height, images[i].height))
        stitchedImage = Image.new('RGBA', size)
        stitchedImage.paste(images[i-1])
        stitchedImage.paste(images[i], (images[i-1].width, 0))
        stitchedImage.save(f"stitched/{i}.png")


paths = loadImages()
stitchImages(paths)

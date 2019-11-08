'''
Stitches images together for use over dual monitors
'''

import glob
from PIL import Image


def load_images():
    '''
    Load images from reszied and stitchIn dirs
    '''

    # Glob is not case sensitive so this works for PNG, etc
    extensions = ['png', 'jpg', 'jpeg', 'gif', 'tiff', 'bmp']
    paths = list()

    # Get the file names of all images
    for extension in extensions:
        paths += glob.glob(f"resized/*.{extension}")
        paths += glob.glob(f"stitchIn/*.{extension}")
    return paths


def stitch_images(image_paths):
    '''Stitch and the images at paths in list'''

    images = [Image.open(i) for i in image_paths]
    for i, image in enumerate(images):
        # Stitch the previous and current image together
        # Using previous because -1 is not out of bounds
        size = (images[i-1].width + image.width,
                max(images[i-1].height, image.height))
        stitched_image = Image.new('RGBA', size)
        stitched_image.paste(images[i-1])
        stitched_image.paste(image, (images[i-1].width, 0))
        stitched_image.save(f"stitched/{i}.png")

def main():
    '''Entry point'''
    paths = load_images()
    stitch_images(paths)

main()

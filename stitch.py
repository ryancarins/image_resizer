'''
Stitches images together for use over dual monitors
'''

import glob
import argparse
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


def stitch_images(image_paths, image_type):
    '''Stitch and the images at paths in list'''
    if image_type == "png":
        mode = 'RGBA'
    else:
        mode = 'RGB'

    images = [Image.open(i) for i in image_paths]
    for i, image in enumerate(images):
        # Stitch the previous and current image together
        # Using previous because -1 is not out of bounds
        size = (image.width*2, image.height)
        stitched_image = Image.new(mode, size)
        stitched_image.paste(images[i-1])
        stitched_image.paste(image, (image.width, 0))
        stitched_image.save(f"stitched/{i}.{image_type}")


def main():
    '''Entry point'''

    parser = argparse.ArgumentParser(description='Image stitcher')
    parser.add_argument('-t', '--type', type=str, choices=["png", "jpg"],
                        default="jpg")

    args = parser.parse_args()
    paths = load_images()
    stitch_images(paths, args.type)

main()

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

    extensions = ['png', 'jpg', 'jpeg', 'gif', 'tiff', 'bmp',
                  'PNG', 'JPG', 'JPEG', 'GIF', 'TIFF', 'BMP']
    paths = list()

    # Get the file names of all images
    for extension in extensions:
        paths += glob.glob(f"resized/*.{extension}")
        paths += glob.glob(f"stitchIn/*.{extension}")
    return paths


def stitch_images(image_paths, image_type, number_monitors):
    '''Stitch and the images at paths in list'''
    if image_type == "png":
        mode = 'RGBA'
    else:
        mode = 'RGB'

    images = [Image.open(i) for i in image_paths]
    for i, image in enumerate(images):
        horizontal_position = 0 #The current horizonal position so we know where to paste
        size = (image.width*number_monitors, image.height)
        stitched_image = Image.new(mode, size)
        for j in range(number_monitors):
            stitched_image.paste(images[(i + j) % len(images)], (horizontal_position, 0))
            horizontal_position += image.width
        stitched_image.save(f"stitched/{i}.{image_type}")


def valid_number(value):
    '''Check that the number of monitors is valid for argparse'''
    number_monitors = int(value)
    if number_monitors < 2:
        raise argparse.ArgumentTypeError(
            f"{number_monitors} is invalid. 2 or more monitors required")
    return number_monitors

def main():
    '''Entry point'''

    parser = argparse.ArgumentParser(description='Image stitcher')
    parser.add_argument('-t', '--type', type=str, choices=["png", "jpg"],
                        default="jpg")
    parser.add_argument('-n', '--number_monitors', type=valid_number, default=2)

    args = parser.parse_args()
    paths = load_images()
    stitch_images(paths, args.type, args.number_monitors)

main()

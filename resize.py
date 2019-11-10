'''
Script to resize a directory of images with
bars on edges instead of stretching
'''

import glob
import pathlib
import argparse
from PIL import Image


def save_images(images, image_type):
    '''Save image as the next available integer'''

    for image in images:
        i = 0
        path = pathlib.Path(f"resized/{i}.{image_type}")
        while path.exists():
            i += 1
            path = pathlib.Path(f"resized/{i}.{image_type}")
        image.save(f"resized/{i}.{image_type}")


def load_images():
    ''' Create a list of image objects '''

    extensions = ['png', 'jpg', 'jpeg', 'gif', 'tiff', 'bmp',
                  'PNG', 'JPG', 'JPEG', 'GIF', 'TIFF', 'BMP']
    paths = list()

    # Get the file names of all known image types in input folder
    for extension in extensions:
        paths += glob.glob(f"input/*.{extension}")

    images = [Image.open(i) for i in paths]
    return images


def resize(images, width, height, image_type):
    '''
    Create and save image of size width x height
    Add black bars to ensure correct ratio
    '''

    # Load all paths as Image objects
    for i, image in enumerate(images):
        if image_type == "png":
            canvas = Image.new("RGBA", (width, height), "#000000")
        else:
            canvas = Image.new("RGB", (width, height), "#000000")

        # Find the smallest multiplier so that neither axis is too large
        multiplier = min(height / image.height, width / image.width)
        image = image.resize((
            int(image.width * multiplier),
            int(image.height * multiplier)))

        # Find which axis matches the required dimensions
        if image.width == width:
            canvas.paste(image, (0, int((height / 2) - (image.height / 2))))
        else:
            canvas.paste(image, (int((width / 2) - (image.width / 2)), 0))

        images[i] = canvas
    return images


def main():
    '''Entry point'''

    # Create folders just to make sure they exist
    pathlib.Path('input').mkdir(parents=True, exist_ok=True)
    pathlib.Path('resized').mkdir(parents=True, exist_ok=True)

    parser = argparse.ArgumentParser(description='Image resizer')
    parser.add_argument('-W', '--width', type=int, default=1920)
    parser.add_argument('-H', '--height', type=int, default=1080)
    parser.add_argument('-t', '--type', type=str, choices=["png", "jpg"],
                        default="jpg")

    args = parser.parse_args()
    images = load_images()
    resize(images, args.width, args.height, args.type)
    save_images(images, args.type)


main()

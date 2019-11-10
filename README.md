## Image Resizer

### Requirements

* Python 3.4 (Only tested on 3.7)
* pillow

### Command line flags

* -h Displays help
* -W --width WIDTH         Sets image width (Defaults to 1920)
* -H --height HEIGHT       Sets image height (Defaults to 1080)
* -t --type TYPE           Sets the image type (Currently defaults to jpg) png is slower but supports transparency

## Image Stitcher

### Requirements

* Python 3.4 (Only tested on 3.7)
* pillow
* The stitcher also requires all images to be the same resolution

### Command line flags

* -h					Displays help
* -n NUMBER_MONITORS	Sets the number of monitors

## Planned

Currently the resizer and the stitcher are separate
this may not change but I would like to add the ability
for the stitcher to resize images appropriately so the user
doesn't need to do two steps

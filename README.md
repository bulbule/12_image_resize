# Image Resizer

The script resizes an image in the indicated folder and saves it either to another desired directory with the same name or leaves it in the initial directory with a changed name. It uses the module [Pillow](https://pillow.readthedocs.io/en/latest/index.html) for manipulating images which can be installed by running:

```#!bash
$ pip install -r requirements.txt
```

# Usage
The script has one obligatory parameter – path to the file and several optional ones: `--width`, `--height`, `--scale` of the resized picture and `output`. 
 * If only `width` (`height`) is indicated the picture is resized in a way to preserve proportions. If both `width` and `height` are indicated the image is resized accordingly with a warning if proportions are changed.
 * If `scale` is given, no `width` or `height` can be defined and script raises an error.
 * If the path to the resized image is not indicated, it is saved in the original folder with a new name that shows its new dimensions. For instance, if there was a file `pic.jpg` with dimensions 100x200, after increasing the scale in twice the name will be transformed to `pic__200x400.jpg`.
 
 ## Example of usage
 ```#!bash
 $ python image_resize.py /Users/anyya/Downloads/grumpy_cat.jpg --scale 2 --output /Users/anyya/bot/thesis/grumpy_cat.jpg
 ```
 
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

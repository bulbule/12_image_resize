from PIL import Image
import os
import argparse
import math


def load_image(filepath):
    if not os.path.exists(filepath):
        raise IOError('Cannot open the image')
    else:
        return Image.open(filepath)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--width', type=int)
    parser.add_argument('--height', type=int)
    parser.add_argument('--scale', type=float)
    parser.add_argument('input', help='path to origin')
    parser.add_argument('--output', help='path to result')
    args = parser.parse_args()
    if (args.scale and (args.width or args.height)) is not None:
        raise ValueError(
            'Please indicate either only scale or width and(or) height')
    else:
        return args


def get_resize_params(image, args):
    original_width, original_height = image.size
    original_scale = original_width / original_height
    if args.scale is None:
        if (args.width and args.height) is not None:
            return {'width': args.width,
                    'height': args.height
                    }
        elif args.height is None:
            return {'width': args.width,
                    'height': args.width / original_scale
                    }
        elif args.width is None:
            return {'width': args.height * original_scale,
                    'height': args.height
                    }
    else:
        return {'width': args.scale * original_width,
                'height': args.scale * original_height
                }


def resize_image(image, resize_params):
    return image.resize(
        (int(
            resize_params['width']), int(
            resize_params['height'])))


def get_renamed_image_path(resized_image, args):
    image_name, image_ext = os.path.splitext(os.path.basename(args.input))
    new_width, new_height = resized_image.size
    image_new_name = '{}__{}x{}{}'.format(
        image_name, new_width, new_height, image_ext)
    renamed_image_path = '{}/{}'.format(os.path.dirname(args.input),
                                        image_new_name)
    return renamed_image_path


def save_resized_image(resized_image, args):
    if args.output is not None:
        resized_image.save(args.output)
    else:
        renamed_image_path = get_renamed_image_path(resized_image, args)
        resized_image.save(renamed_image_path)
        

def check_proportions(resize_params, image):
    original_scale = image.size[0] / image.size[1]
    new_scale = resize_params['width'] / resize_params['height']
    if not math.isclose(original_scale, new_scale, rel_tol=1e-2):
        print('Warning: original proportions will not be preserved.')

if __name__ == '__main__':
    args = get_args()
    image = load_image(args.input)
    resize_params = get_resize_params(image, args)
    check_proportions(resize_params, image)    
    resized_image = resize_image(image, resize_params)
    image.close()
    save_resized_image(resized_image, args)

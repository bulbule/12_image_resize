from PIL import Image
import os
import argparse


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
            if args.width / args.height != original_scale:
                print('Warning: original proportions will not be preserved.')
            return {'width': args.width,
                    'height': args.height
                    }
        elif args.height is None:
            return {'width': args.width,
                    'height': args.width / original_scale
                    }
        elif args.width is None:
            return {'width': args.height * original_scale,
                    'height': args.width / original_scale
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


def save_resized_image(resized_image, args):

    image_name, image_ext = os.path.splitext(os.path.basename(args.input))
    new_width, new_height = resized_image.size
    if args.output is not None:
        resized_image.save(args.output)
    else:
        image_new_name = '{}__{}x{}{}'.format(
            image_name, new_width, new_height, image_ext)
        image_new_name_path = '{}/{}'.format(os.path.dirname(args.input),
                                             image_new_name)
        resized_image.save(image_new_name_path)


if __name__ == '__main__':

    args = get_args()
    image = load_image(args.input)
    resize_params = get_resize_params(image, args)
    resized_image = resize_image(image, resize_params)
    save_resized_image(resized_image, args)
    image.close()

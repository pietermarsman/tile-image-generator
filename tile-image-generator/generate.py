from math import ceil
from random import random, uniform

from PIL import Image, ImageColor

from colors import rgb_from_hsv


def generate_tile_image(size, method='hierarchical', depth=7):
    """Generate tiled images with various methods

    :param size: (height, width) of image in pixels
    :param method: method for generating images. Currently only supports "hierarchical".
    :param depth: maximum recursion depth for hierarchical method.
    :return: PIL image
    """

    if method is 'hierarchical':
        return generate_hierarchical_tile_image(size, depth)
    else:
        raise AttributeError('Method {!r} is unknown. Should be {!r}.'.format(method, 'hierarchical'))


def generate_hierarchical_tile_image(size, depth, min_hue, max_hue, min_saturation, max_saturation, min_value,
                                     max_value):
    if depth <= 0:
        hue = uniform(min_hue, max_hue)
        saturation = uniform(min_saturation, max_saturation)
        value = uniform(min_value, max_value)
        rgb = rgb_from_hsv(hue, saturation, value)
        return Image.new('RGB', size, rgb)
    else:
        image = Image.new('RGB', size, 'white')

        hue_step = (max_hue - min_hue) / 4
        child_size = (ceil(size[0] / 2), ceil(size[1] / 2))
        child_hues = [(min_hue + hue_step * i, min_hue + hue_step * (i + 1)) for i in range(4)]
        child_position = [(0, 0), (size[0] // 2, 0), (0, size[1] // 2), (size[0] // 2, size[1] // 2)]
        for child_hue, child_position in zip(child_hues, child_position):
            child_image = generate_hierarchical_tile_image(child_size, depth - 1, child_hue[0], child_hue[1],
                                                           min_saturation, max_saturation, min_value, max_value)
            image.paste(child_image, child_position)
        return image

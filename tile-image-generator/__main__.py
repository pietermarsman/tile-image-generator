import argparse

from generate import generate_tile_image, generate_hierarchical_tile_image

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate various tiled images')
    methods = parser.add_subparsers(help='Different methods for generating tiled images', dest='method')

    parser.add_argument('width', type=int, default=1920, help='Width of the generated image')
    parser.add_argument('height', type=int, default=1080, help='Height of the generated image')
    parser.add_argument('--min-hue', type=float, default=0.0, help='Minimum hue')
    parser.add_argument('--max-hue', type=float, default=1.0, help='Maximum hue')
    parser.add_argument('--min-saturation', type=float, default=0.0, help='Minimum saturation')
    parser.add_argument('--max-saturation', type=float, default=1.0, help='Maximum saturation')
    parser.add_argument('--min-value', type=float, default=0.0, help='Minimum value (lightness)')
    parser.add_argument('--max-value', type=float, default=1.0, help='Maximum value (lightness)')

    hierarchy_parser = methods.add_parser('hierarchical')
    hierarchy_parser.add_argument('--depth', type=int, default=3, help='Maximum depth of hierarchy')

    args = parser.parse_args()
    size = (args.width, args.height)
    if args.method == 'hierarchical':
        image = generate_hierarchical_tile_image(size, args.depth, args.min_hue, args.max_hue, args.min_saturation,
                                                 args.max_saturation, args.min_value, args.max_value)
    else:
        raise AttributeError('Method {!r} is unknown.'.format(args.method))
    image.show()
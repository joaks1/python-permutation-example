#! /usr/bin/env python3

"A script for randomly permuting input strings."

import sys
import random
import argparse


def arg_is_positive_int(i):
    try:
        if int(i) < 1:
            raise
    except:
        msg = '{0!r} is not a positive integer'.format(i)
        raise argparse.ArgumentTypeError(msg)
    return int(i)

def main_cli():
    import argparse

    # Create a command-line parser object
    parser = argparse.ArgumentParser(
            formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    # Tell the parser what command-line arguments this script can receive
    parser.add_argument('elements',
            metavar = 'ELEMENT',
            nargs = '+', # one or more arguments
            type = str,
            help = ('One element to include in the permutation.'))
    parser.add_argument('--seed',
            action = 'store',
            type = arg_is_positive_int,
            help = ('A positive integer for seeding the random number '
                    'generator.'))

    args = parser.parse_args()

    # Create an instance of a random number generator
    random_number_generator = random.Random()
    if not args.seed:
        # The user did not provide a seed for the random number generator, so
        # we will pick one.
        # We'll pick a random integer between 1 and a very large number
        args.seed = random.randint(1, 999999999)
    # Seed the random number generator
    random_number_generator.seed(args.seed)

    # Let's output the seed that was used, so the results can be replicated
    # later
    sys.stdout.write("Random number seed: {0}\n".format(args.seed))

    # Randomly shuffle the elements provided by the user
    # The shuffle method modifies the input list, and so returns `None`.
    random_number_generator.shuffle(args.elements)

    # Loop over the shuffled elements and write them to stdout
    for el in args.elements:
        sys.stdout.write("{0}\n".format(el))


if __name__ == '__main__':
    main_cli()

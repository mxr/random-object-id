import binascii
import os
import sys
import time
import json

from argparse import ArgumentParser


def gen_random_object_id():
    timestamp = '{0:x}'.format(int(time.time()))
    rest = binascii.b2a_hex(os.urandom(8)).decode('ascii')
    return timestamp + rest


def parse_args(args):
    parser = ArgumentParser(description='Generate a random MongoDB ObjectId')
    parser.add_argument('-l', '--longform',
                        action="store_true",
                        dest="long_form",
                        help='prints the ID surrounded by ObjectId("...")')
    parser.add_argument('-j', '--json',
                        action="store_true",
                        dest="json",
                        help='prints the IDs as a json list')
    parser.add_argument('-n', '--count',
                        type=int,
                        dest="count",
                        default=1,
                        help='prints a certain amount of ids')

    return parser.parse_args(args)


def main():
    args = parse_args(sys.argv[1:])

    if args.count < 1:
        print("Count cannot be < 1. Your input: {}".format(args.count))
        return

    object_ids = [gen_random_object_id() for _ in range(args.count)]

    if args.long_form:
        object_ids = ['ObjectId("{}")'.format(object_id) for object_id in object_ids]

    if args.json:
        print(json.dumps(object_ids, indent="    "))
    else:
        [print(object_id) for object_id in object_ids]


import binascii
import os
import time

from argparse import ArgumentParser


def gen_random_object_id():
    timestamp = '{0:x}'.format(int(time.time()))
    rest = binascii.b2a_hex(os.urandom(8)).decode('ascii')
    return timestamp + rest

if __name__ == '__main__':
    parser = ArgumentParser(description='Generate a random MongoDB ObjectId')
    parser.add_argument('-l', '--longform',
                        action="store_true",
                        dest="long_form",
                        help="prints the ID surrounded by ObjectId(...)")

    args = parser.parse_args()

    object_id = gen_random_object_id()

    if args.long_form:
        print('ObjectId("{}")'.format(object_id))
    else:
        print(object_id)

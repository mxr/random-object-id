from __future__ import annotations

import binascii
import os
import time
from argparse import ArgumentParser
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence


def generate() -> str:
    timestamp = int(time.time())
    rest = binascii.b2a_hex(os.urandom(8)).decode("ascii")
    return f"{timestamp:x}{rest}"


def main(argv: Sequence[str] | None = None) -> int:
    parser = ArgumentParser(description="Generate a random MongoDB ObjectId")
    parser.add_argument(
        "-l",
        "--longform",
        action="store_true",
        dest="long_form",
        help='prints the ID surrounded by ObjectId("...")',
    )

    args = parser.parse_args(argv)

    object_id = generate()

    if args.long_form:
        print(f'ObjectId("{object_id}")')
    else:
        print(object_id)

    return 0


if __name__ == "__main__":
    exit(main())

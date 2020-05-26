import re

import pytest

from random_object_id import generate
from random_object_id import main


def test_generate(mocker):
    mocker.patch("time.time", return_value=1429506585.786924)

    object_id = generate()

    assert object_id.startswith("55348a19")
    assert re.match("^[0-9a-f]{24}$", generate())


@pytest.mark.parametrize(
    ("args", "expected"),
    (
        pytest.param((), "^[0-9a-f]{24}\n$", id="default"),
        pytest.param(("-l",), r'^ObjectId\("[0-9a-f]{24}"\)\n$', id="long form"),
    ),
)
def test_main(capsys, args, expected):
    assert not main(args)

    out, _ = capsys.readouterr()
    assert re.match(expected, out), out

import re

import mock

from random_object_id.random_object_id import gen_random_object_id


def test_gen_random_object_id_time():
    with mock.patch('time.time') as mock_time:
        mock_time.return_value = 1429506585.786924
        object_id = gen_random_object_id()

    assert re.match('55348a19', object_id)


def test_gen_random_object_id_length():
    assert len(gen_random_object_id()) == 24

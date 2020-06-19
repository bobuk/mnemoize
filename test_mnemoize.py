import mnemoize
import random
import pytest
import uuid


@pytest.mark.parametrize(
    "vint",
    [
        2999,
        991,
        1,
        random.randint(0, 2 ** 128),
        random.randint(0, 2 ** 201),
        123489012341092348,
        uuid.uuid4().int,
    ],
)
def test_with(vint):
    t = mnemoize.pack(vint, "russian")
    newint = mnemoize.unpack(t, "russian")
    assert vint == newint

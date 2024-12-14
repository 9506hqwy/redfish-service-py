from example.func import (
    add,
    sub,
)


def test_add() -> None:
    assert add(2, 1) == 3


def test_sub() -> None:
    assert sub(2, 1) == 1

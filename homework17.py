import pytest

from shop import discount


def test_d_10_p():
    assert discount(100, 10) == 90

def test_d_10_p():
    assert discount(100, 0) == 100

def test_d_over_hp():
    with pytest.raises(ValueError):
        discount(100, 150)
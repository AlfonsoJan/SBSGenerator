import pytest
import sbsgenerator


def test_sum_as_string():
    assert sbsgenerator.sum_as_string(1, 1) == "2"

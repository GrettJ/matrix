from main import process_matrix
import pytest


def test_process_matrix():
    assert process_matrix([1,2,3]) == [1.5, 2, 2.5]
    assert process_matrix(["a", 1, None]) == ValueError

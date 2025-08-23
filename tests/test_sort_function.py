import pytest

from sort_function import sort


def test_sort_function():
    assert sort(1, 2, 3, 4) == 'standard'
    assert sort(1000, 1000, 1000, 5) == 'special'  # bulky because of volume

    default_args = [1, 1, 1]

    # Bulky because of a dimension
    for i in range(3):
        args = default_args.copy()
        args[i] = 150
        assert sort(*args, 5) == 'special'

    assert sort(1, 1, 1, 20) == 'special'  # heavy

    assert sort(150, 1, 1, 20) == 'rejected'  # both bulky and heavy


def test_sort_function_incorrect_inputs():
    default_args = [1, 1, 1, 1]
    for i in range(4):
        args = default_args.copy()
        args[i] = "invalid"
        with pytest.raises(ValueError, match="All values must be numeric"):
            sort(*args)
        args[i] = 0
        with pytest.raises(ValueError, match="All values must be greater than 0"):
            sort(*args)

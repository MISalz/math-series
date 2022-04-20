from math_series.series import series, fibonacci


def test_math_series_one():
    # what happened
    actual = series(1)
    # what did you expect to happen
    expected = '1'
    # does what happened match what you expected
    assert actual == expected


def test_fibonacci():
    # what happened
    actual = fibonacci(n)
    # what did you expect to happen
    expected = '1'
    # does what happened match what you expected
    assert actual == expected


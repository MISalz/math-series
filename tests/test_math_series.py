from math_series.series import series, fibonacci, lucas, sum_series


def test_math_series_one():
    # what happened
    actual = series(1)
    # what did you expect to happen
    expected = '1'
    # does what happened match what you expected
    assert actual == expected


def test_fibonacci():
    # what happened
    actual = fibonacci(5)
    # what did you expect to happen
    expected = '20'
    # does what happened match what you expected
    assert actual == expected


def test_lucas():
    # what happened
    actual = lucas(4)
    # what did you expect to happen
    expected = '7'
    # does what happened match what you expected
    assert actual == expected

def test_sum_series():
    # what happened
    actual = sum_series(7)
    # what did you expect to happen
    expected = '7'
    # does what happened match what you expected
    assert actual == expected


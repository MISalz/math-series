from math_series.series import series


def test_math_series_one():
    # what happened
    actual = series(1)
    # what did you expect to happen
    expected = '1'
    # does what happened match what you expected
    assert actual == expected

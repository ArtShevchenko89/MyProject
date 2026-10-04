import pytest

from myproject import average, letter_grade, median, passed, summary


def test_average():
    assert average([60, 80, 100]) == 80


def test_median_odd():
    assert median([90, 60, 75]) == 75


def test_median_even():
    assert median([60, 70, 80, 90]) == 75


@pytest.mark.parametrize(
    "score, letter",
    [(95, "A"), (85, "B"), (75, "C"), (65, "D"), (60, "E"), (40, "FX"), (20, "F")],
)
def test_letter_grade(score, letter):
    assert letter_grade(score) == letter


def test_passed():
    assert passed(60)
    assert not passed(59)


def test_summary():
    result = summary([72, 85, 90, 64, 58, 95])
    assert result == {"count": 6, "average": 77.33, "median": 78.5, "passed": 5}


def test_empty_list_raises():
    with pytest.raises(ValueError):
        average([])


def test_out_of_range_raises():
    with pytest.raises(ValueError):
        median([50, 120])

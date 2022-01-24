import pytest

from typing import Iterable
from titanic import Titanic


@pytest.fixture
def test_titanic() -> Titanic:
    return Titanic("./titanic.csv")


def test_number_of_passengers(test_titanic: Titanic):
    # According to the CSV, there were 891 passengers aboard.
    assert test_titanic.number_of_passengers() == 891


def test_total_fare_paid(test_titanic: Titanic):
    # The sum of the fares paid by all passengers. The input data has at most
    # four decimal places. If you had to round your answer, where did the extra
    # places come from?
    assert test_titanic.total_fare_paid() == 28693.9493


def test_median_fare(test_titanic: Titanic):
    # The median of the fares paid by all passengers
    assert test_titanic.median_fare() == 14.4542


def test_cherbourg_survival_rate(test_titanic: Titanic):
    # Passengers boarded at three different ports before the Atlantic crossing
    # began. Those who boarded at Cherbourg had the best chance of survival at
    # ~55%.
    assert test_titanic.cherbourg_survival_rate() == (93 / 168)


def test_passenger_class_by_survival(test_titanic: Titanic):
    # The three passenger classes had very different survival rates; the more
    # you paid, the better your chances.
    actual = test_titanic.passenger_class_by_survival()
    expected = [1, 2, 3]
    assert isinstance(actual, Iterable)
    assert list(actual) == expected

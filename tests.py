import pytest
from ActiveUserDates import ActiveUserDates
from FetchData import FetchData
from main import generate_graph


@pytest.fixture
def data():
    return {
        "01-01-2022": 300,
        "02-01-2022": 500,
        "03-01-2022": 700,
        "04-01-2022": 1300,
        "05-01-2022": 2000,
        "06-01-2022": 3000,
        "07-01-2022": 3500,
        "08-01-2022": 4000,
        "09-01-2022": 4500,
        "10-01-2022": 5000,
        "11-01-2022": 20000,
        "12-01-2022": 35000,
        "13-01-2022": 46000,
        "14-01-2022": 70000,
        "15-01-2022": 90000,
    }


@pytest.fixture
def bad_data():
    return {}


@pytest.fixture
def cmd_input():
    return ["", "01-01-2022", "09-01-2022"]


@pytest.fixture
def cmd_input_invalid_date_type():
    return ["", "01-01-2022", 2]


@pytest.fixture
def cmd_input_invalid_date():
    return ["", "01-01-2022", "01-2022"]


@pytest.fixture
def cmd_input_out_of_range_date():
    return ["", "21-01-2022", "02-02-2022"]


def test_graph_display(data, cmd_input):
    active_user_dates = ActiveUserDates(data, cmd_input)
    user_data = active_user_dates.get_data_for_date_ranges()
    assert isinstance(user_data[0], list)
    assert isinstance(user_data[1], list)
    assert len(user_data[0]) == len(user_data[1])
    assert generate_graph(user_data) is None


def test_bad_data(bad_data, cmd_input):
    active_user_dates = ActiveUserDates(bad_data, cmd_input)
    user_data = active_user_dates.get_data_for_date_ranges()
    assert user_data[0] is False
    assert user_data[1] == "No data for date range selected"


def test_out_of_range_date(data, cmd_input_out_of_range_date):
    active_user_dates = ActiveUserDates(data, cmd_input_out_of_range_date)
    user_data = active_user_dates.get_data_for_date_ranges()
    assert user_data[0] is False
    assert user_data[1] == "No data for date range selected"


def test_invalid_date_type(data, cmd_input_invalid_date_type):
    active_user_dates = ActiveUserDates(data, cmd_input_invalid_date_type)
    user_data = active_user_dates.get_data_for_date_ranges()
    assert user_data[0] is False
    assert user_data[1] == "Date should be a string"


def test_bad_date(data, cmd_input_invalid_date):
    active_user_dates = ActiveUserDates(data, cmd_input_invalid_date)
    user_data = active_user_dates.get_data_for_date_ranges()
    assert user_data[0] is False
    assert (
        user_data[1]
        == "This is the incorrect date string format. It should be DD-MM-YYY"
    )


def test_data_retrieval():
    assert isinstance(FetchData.get_user_and_date_data(), dict)

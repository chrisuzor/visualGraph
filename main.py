import plotext as plt
import sys
from FetchData import FetchData
from ActiveUserDates import ActiveUserDates


def generate_graph(active_user_dates):
    plt.bar(active_user_dates[0], active_user_dates[1])
    plt.title("Active Users vs Dates")
    plt.show()


if __name__ == "__main__":
    data = FetchData.get_user_and_date_data()
    active_user_dates = ActiveUserDates(data, sys.argv)
    user_data = active_user_dates.get_data_for_date_ranges()
    if user_data[0]:
        generate_graph(user_data)
    else:
        raise RuntimeError(user_data[1])

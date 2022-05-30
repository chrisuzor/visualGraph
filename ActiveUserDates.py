from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ActiveUserDates:
    data: dict
    sys_args: list
    date_format: str = field(init=False)

    def __post_init__(self) -> None:
        self.date_format = "%d-%m-%Y"

    def get_data_for_date_ranges(self) -> list:
        try:
            dates = []
            counts = []
            for key, value in self.data.items():
                if (
                    datetime.strptime(self.sys_args[1], self.date_format)
                    <= datetime.strptime(key, self.date_format)
                    <= datetime.strptime(self.sys_args[2], self.date_format)
                ):
                    dates.append(key)
                    counts.append(value)

            return (
                [dates, counts] if dates else [False, "No data for date range selected"]
            )
        except IndexError:
            return [False, "You're required to input a start date and end date"]
        except ValueError:
            return [
                False,
                "This is the incorrect date string format. It should be DD-MM-YYY",
            ]
        except TypeError:
            return [False, "Date should be a string"]

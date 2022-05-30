import requests


class FetchData:
    @staticmethod
    def get_user_and_date_data():
        try:
            response = requests.get(
                "http://sam-user-activity.eu-west-1.elasticbeanstalk.com/", timeout=5
            )
            if response.status_code == 200:
                return response.json()
            return False
        except (requests.ConnectionError, requests.Timeout) as exception:
            raise requests.ConnectionError("No internet connection.")

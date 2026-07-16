from datetime import datetime


class Helper:

    @staticmethod
    def get_current_date():

        return datetime.now().strftime("%Y-%m-%d")


    @staticmethod
    def get_current_time():

        return datetime.now().strftime("%H:%M:%S")


    @staticmethod
    def get_current_datetime():

        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    @staticmethod
    def print_line():

        print("-" * 50)


    @staticmethod
    def print_title(title):

        print("\n" + "=" * 50)
        print(title.upper())
        print("=" * 50)
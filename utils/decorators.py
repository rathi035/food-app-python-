from functools import wraps
from utils.logs import Logger


def log_execution(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        Logger.info(f"Executing {func.__name__}")

        try:

            result = func(*args, **kwargs)

            Logger.info(f"{func.__name__} Executed Successfully")

            return result

        except Exception as e:

            Logger.error(f"{func.__name__} Failed : {e}")

            raise

    return wrapper
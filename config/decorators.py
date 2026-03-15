from functools import wraps
import time
from config.logger import logger

def log_execution(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        name = func.__qualname__
        logger.info(f"Starting {name}")

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        logger.info(f"Finished {name} in {end-start:.2f}s")

        return result

    return wrapper
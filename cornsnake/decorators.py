from . import util_time


def timer(original_function):
    def wrapper(*args, **kwargs):
        start = util_time.start_timer()

        # Call the original function
        result = original_function(*args, **kwargs)

        elapsed = util_time.end_timer(start)
        print(f"[time taken: {util_time.describe_elapsed_seconds(elapsed)}]")

        return result

    return wrapper

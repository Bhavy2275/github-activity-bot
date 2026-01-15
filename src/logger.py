# logger.py module


def retry_operation(func, retries=3):
    """Decorator to retry a function multiple times on failure."""
    def wrapper(*args, **kwargs):
        for i in range(retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Retry {i+1} failed: {e}")
    return wrapper


def format_timestamp(ts: float, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Formats a timestamp into a human-readable string."""
    from datetime import datetime
    return datetime.fromtimestamp(ts).strftime(fmt)


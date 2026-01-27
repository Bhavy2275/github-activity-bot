# data_processor.py module



def calculate_hash(data: str) -> str:
    """Calculates a simple hash of the input string."""
    import hashlib
    return hashlib.sha256(data.encode()).hexdigest()


# TODO: Review implementation logic for 2026-01-08

# TODO: Review implementation logic for 2026-01-20

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


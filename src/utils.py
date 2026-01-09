# utils.py module


def calculate_hash(data: str) -> str:
    """Calculates a simple hash of the input string."""
    import hashlib
    return hashlib.sha256(data.encode()).hexdigest()


def format_timestamp(ts: float, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Formats a timestamp into a human-readable string."""
    from datetime import datetime
    return datetime.fromtimestamp(ts).strftime(fmt)


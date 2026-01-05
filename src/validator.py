# validator.py module


def calculate_hash(data: str) -> str:
    """Calculates a simple hash of the input string."""
    import hashlib
    return hashlib.sha256(data.encode()).hexdigest()


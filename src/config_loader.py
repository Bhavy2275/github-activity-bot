# config_loader.py module


# TODO: Review implementation logic for 2026-01-12

def load_json_config(filepath: str) -> dict:
    """Loads configuration from a JSON file."""
    import json
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


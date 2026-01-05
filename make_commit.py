import os
import random
import subprocess
import datetime
import textwrap

# --- Configuration ---
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(ROOT_DIR, "src")
FILES = ["utils.py", "data_processor.py", "logger.py", "validator.py", "config_loader.py"]

# --- Content Banks ---

# Helper Functions to add
FUNCTIONS = [
    {
        "name": "calculate_hash",
        "code": """
def calculate_hash(data: str) -> str:
    \"\"\"Calculates a simple hash of the input string.\"\"\"
    import hashlib
    return hashlib.sha256(data.encode()).hexdigest()
""",
        "type": "feat",
        "msg": "feat(utils): implement secure hash calculation"
    },
    {
        "name": "format_timestamp",
        "code": """
def format_timestamp(ts: float, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    \"\"\"Formats a timestamp into a human-readable string.\"\"\"
    from datetime import datetime
    return datetime.fromtimestamp(ts).strftime(fmt)
""",
        "type": "feat",
        "msg": "feat(utils): add timestamp formatting helper"
    },
    {
        "name": "validate_email",
        "code": """
def validate_email(email: str) -> bool:
    \"\"\"Validates an email address using regex.\"\"\"
    import re
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))
""",
        "type": "feat",
        "msg": "feat(validator): add email validation logic"
    },
    {
        "name": "sanitize_input",
        "code": """
def sanitize_input(user_input: str) -> str:
    \"\"\"Removes potentially dangerous characters from input.\"\"\"
    return user_input.replace("<", "&lt;").replace(">", "&gt;")
""",
        "type": "fix",
        "msg": "fix(security): improve input sanitization"
    },
    {
        "name": "load_json_config",
        "code": """
def load_json_config(filepath: str) -> dict:
    \"\"\"Loads configuration from a JSON file.\"\"\"
    import json
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
""",
        "type": "feat",
        "msg": "feat(config): add json config loader"
    },
    {
        "name": "retry_operation",
        "code": """
def retry_operation(func, retries=3):
    \"\"\"Decorator to retry a function multiple times on failure.\"\"\"
    def wrapper(*args, **kwargs):
        for i in range(retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Retry {i+1} failed: {e}")
    return wrapper
""",
        "type": "feat",
        "msg": "feat(core): add retry mechanism decorator"
    }
]

# Docstrings updates (for refactoring)
DOCSTRINGS = [
    {
        "target": "calculate_hash",
        "content": "\"\"\"Calculates SHA-256 hash safely.\"\"\"",
        "msg": "docs(utils): improve calculate_hash docstring"
    },
    {
        "target": "validate_email",
        "content": "\"\"\"Checks if the provided string is a valid email format.\"\"\"",
        "msg": "docs(validator): clarify validation rules"
    }
]

# Variable renames (simple search/replace logic for demonstration)
RENAMES = [
    {"from": "data", "to": "input_data", "msg": "refactor: rename generic data variable"},
    {"from": "fmt", "to": "format_string", "msg": "refactor: use more descriptive argument name"}
]

class GitManager:
    @staticmethod
    def run(command):
        subprocess.run(command, check=True, shell=True)

    @staticmethod
    def commit(message):
        GitManager.run("git add .")
        GitManager.run(f'git commit -m "{message}"')

class CodeManager:
    def __init__(self):
        if not os.path.exists(SRC_DIR):
            os.makedirs(SRC_DIR)
        
        # Ensure base files exist
        for filename in FILES:
            path = os.path.join(SRC_DIR, filename)
            if not os.path.exists(path):
                with open(path, "w") as f:
                    f.write(f"# {filename} module\n\n")

    def get_random_file_path(self):
        return os.path.join(SRC_DIR, random.choice(FILES))

    def add_function(self):
        """Adds a random function to a random file."""
        func = random.choice(FUNCTIONS)
        target_file = self.get_random_file_path()
        
        # Check if function already exists in file (simple check)
        with open(target_file, "r") as f:
            content = f.read()
            
        if func['name'] in content:
            return False # Function already exists, try something else
            
        with open(target_file, "a") as f:
            f.write(func['code'])
            f.write("\n")
            
        return func['msg']

    def update_docs(self):
        """Mock update of documentation."""
        # For simplicity, we'll just append a TODO comment to a random file
        target_file = self.get_random_file_path()
        with open(target_file, "a") as f:
            f.write(f"\n# TODO: Review implementation logic for {datetime.datetime.now().strftime('%Y-%m-%d')}\n")
        return "docs: update todo markers"

    def refactor_formatting(self):
        """Mock formatting change."""
        target_file = self.get_random_file_path()
        with open(target_file, "r") as f:
            lines = f.readlines()
        
        # just adding a blank line somewhere
        if len(lines) > 2:
            idx = random.randint(1, len(lines)-1)
            lines.insert(idx, "\n")
            
        with open(target_file, "w") as f:
            f.writelines(lines)
            
        return "style: format code according to lint rules"

def main():
    manager = CodeManager()
    
    # Decisions
    # 60% chance to add a feature
    # 20% chance to doc update
    # 20% chance to format/refactor
    
    roll = random.random()
    commit_msg = ""
    
    if roll < 0.6:
        commit_msg = manager.add_function()
        # If adding failed (duplicate), fall back to docs
        if not commit_msg:
            commit_msg = manager.update_docs()
    elif roll < 0.8:
        commit_msg = manager.update_docs()
    else:
        commit_msg = manager.refactor_formatting()
        
    print(f"Performing action: {commit_msg}")
    
    try:
        GitManager.commit(commit_msg)
        print("Success.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

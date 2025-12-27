import os
import datetime
import random

def main():
    # Only commit 90% of the time to look more natural? 
    # Or 100% to ensure green square. Let's do 100% as requested.
    
    timestamp = datetime.datetime.now().isoformat()
    log_file = "activity.log"
    
    with open(log_file, "a") as f:
        f.write(f"Commit made at {timestamp}\n")
    
    print(f"Updated {log_file} at {timestamp}")

if __name__ == "__main__":
    main()

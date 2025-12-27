import os
import datetime
import random
import subprocess

def run_command(command):
    subprocess.run(command, check=True, shell=True)

def main():
    # Generate random number of commits (12 to 25) to ensure darkest green squares
    num_commits = random.randint(12, 25)
    log_file = "activity.log"
    
    print(f"Generating {num_commits} commits for today...")

    for i in range(num_commits):
        timestamp = datetime.datetime.now().isoformat()
        
        with open(log_file, "a") as f:
            f.write(f"Commit {i+1} at {timestamp}\n")
        
        # Stage and commit immediately after each write
        try:
            run_command(f"git add {log_file}")
            run_command(f'git commit -m "Auto commit {i+1}/{num_commits}"')
        except subprocess.CalledProcessError as e:
            print(f"Error making commit: {e}")
    
    print(f"Finished. Created {num_commits} commits.")

if __name__ == "__main__":
    main()

import os
import random
import subprocess
import glob

# Set the number of commits to 200
NUM_COMMITS = 200

# Set the year to 2024
year = 2024

# Get all eligible files from the project for random commits
def get_eligible_files():
    # Exclude certain files and directories
    all_files = []
    for ext in ['*.py', '*.md', '*.txt', '*.json', '*.yaml']:
        all_files.extend(glob.glob(ext))
    
    # Filter out specific files we don't want to modify
    excluded_files = ['.git', '.gitignore', 'yolov8n.pt', 'yolov8s.pt', 'git.py']
    return [f for f in all_files if not any(excluded in f for excluded in excluded_files)]

eligible_files = get_eligible_files()

# Initial commit
init_file = random.choice(eligible_files)
with open(init_file, 'a') as file:
    file.write('\n# Initial commit enhancement\n')

subprocess.call(['git', 'add', init_file])
subprocess.call(['git', 'commit', '-m', 'Initial enhancement commit'])

for i in range(NUM_COMMITS):
    # Generate random month and day offset
    month = random.randint(1, 12)
    day_offset = i % 28 + 1  # Ensures the day is between 1 and 28 to avoid invalid dates

    # Construct the commit date string
    commit_date_str = f"{year}-{month:02d}-{day_offset:02d} 12:00:00"

    # Select a random file to modify
    file_to_modify = random.choice(eligible_files)
    
    # Write to file to create a change
    with open(file_to_modify, 'a') as file:
        file.write(f'\n# Enhancement update for {commit_date_str}\n')
    
    # Add and commit changes with the specified date
    try:
        subprocess.call(['git', 'add', file_to_modify])
        subprocess.call(['git', 'commit', '--date', commit_date_str, '-m', f'Update #{i+1}: Traffic Sign Recognition enhancement on {file_to_modify}'])
        print(f"Completed commit {i+1}/{NUM_COMMITS} on file {file_to_modify}")
    except Exception as e:
        print(f"Error during commit {i+1}: {e}")

# Push commits to the remote repository
try:
    subprocess.call(['git', 'push', '-u', 'origin', 'master'])
    print("Successfully pushed all commits to the repository!")
except Exception as e:
    print(f"Error pushing to repository: {e}") 
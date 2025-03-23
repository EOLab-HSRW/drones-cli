import sys
import subprocess
from pathlib import Path

def get_latest_git_tag(directory: Path):

    if not directory.exists():
        print("Invalid directory")
        sys.exit(1) 

    try:
        result = subprocess.run(
            ["git", "describe", "--tags", "--abbrev=0"],
            cwd=directory,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.strip() or 'No tags found or repository issue.'}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        sys.exit(1)

def run_command(command: str, cwd: Path, check: bool = True):
    try:
        subprocess.run(command, cwd=cwd, shell=True, check=check, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error while executing: {command}\n{e}")
        sys.exit(1)

def git_clone_px4(dest: Path) -> bool:
    return fetch_repo("https://github.com/PX4/PX4-Autopilot.git", dest)

def fetch_repo(url: str, dest: Path) -> bool:

    if dest.exists():
        print(f"{dest.name} already there skipping clone.")
        return True

    try:
        print(f"Cloning into {dest}...")
        subprocess.run(["git", "clone", url, dest, "--recursive"], check=True)
        print(f"Repository cloned successfully into {dest}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while cloning: {e}")
        return False


def fetch_all_repos() -> bool:

    for drone_name, drone_obj in DRONES.items():
        fetch_repo(drone_obj.url, DRONES_DIR / drone_name)

    return True

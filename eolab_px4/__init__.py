from pathlib import Path

__version__ = '0.0.0'
__package__ = "eolab_px4"

CACHE_DIR = Path().home() / __package__
PX4_DIR = CACHE_DIR / "PX4-Autopilot"
DRONES_DIR = CACHE_DIR / "drones"


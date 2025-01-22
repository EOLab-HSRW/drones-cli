from pathlib import Path

__version__ = '0.0.0'
__package__ = "eolab_px4"

CACHE_DIR = Path().home() / ".cache" / __package__
PX4_DIR = CACHE_DIR / "PX4-Autopilot"

drones = {
    "phonix": {
        "url": "https://github.com/EOLab-HSRW/fw-phoenix",
        "id": 22101
    },
    "platypus": {
        "url": "https://github.com/EOLab-HSRW/fw-platypus",
        "id": 22102
    },
    "sar": {
        "url": "https://github.com/EOLab-HSRW/fw-sar",
        "id": 22103
    }
}

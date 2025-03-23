import yaml
import pickle
from pathlib import Path

class Loader:
    def __init__(self, yaml_file, cache_file='catalog.pkl'):
        self.yaml_file = Path(yaml_file)
        self.cache_file = self.yaml_file.parent / Path(cache_file)
        self.catalog = self._load_catalog()

    def _load_catalog(self):
        if self.cache_file.exists() and self.cache_file.stat().st_mtime >= self.yaml_file.stat().st_mtime:
            with self.cache_file.open('rb') as cache:
                return pickle.load(cache)
        else:
            with self.yaml_file.open('r') as file:
                config = yaml.safe_load(file)
            with self.cache_file.open('wb') as cache:
                pickle.dump(config, cache)
            return config

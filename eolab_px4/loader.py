import yaml
import pickle
from pathlib import Path

class Loader:
    def __init__(self, yaml_file, cache_file='catalog_cache.pkl'):
        self.yaml_file = Path(yaml_file)
        self.cache_file = Path(cache_file)
        self.config = self._load_config()
    
    def _load_config(self):
        if self.cache_file.exists() and self.cache_file.stat().st_mtime >= self.yaml_file.stat().st_mtime:
            with self.cache_file.open('rb') as cache:
                return pickle.load(cache)
        else:
            with self.yaml_file.open('r') as file:
                config = yaml.safe_load(file)
            with self.cache_file.open('wb') as cache:
                pickle.dump(config, cache)
            return config

loader = Loader(Path(__file__).parent / 'catalog.yml')

catalog = loader.config

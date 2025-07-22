import yaml
from utils.paths import ROOT_DIR
import os

class Config:
    def __init__(self, path=os.path.join(ROOT_DIR, "config", "config.yaml")):
        with open(path, "r") as f:
            self.cfg = yaml.safe_load(f)
            
    def __getitem__(self, item):
        return self.cfg[item]

if __name__ == "__main__":
    config = Config()
    print(config.cfg)
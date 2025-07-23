import yaml
from analyzer_gpt.utils.paths import ROOT_DIR
import os

class Config:
    def __init__(self, title=None, path=os.path.join(ROOT_DIR, "config", "config.yaml")):
        self.title = title
        with open(path, "r") as f:
            self.cfg = yaml.safe_load(f)
            
    def __getitem__(self, item):
        section = self.title if self.title else item
        return self.cfg[item]

if __name__ == "__main__":
    config = Config()
    print(config.cfg)
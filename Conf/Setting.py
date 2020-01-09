import yaml
import os
class Setting:
    def __init__(self, settingPath):
        # GameSettings
        with open(settingPath, 'r') as stream:
            try:
                self.conf = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
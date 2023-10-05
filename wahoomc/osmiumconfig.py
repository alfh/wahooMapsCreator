import json
import os

class OsmiumBatchExtractConfig:
    def __init__(self, directory, extracts):
        self.directory = directory
        self.extracts = extracts

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

class OsmiumExtract:
    def __init__(self, name, tileX, tileY, left, bottom, right, top):
        self.name = os.path.join(f'{tileX}', f'{tileY}', f'{name}')
        #self.tileX = tileX
        #self.tileY = tileY
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

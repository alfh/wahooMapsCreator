import json
import os

class OsmiumBatchExtractConfig:
    def __init__(self, directory, extracts):
        self.directory = directory
        self.extracts = extracts

    def toJson(self):
#        return json.dumps(self, default=lambda o: o.__dict__)
        return json.dumps({"directory": self.directory, "extracts": self.extracts}, default=lambda o: o.__dict__)
#        return json.dumps({"directory": self.directory}, default=lambda o: o.__dict__)

class OsmiumExtract:
    def __init__(self, name, tileX, tileY, left, bottom, right, top):
        self.output = os.path.join(f'{tileX}', f'{tileY}', f'{name}')
        self.output_format = 'pbf'
        #self.tileX = tileX
        #self.tileY = tileY
        self.bbox = [left, bottom, right, top]

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

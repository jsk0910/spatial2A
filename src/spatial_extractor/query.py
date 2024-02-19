from spatial_features import Spatial_feature

class Query:
    def __init__(self, q):
        self.query = q

    def encode(self):
        args = {}
        
        spatial_info = Spatial_feature()
        
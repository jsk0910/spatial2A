# base data structure
# spatial feature (address, (latitude, longitude), features)
# features is a integrated document about this location

class Spatial_feature:
    def __init__(self, args):
        self.address = args['address'] # address
        self.xy = (args['x'], args['y']) # latitude and longitude
        self.features = {} # document about this location

    # getter
    def get_address(self):
        return self.address
    
    def get_xy(self):
        return self.xy
    
    def get_feature(self):
        return self.features
    
    #setter
    def set_address(self, address):
        self.address = address
    
    def set_xy(self, x, y):
        self.xy = (x, y)
    
    def set_features(self, features):
        self.features = features
    
    def append_feature(self, key, feature):
        self.features[key] = feature
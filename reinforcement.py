from geometry import Circular

class Bar:
    def __init__(self, geometry:Circular) -> None:
        self.geometry = geometry
    
    
    @property
    def diameter(self):
        return self.geometry.diameter
    
    
    @property
    def area(self):
        return self.geometry.area


    def assign_coordinates(self, x, y):
        self.x = x
        self.y = y 
    
    @property
    def coordinates(self):
        try:
            return (self.x, self.y)
        except:
            return "No coordinates assigned yet"
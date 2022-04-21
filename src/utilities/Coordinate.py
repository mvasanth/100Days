class Coordinate:
    """
    Models a single coordinate.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def getOffset(self, row, column):
        return Coordinate(self.x + row, self.y + column)

    def __add__(self, other):
        if not isinstance(other, Coordinate):
            return NotImplemented

        return Coordinate(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Coordinate):
            return NotImplemented

        return Coordinate(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        if not isinstance(other, Coordinate):
            return False
        
        return self.x == other.getX() and self.y == other.getY()
    
    def __hash__(self):
        return hash((self.x, self.y))
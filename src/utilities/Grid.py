import queue
from typing import Any
from utilities.Coordinate import Coordinate

class Grid:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

        self._backingList = [ None ] * rows * columns

    def getAt(self, x : int, y : int):
        return self._backingList[self._getLinearOffset(x, y)]

    def getAt(self, coord : Coordinate):
        return self.getAt(coord.getX(), coord.getY())

    def getAt(self, base : Coordinate, offset : Coordinate):
        x = base.getX() + offset.getX()
        y = base.getY() + offset.getY()

        return self.getAt(x, y)

    def setAt(self, x : int, y : int, value : Any):
        self._backingList[self._getLinearOffset(x, y)] = value

    def setAt(self, coord : Coordinate, value : Any):
        self.setAt(coord.getX(), coord.getY(), value)

    def containsCoord(self, base : Coordinate, offset : Coordinate):
        x = base.getX() + offset.getX()
        y = base.getY() + offset.getY()

        return self._hasCoordinate(x, y)

    def BFS(self, startAt: Coordinate, visit):
        return grid_bfs_iter(self, startAt, visit)

    def _getLinearOffset(self, x : int, y : int):
        if not self._hasCoordinate(x, y):
            raise IndexError()

        return x * self.rows + y

    def _hasCoordinate(self, x : int, y : int):
        return x >= 0 and x < self.columns and y >= 0 and y < self.rows

    def __eq__(self, other):
        if not isinstance(other, Grid):
            return False
        
        return self.rows == other.rows \
            and self.columns == other.columns \
            and self._backingList == other._backingList
    
    def __hash__(self):
        return hash((self.rows, self.columns, self._backingList))

    def __iter__(self):
        return iter([ (x, y , self.getAt(x, y)) for x, y in zip(range(self.columns), range(self.rows))])

class grid_bfs_iter:
    def __init__(self, grid : Grid, start : Coordinate, visit):
        self._grid = grid
        self._queue = queue.Queue()
        self._visit = visit
        self._visited = set()

        self._queue.put(start)

    def __iter__(self):
        return self

    _neighbour_offsets = [ (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1) ]

    def __next__(self):
        if (self._queue.empty):
            raise StopIteration()

        cur = self._queue.get()

        self._visited.add(cur)

        validOffsets = [ offset for offset in self._neighbour_offsets 
            if self._grid.containsCoord(cur, offset)]

        maybeVisit = [ cur + offset for offset in validOffsets ]

        toVisit = [ absCoord for absCoord in maybeVisit 
            if absCoord not in self._visited 
            and self._visit(cur, offset) ]

        for n in toVisit:
            self._queue.put(n)
        
        return cur

def cardinal_neighbours(_, offset):
    return offset.getX() == 0 or offset.getY() == 0

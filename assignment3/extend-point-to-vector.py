import math

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"point({self.x}, {self.y})"
    
    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    
class vector(point):
    def __str__(self):
        return f'vector({self.x }, {self.y})'
    
    def _add_(self, other):
        return vector(self.x + other.x, self.y + other.y)
    
if __name__ == '__main__':
  
    p1 = point(1,2)
    p2 = point(1,2)
    p3 = point(3,4)

    print(p1)                     
    print(p1 == p2)               
    print(p1 == p3)               
    print(p1.distance_to(p3)) 

    v1 = vector(2,3)
    v2 = vector(3,4)
    v3 = v1 + v2

    print(v1)                     
    print(v2)                     
    print(v3)                     

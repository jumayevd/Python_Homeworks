import math


class Vector:
    def __init__(self, *components):
        self.components = components

    def __str__(self):
        return f"Vector({', '.join(map(str, self.components))})"

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Addition is only supported between Vector instances")
        if len(self.components) != len(other.components):
            raise ValueError("Vectors should have the same dimensions")
        
        return Vector(*(x + y for x,y in zip(self.components, other.components)))

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Subtraction is only supported between Vector instances")
        if len(self.components) != len(other.components):
            raise ValueError("")
        return Vector(*(x - y for x, y in zip(self.components, other.components)))
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*(x * other for x in self.components))
        
        if isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Component sizes should be the same")
            
            return sum(x*y for x,y in zip(self.components, other.components))
        return TypeError("Multiplication is supported with a scalar or another Vector")

    def __rmul__(self, other):
        # supporting scalar multiplication from the left
        return self * other
    
    def magnitude(self):
        return math.sqrt(sum(x**2 for x in self.components))
    
    def normalize(self):
        magnitude = self.magnitude()
        if magnitude == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector(*(x / magnitude for x in self.components))
    
if __name__ == "__main__":
    v1 = Vector(1,2,3)
    v2 = Vector(4,5,6)

    #printing the vector
    print(v1)

    #addition
    v3 = v1 + v2
    print(v3)

    #subtraction
    v4 = v2 - v1 
    print(v4) 

    #dot product
    v5 = v1 * v2
    print(v5)

    #scalar multiplication
    v6 = 3 * v1
    print(v6)

    #magnitude
    print(v1.magnitude())

    #normalize
    v_unit_vector = v1.normalize()
    print(v_unit_vector)
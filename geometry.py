from enum import Enum
from shapely.geometry import Polygon, Point


class GeometryType(Enum):
    """
    Enum for different types of geometry sections.
    """
    RECTANGULAR = 1
    CIRCULAR = 2


class Geometry:
    """
    Base class for geometric shapes.

    Attributes:
        geometry_section (GeometryType): Type of the geometry section.
    """
    def __init__(self, geometry_section: GeometryType) -> None:
        """
        Initializes the Geometry with a specified type.

        Parameters:
            geometry_section (GeometryType): The type of the geometry.
        """
        self.geometry_section = geometry_section


class Rectangular(Geometry):
    """
    Class representing a rectangular geometric shape.

    Attributes:
        length_1 (float): The length of the rectangle along one axis.
        length_2 (float): The length of the rectangle along the other axis.
    """
    def __init__(self, length_1: float, length_2: float) -> None:
        """
        Initializes a Rectangular geometry with specified lengths.

        Parameters:
            length_1 (float): The length of the rectangle along one axis.
            length_2 (float): The length of the rectangle along the other axis.
        """
        super().__init__(GeometryType.RECTANGULAR)
        self.length_1 = length_1
        self.length_2 = length_2

    @property
    def vertices(self) -> list[tuple[float, float]]:
        """
        List of vertices for the rectangle.

        Returns:
            list[tuple[float, float]]: A list of tuples representing the vertices.
        """
        return [
            (0, 0),  # Bottom-left corner
            (self.length_1, 0),  # Bottom-right corner
            (self.length_1, self.length_2),  # Top-right corner
            (0, self.length_2),  # Top-left corner
            (0, 0)  # Closing the polygon back to the bottom-left corner
        ]

    @property
    def shape(self) -> Polygon:
        """
        Polygon object representing the rectangle.

        Returns:
            Polygon: A Shapely Polygon object of the rectangle.
        """
        return Polygon(self.vertices)

    @property
    def area(self) -> float:
        """
        Calculates the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.shape.area

    @property
    def perimeter(self) -> float:
        """
        Calculates the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return self.shape.length

    @property
    def centroid(self) -> Point:
        """
        Calculates the centroid of the rectangle.

        Returns:
            Point: A Shapely Point object representing the centroid.
        """
        return self.shape.centroid

    def properties_dict(self) -> dict:
        """
        Returns a dictionary of all geometric properties of the rectangle.

        Returns:
            dict: A dictionary containing the area, perimeter, and centroid.
        """
        return {
            "Area": self.area,
            "Perimeter": self.perimeter,
            "Centroid": (self.centroid.x, self.centroid.y)
        }


class Circular(Geometry):
    """
    Class representing a circular geometric shape.

    Attributes:
        radius (float): The radius of the circle.
    """
    def __init__(self, radius: float) -> None:
        """
        Initializes a Circular geometry with a specified radius.

        Parameters:
            radius (float): The radius of the circle.
        """
        super().__init__(GeometryType.CIRCULAR)
        self.radius = radius

    @property
    def shape(self) -> Polygon:
        """
        Polygon object representing the circle using buffer.

        Returns:
            Polygon: A Shapely Polygon object of the circle.
        """
        return Point(0, 0).buffer(self.radius)

    @property
    def area(self) -> float:
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.shape.area

    @property
    def perimeter(self) -> float:
        """
        Calculates the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return self.shape.length

    @property
    def centroid(self) -> Point:
        """
        Calculates the centroid of the circle.

        Returns:
            Point: A Shapely Point object representing the centroid.
        """
        return self.shape.centroid

    def properties_dict(self) -> dict:
        """
        Returns a dictionary of all geometric properties of the circle.

        Returns:
            dict: A dictionary containing the area, perimeter, and centroid.
        """
        return {
            "Area": self.area,
            "Perimeter": self.perimeter,
            "Centroid": (self.centroid.x, self.centroid.y)
        }


# Example usage
if __name__ == "__main__":
    rectangle = Rectangular(length_1=4, length_2=3)
    print("Rectangle Properties:")
    print(f"Vertices: {rectangle.vertices}")
    print(f"Area: {rectangle.area}")
    print(f"Perimeter: {rectangle.perimeter}")
    print(f"Centroid: {rectangle.centroid}")
    print(f"Properties: {rectangle.properties_dict()}")

    circle = Circular(radius=5)
    print("\nCircle Properties:")
    print(f"Area: {circle.area}")
    print(f"Perimeter: {circle.perimeter}")
    print(f"Centroid: {circle.centroid}")
    print(f"Properties: {circle.properties_dict()}")

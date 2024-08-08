from geometry import GeometryType, Rectangular, Circular
import math

class Element:
    """
    Base class for geometric elements.

    This class provides methods to set the lengths of different dimensions of a geometric element.
    """
    def __init__(self, geometry_section: GeometryType) -> None:
        """
        Initializes an Element instance with no lengths set.
        """
        self.section = geometry_section
        self.length_1 = None
        self.length_2 = None
        self.length_3 = None
        self.radius = None
        self.geometry = None

    def set_length_1(self, length: float) -> None:
        """
        Sets the first length dimension of the element.

        Parameters:
            length (float): The length to set for the first dimension.
        """
        self.length_1 = length

    def set_length_2(self, length: float) -> None:
        """
        Sets the second length dimension of the element.

        Parameters:
            length (float): The length to set for the second dimension.
        """
        self.length_2 = length

    def set_length_3(self, length: float) -> None:
        """
        Sets the third length dimension of the element.

        Parameters:
            length (float): The length to set for the third dimension.
        """
        self.length_3 = length

    def set_radius(self, radius: float) -> None:
        """
        Sets the radius dimension of the element.

        Parameters:
            radius (float): The radius to set.
        """
        self.radius = radius

    def set_geometry(self) -> None:
        """
        Sets the geometry of the element based on the type of geometry section.
        """
        if self.section == GeometryType.RECTANGULAR:
            self.length_1 = float(input("Enter length 1: "))
            self.length_2 = float(input("Enter length 2: "))
            self.length_3 = float(input("Enter length 3: "))
            self.geometry = Rectangular(self.length_1, self.length_2)
        elif self.section == GeometryType.CIRCULAR:
            self.radius = float(input("Enter radius: "))
            self.length_1 = float(input("Enter length: "))
            self.geometry = Circular(self.radius)
        else:
            raise ValueError("Unsupported geometry type")

    @property
    def section_12(self) -> Rectangular:
        """
        Returns the cross-section defined by length_1 and length_2.

        Returns:
            Rectangular: A Rectangular cross-section with dimensions length_1 and length_2.
        """
        return Rectangular(self.length_1, self.length_2)

    @property
    def section_13(self) -> Rectangular:
        """
        Returns the cross-section defined by length_1 and length_3.

        Returns:
            Rectangular: A Rectangular cross-section with dimensions length_1 and length_3.
        """
        return Rectangular(self.length_1, self.length_3)

    @property
    def section_23(self) -> Rectangular:
        """
        Returns the cross-section defined by length_2 and length_3.

        Returns:
            Rectangular: A Rectangular cross-section with dimensions length_2 and length_3.
        """
        return Rectangular(self.length_2, self.length_3)

    @property
    def circular_section(self) -> Circular:
        """
        Returns a circular cross-section defined by radius.

        Returns:
            Circular: A Circular cross-section with the specified radius.
        """
        return Circular(self.radius)

    def volume(self) -> float:
        """
        Calculates the volume of the element based on its geometry type.

        Returns:
            float: The volume of the element.
        """
        if self.section == GeometryType.RECTANGULAR:
            return self.length_1 * self.length_2 * self.length_3
        elif self.section == GeometryType.CIRCULAR:
            return math.pi * (self.radius ** 2) * self.length_1
        else:
            raise ValueError("Unsupported geometry type")


# Example usage
if __name__ == "__main__":
    element_type = input("Enter the type of geometry (rectangular/circular): ").strip().lower()

    if element_type == "rectangular":
        element = Element(GeometryType.RECTANGULAR)
    elif element_type == "circular":
        element = Element(GeometryType.CIRCULAR)
    else:
        raise ValueError("Invalid geometry type entered")

    element.set_geometry()

    if element.section == GeometryType.RECTANGULAR:
        section_12 = element.section_12
        section_13 = element.section_13
        section_23 = element.section_23

        print("Section 12 Properties:")
        print(f"Area: {section_12.area}")
        print(f"Perimeter: {section_12.perimeter}")
        print(f"Centroid: {section_12.centroid}")

        print("\nSection 13 Properties:")
        print(f"Area: {section_13.area}")
        print(f"Perimeter: {section_13.perimeter}")
        print(f"Centroid: {section_13.centroid}")

        print("\nSection 23 Properties:")
        print(f"Area: {section_23.area}")
        print(f"Perimeter: {section_23.perimeter}")
        print(f"Centroid: {section_23.centroid}")

    elif element.section == GeometryType.CIRCULAR:
        circular_section = element.circular_section

        print("\nCircular Section Properties:")
        print(f"Area: {circular_section.area}")
        print(f"Perimeter: {circular_section.perimeter}")
        print(f"Diameter: {circular_section.diameter}")
        print(f"Centroid: {circular_section.centroid}")

    print(f"\nVolume: {element.volume()}")

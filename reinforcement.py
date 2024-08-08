from geometry import Circular

class Bar:
    """
    Class representing a reinforcing bar with a circular cross-section.

    Attributes:
        geometry (Circular): The circular geometry of the bar.
    """
    def __init__(self, geometry: Circular) -> None:
        """
        Initializes a Bar instance with a given circular geometry.

        Parameters:
            geometry (Circular): The circular geometry of the bar.
        """
        self.geometry = geometry
        self.x = None
        self.y = None
    
    @property
    def diameter(self) -> float:
        """
        Returns the diameter of the circular geometry.

        Returns:
            float: The diameter of the bar.
        """
        return self.geometry.diameter
    
    @property
    def area(self) -> float:
        """
        Returns the area of the circular geometry.

        Returns:
            float: The area of the bar.
        """
        return self.geometry.area

    def set_coordinates(self, x: float, y: float) -> None:
        """
        Sets the coordinates of the bar.

        Parameters:
            x (float): The x-coordinate of the bar.
            y (float): The y-coordinate of the bar.
        """
        self.x = x
        self.y = y
    
    @property
    def coordinates(self) -> tuple:
        """
        Returns the coordinates of the bar if set, otherwise returns a message.

        Returns:
            tuple: The coordinates (x, y) of the bar.
            str: Message indicating coordinates are not set.
        """
        try:
            return (self.x, self.y)
        except AttributeError:
            return "No coordinates assigned yet"


class Reinforcement:
    """
    Class representing reinforcement details.

    Attributes:
        bar (Bar): The reinforcing bar.
        cover (float): The cover of the reinforcement.
        location (str): The location of the reinforcement.
        quantity (int): The quantity of bars.
        spacing (float): The spacing between bars.
    """
    def __init__(self, bar: Bar = None, cover: float = None, location: str = None, 
                 quantity: int = None, spacing: float = None) -> None:
        """
        Initializes a Reinforcement instance with optional parameters.

        Parameters:
            bar (Bar): The reinforcing bar.
            cover (float): The cover of the reinforcement.
            location (str): The location of the reinforcement.
            quantity (int): The quantity of bars.
            spacing (float): The spacing between bars.
        """
        self.bar = bar
        self.cover = cover
        self.location = location
        self.quantity = quantity
        self.spacing = spacing

    # Setters
    def set_cover(self, cover: float) -> None:
        """
        Sets the cover of the reinforcement.

        Parameters:
            cover (float): The cover to set.
        """
        self.cover = cover

    def set_location(self, location: str) -> None:
        """
        Sets the location of the reinforcement.

        Parameters:
            location (str): The location to set.
        """
        if isinstance(location, str):
            self.location = location
        else:
            raise ValueError("Provide a valid location (string)")

    def set_quantity(self, quantity: int) -> None:
        """
        Sets the quantity of bars.

        Parameters:
            quantity (int): The quantity to set.
        """
        if isinstance(quantity, int):
            self.quantity = quantity
        else:
            raise ValueError("Provide a valid quantity (integer)")
    
    def set_spacing(self, spacing: float) -> None:
        """
        Sets the spacing between bars.

        Parameters:
            spacing (float): The spacing to set.
        """
        if isinstance(spacing, (int, float)):
            self.spacing = spacing
        else:
            raise ValueError("Provide a valid spacing (number)")

    def calculate_spacing(self, effective_space: float) -> None:
        """
        Calculates and sets the spacing between bars based on the effective space.

        Parameters:
            effective_space (float): The effective space available for bars.
        """
        try:
            self.spacing = effective_space / (self.quantity - 1)
        except TypeError:
            raise ValueError("Provide a valid quantity of bars first.")
        except ZeroDivisionError:
            raise ValueError("Quantity must be greater than 1 to calculate spacing.")

    def calculate_quantity(self, effective_space: float) -> None:
        """
        Calculates and sets the quantity of bars based on the effective space.

        Parameters:
            effective_space (float): The effective space available for bars.
        """
        try:
            self.quantity = int(effective_space / self.spacing) + 1
        except TypeError:
            raise ValueError("Provide a valid spacing first.")
        except ZeroDivisionError:
            raise ValueError("Spacing must be greater than 0 to calculate quantity.")


# Example usage
if __name__ == "__main__":
    # Create a Circular geometry for the Bar
    circular_geometry = Circular(radius=1.0)

    # Initialize a Bar with the Circular geometry
    bar = Bar(geometry=circular_geometry)

    # Set coordinates for the Bar
    bar.set_coordinates(x=5.0, y=10.0)

    # Print Bar properties
    print("Bar Properties:")
    print(f"Diameter: {bar.diameter}")
    print(f"Area: {bar.area}")
    print(f"Coordinates: {bar.coordinates}")

    # Initialize a Reinforcement with the Bar
    reinforcement = Reinforcement(bar=bar, cover=2.0, location="Top", quantity=5)

    # Set spacing for the Reinforcement
    reinforcement.set_spacing(15.0)

    # Print Reinforcement properties before calculations
    print("\nReinforcement Properties (Before Calculations):")
    print(f"Cover: {reinforcement.cover}")
    print(f"Location: {reinforcement.location}")
    print(f"Quantity: {reinforcement.quantity}")
    print(f"Spacing: {reinforcement.spacing}")

    # Calculate spacing based on an effective space
    effective_space = 60.0
    reinforcement.calculate_spacing(effective_space=effective_space)

    # Calculate quantity based on an effective space
    reinforcement.calculate_quantity(effective_space=effective_space)

    # Print Reinforcement properties after calculations
    print("\nReinforcement Properties (After Calculations):")
    print(f"Cover: {reinforcement.cover}")
    print(f"Location: {reinforcement.location}")
    print(f"Quantity: {reinforcement.quantity}")
    print(f"Spacing: {reinforcement.spacing}")

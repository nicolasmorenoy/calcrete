from geometry import Rectangular, Circular
from reinforcement import Bar

shape = Rectangular(10,20)
shape_2 = Circular(10)
diameter = 10
bar = Bar(Circular(diameter/2))
bar.set_coordinates(10,15)

if __name__ == "__main__":
    print(f"""Welcome to Calcrete, these are the properties of your section:
          {shape_2.properties_dict()}
          """)
    print(bar.coordinates)
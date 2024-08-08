from geometry import Rectangular, Circular
shape = Rectangular(10,20)
shape_2 = Circular(10)

if __name__ == "__main__":
    print(f"""Welcome to Calcrete, these are the properties of your section:
          {shape_2.properties_dict()}
          """)
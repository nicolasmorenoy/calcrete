from geometry import Rectangular
shape = Rectangular(10,20)

if __name__ == "__main__":
    print(f"""Welcome to Calcrete, these are the properties of your section:
          {shape.properties_dict()}
          """)
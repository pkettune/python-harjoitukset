import math

radius_str = input("Anna ympyrän säde (cm)\n")
radius = float(radius_str)
area = math.pi * radius**2
print (f"Ympyrän pinta-ala on:\n{area:.2f} cm²")
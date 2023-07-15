edge_length = float(input("Please enter the length of the edge: "))
surface_area = (3**(1/2)) * (edge_length)**2
rounding_surface = round(surface_area,3)
volume = (2**(1/2))/12 * (edge_length)**3
rounding_volume = round(volume,3)
print("the edge length that you input was: ",edge_length)
print("")
print("the surface area is: ",rounding_surface)
print("")
print("the volume is: ",rounding_volume)
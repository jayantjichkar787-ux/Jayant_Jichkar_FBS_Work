# 4. Calculate the cost of painting the following building’s walls (both interior and 
#    exterior). You need to accept area (one wall) and cost of both interior and 
#    exterior wall.  


area = float(input("Enter area of one wall: "))

interior_cost = float(input("Enter interior painting cost per wall: "))
exterior_cost = float(input("Enter exterior painting cost per wall: "))

# Two rooms have 8 walls in total.
# One wall is common between the two rooms.
# Therefore, total walls = 8 - 1 = 7

total_walls = 7

total_interior_cost = area * interior_cost * total_walls
total_exterior_cost = area * exterior_cost * total_walls

total_cost = total_interior_cost + total_exterior_cost

print("Interior painting cost =", total_interior_cost)
print("Exterior painting cost =", total_exterior_cost)
print("Total painting cost =", total_cost)
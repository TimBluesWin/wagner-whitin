import sys

def wagner_whitin(d, h, a):
    # Initialize minimum price for production
    z_min = sys.maxsize
    # Initialize max week for production
    max_week = 0
    number_of_weeks = len(d) 
    z_stars = []
    j_stars = []
    # Step 1 to number of weeks
    for i in range(0, number_of_weeks):
        production_options = []
        # Each row in the matrix (z_arrays)
        print("---- PLANNED HORIZON " + str(i + 1) + " ----")
        for j in range(0, (i + 1)):
            # Used to iterate holding costs for multiplication with d_t
            original_iteration = j
            current_cost = 0
            # Add value of Z_t
            if j != 0:
                current_cost = current_cost + z_stars[j-1]
            current_cost = current_cost + a[j]
            iteration = original_iteration
            while iteration <= i:
                total_h = 0
                # Keep for looping until iteration == i
                for x in range(original_iteration, iteration):
                    total_h = total_h + h[x]
                current_cost = current_cost + total_h * d[iteration]
                iteration = iteration + 1
            production_options.append(current_cost)
            print("Last week " + str(j + 1) + ": " + str(current_cost))
        # Find the minimum of the production option of the week
        z_star = min(production_options)
        z_min = z_star
        z_stars.append(z_star)
        max_week = min(range(len(production_options)), key=production_options.__getitem__)
        j_stars.append(max_week)
    answer = {"z_stars":z_stars, "j_stars":j_stars}
    return answer

d = [20, 50, 10, 50, 50, 10, 20, 40, 20, 30]
a = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
h = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
answers = wagner_whitin(d, h, a)
z_stars = answers['z_stars']
j_stars = answers['j_stars']
start_week = len(j_stars) - 1
end_week = len(j_stars) - 1
lot_number = 1
lot_size = 0
print("---Z values---")
for i in range(0, len(z_stars)):
    print("z_"+str(i)+": " + str(z_stars[i]))
print("---J values---")
for i in range(0, len(j_stars)):
    print("j_"+str(i)+": " + str(j_stars[i]))
while True:
    start_week = j_stars[end_week]
    print("---Lot number: " + str(lot_number) + "---")
    print("Start week: " + str(start_week + 1))
    print("End week: " + str(end_week + 1))
    for i in range(start_week, end_week + 1):
        lot_size = lot_size + d[i]
    print("Lot size: " + str(lot_size))
    if start_week == 0:
        break
    lot_size = 0
    lot_number = lot_number + 1
    end_week = start_week - 1
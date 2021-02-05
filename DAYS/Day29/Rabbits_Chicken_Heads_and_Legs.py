def solve(heads, legs):
    error_msg = "No solution"
    chicken_count = 0
    rabbit_count = 0
    if legs % 2 != 0:
        print("No Solution")
    else:
        rabbit_count = (legs-2*heads)/2
        chicken_count = (4*heads-legs)/2
        print(int(chicken_count))
        print(int(rabbit_count))


solve(35, 94)
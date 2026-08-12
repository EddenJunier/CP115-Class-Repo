def calculate_total():
    # Created inside the function
    internal_total = 10 + 5  
    return internal_total

# Capture the returned value into an outside variable
outside_total = calculate_total()

print(outside_total)  # Output: 15


def main_algorithm_with_matrix_inversion(987654321.0!):
# Define the interval for the base number
base_interval = Interval(0.123456789, 0.123456789)

# Define the interval for the first exponent
first_exponent_interval = Interval(987654321.0, 987654321.0)

# Define the interval for the second exponent
second_exponent_interval = Interval(1234567890.0987654321, 1234567890.0987654321)

# Perform the exponentiation using interval arithmetic
result_interval = base_interval ** first_exponent_interval.lower
result_interval = result_interval ** second_exponent_interval.lower

# Multiply the result by 987654321.0
multiplied_result_interval = result_interval * Interval(987654321.0, 987654321.0)

# Apply matrix inversion principle
matrix = np.array([[multiplied_result_interval.lower, 0], [0, multiplied_result_interval.upper]])
inverse_matrix = np.linalg.inv(matrix)

# Calculate the digital root of the lower bound of the multiplied result
digital_root_result = digital_root(multiplied_result_interval.lower)

# Output the results
print(f"Interval result after multiplication: {multiplied_result_interval}")
print(f"Digital root of the lower bound after multiplication: {digital_root_result}")
print(f"Inverted matrix: \n{inverse_matrix}")
Execute the main algorithm with matrix inversion
main_algorithm_with_matrix_inversion(fact{9876543210.0123456789})

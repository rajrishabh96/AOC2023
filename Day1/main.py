def extract_digits(line):
    # Need to find the first and last digits
    first_digit = next(char for char in line if char.isdigit())
    last_digit = next(char for char in reversed(line) if char.isdigit())
    # Now to form a digit
    calibration_value = int(first_digit + last_digit)
    return calibration_value

def calculate_total_of_digits(lines):
    # Extract the digits then form numbers from all the read lines
    calibration_values = [extract_digits(line) for line in lines]
    # Calculate the total sum of calibration values
    total_sum = sum(calibration_values)
    return total_sum


# Input
file_path = 'inputs.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

# Printing the results
if __name__ == '__main__':
    total_sum = calculate_total_of_digits(lines)
    print("Total sum of calibration values:", total_sum)
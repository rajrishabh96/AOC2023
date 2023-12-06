def extract_digits(line):
    # Need to find the first and last digits
    first_digit = next((char for char in line if char.isdigit()), None)
    last_digit = next((char for char in reversed(line) if char.isdigit()), None)
    # Now to form a digit
    if first_digit is not None and last_digit is not None:
        # Combine the digits to form a two-digit number
        combined = int(first_digit + last_digit)
        return combined
    else:
        return 0

def calculate_total_of_digits(lines):
    # Extract the digits then form numbers from all the read lines
    all_combined = [extract_digits(line) for line in lines]
    # Calculate the total sum of calibration values
    total_sum = sum(all_combined)
    return total_sum


# Input
file_path = 'inputs.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

# Printing the results
if __name__ == '__main__':
    total_sum = calculate_total_of_digits(lines)
    print("Total sum of calibration values:", total_sum)
import os
print("Current working directory:", os.getcwd())

input_filename = input("Enter the file name: ") + ".log"  # Correctly appends '.log' to the input
output_filename = input_filename.replace(".log", "") + "_auto.xyz"  # Constructs output filename correctly
print(input_filename)
def extract_lines(input_filename):
    start_extracting = False
    extracted_lines = []

    with open(input_filename, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if line_number >= 159:
                start_extracting = True
            
            if start_extracting:
                if "#atoms" in line:
                    break
                extracted_lines.append(line)
    
    return extracted_lines

extracted_lines = extract_lines(input_filename)
num_atom_for_Na = None  # Initialize to None; will store num_atom for "Na"

# Conversion factor
conversion_factor = 0.529177249

# Loop to find num_atom for a line containing "Na"
for line in extracted_lines:
    if "Na" in line:
        data = line.split()
        if len(data) > 0:
            num_atom_for_Na = data[0]  # Capture num_atom for "Na"
            break  # Stop after finding the first occurrence

# Writing to the output file
with open(output_filename, 'w') as file:
    if num_atom_for_Na is not None:
        # Write num_atom as the first line if "Na" was found, followed by a blank line
        file.write(f"{num_atom_for_Na}\n\n")  # Two newline characters to add a blank line

    # Loop to process and write all lines to the output file
    for line in extracted_lines:
        data = line.split()
        if len(data) >= 5:
            element = data[1]
            # Convert x, y, z to floats, multiply by the conversion factor, and format back to strings
            x = str(float(data[-3]) * conversion_factor)
            y = str(float(data[-2]) * conversion_factor)
            z = str(float(data[-1]) * conversion_factor)
            output_line = f"{element} {x} {y} {z}\n"
            file.write(output_line)
            
print(output_filename)
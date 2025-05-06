import os
import random
import pathlib
import subprocess

# Path to your training text file
training_text_file = 'langdata/chi_sim.training_text'

lines = []

# Read lines from the training text file
with open(training_text_file, 'r', encoding="utf-8") as input_file:
    for line in input_file.readlines():
        lines.append(line.strip())

# Output directory for the generated images and ground truth files
output_directory = 'tesstrain/data/ARIRanbac-ground-truth'

# Create the directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory, exist_ok=True)

# Shuffle the lines to randomize the data
random.shuffle(lines)

# Number of lines to use (500 lines in this case)
count = 12000
lines = lines[:count]

# Starting line count (starting from 6000)
line_count = 54000
fonts =  ['Arial Unicode MS', 'AR PL UKai CN']  # List of fonts

for line in lines:
    # Construct the filename for the ground truth file
    training_text_file_name = pathlib.Path(training_text_file).stem
    line_training_text = os.path.join(output_directory, f'{training_text_file_name}_{line_count}.gt.txt')
    
    # Write the line to the ground truth file
    with open(line_training_text, 'w', encoding="utf-8") as output_file:
        output_file.writelines([line])

    # Choose a random font from the list
    random_font = random.choice(fonts)

    # Base filename for the image output
    file_base_name = f'chi_sim_{line_count}'

    # Run the text2image command to generate the image
    subprocess.run([
        'text2image',
        f'--font={random_font}',  # Use a random font
        f'--text={line_training_text}', 
        f'--outputbase={output_directory}/{file_base_name}',
        '--max_pages=1',
        '--strip_unrenderable_words',
        '--leading=32',
        '--xsize=2550',
        '--ysize=480',
        '--char_spacing=0',
        '--exposure=0',
        '--unicharset_file=langdata/chi_sim.unicharset'
    ])

    # Increment the line count for the next iteration
    line_count += 1
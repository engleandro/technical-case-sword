import sys

from app.processor import process_file, write_results


if len(sys.argv) != 3:
    print("Usage: python your_script.py input_file.txt output_file.txt")
    sys.exit(1)

input_file, output_file = sys.argv[1], sys.argv[2]

# set the number of threads
number_of_workers: int = 10

try:
    word_counts = process_file(input_file, num_workers=number_of_workers)
    write_results(word_counts, output_file)
    print(f"The text processing outputs have been written to {output_file}")
except Exception as error:
    print(f"An error occurred: {error}")
    sys.exit(1)

import sys
import re
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from threading import Lock


def count_words(chunk: str) -> Counter:
    words = re.findall(r'\w+', chunk.lower())
    words = [word for word in words if word.isalpha()]
    return Counter(words)

def read_file_safely(filename: str) -> None:
    encodings = ['utf-8', 'iso-8859-1', 'cp1252']
    
    for encoding in encodings:
        try:
            with open(filename, 'r', encoding=encoding) as file:
                return file.read()
        except UnicodeDecodeError:
            continue
    
    raise ValueError(f"Unable to read the file {filename}.")

def process_file(filename: str, num_workers: int=10) -> Counter:
    try:
        content = read_file_safely(filename)
    except ValueError as e:
        print(f"An error has occurred: {e}")
        sys.exit(1)

    chunk_size = max(1, len(content) // num_workers)
    chunks = [content[i:i+chunk_size] for i in range(0, len(content), chunk_size)]

    total_counts = Counter()
    lock = Lock()

    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        future_to_chunk = {executor.submit(count_words, chunk): chunk for chunk in chunks}
        for future in future_to_chunk:
            try:
                result = future.result()
                with lock:
                    total_counts.update(result)
            except Exception as exc:
                print(f'An exception had occurred: {exc}')

    return total_counts

def write_results(counts: Counter, output_filename: str) -> None:
    try:
        with open(output_filename, 'w', encoding='utf-8') as file:
            for word, count in counts.most_common():
                file.write(f"{word} {count}\n")
    except IOError as e:
        print(f"Error writing to file {output_filename}: {e}")
        sys.exit(1)

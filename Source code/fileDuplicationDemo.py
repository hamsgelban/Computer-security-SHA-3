import hashlib
import os
from collections import defaultdict

# Define a function to calculate the SHA-3 hash of a file's content
def calculate_sha3(file_path):
    sha3 = hashlib.sha3_256()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(65536)  # Read the file in 64 KB chunks
            if not data:
                break
            sha3.update(data)
    return sha3.hexdigest()

# Define a function to find duplicate files in a directory
def find_duplicates(directory):
    file_hashes = defaultdict(list)
    duplicates = []

    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_hash = calculate_sha3(file_path)
            file_hashes[file_hash].append(file_path)

    for hash, paths in file_hashes.items():
        if len(paths) > 1:
            duplicates.append(paths)

    return duplicates

if __name__ == '__main__':
    directory = r'C:\Users\hamsg\OneDrive - Qatar University\Fall 2023\software eng'  
    duplicates = find_duplicates(directory)

    if duplicates:
        print("Duplicate files found:")
        for duplicate_set in duplicates:
            print('\n'.join(duplicate_set))
    else:
        print("No duplicate files found.")

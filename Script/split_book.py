#!/usr/bin/env python3
import os

# Configuration
input_path = 'C:\Users\kisel\IdeaProjects\Book\Book 1\-- Стивен Кинг долгая прогулка.txt'
part_size = 100000  # 100,000 characters per part

# Read the input file with UTF-8 encoding
with open(input_path, 'r', encoding='utf-8') as f:
    content = f.read()

total_length = len(content)

# Calculate number of parts needed
num_parts = (total_length + part_size - 1) // part_size
parts = []

print(f"Total file size: {total_length} characters")
print(f"Part size: {part_size} characters")
print(f"Number of parts to create: {num_parts}")
print()

# Create each part file
for i in range(num_parts):
    start = i * part_size
    end = start + part_size
    if end > total_length:
        end = total_length

    part_content = content[start:end]
    part_number = (i + 1)
    part_filename = f"Часть_{part_number:02d}.txt"
    part_path = os.path.join(os.path.dirname(input_path), part_filename)

    # Write the part to file
    with open(part_path, 'w', encoding='utf-8') as f:
        f.write(part_content)

    parts.append(part_path)
    print(f"Created: {part_filename}")

print()
print(f"Successfully created {len(parts)} part files")

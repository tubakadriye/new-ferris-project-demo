import os

script_dir = os.path.dirname(__file__)
rel_path = "test_file.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path, 'r') as f:
    for line in f:
        print(line)
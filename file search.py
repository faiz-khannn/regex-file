import regex as re
import os

def search_string_in_files(pattern, directory):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            with open(os.path.join(directory, filename), 'r') as file:
                lines = file.readlines()
                for i, line in enumerate(lines, 1):
                    matches = re.finditer(pattern, line)
                    for match in matches:
                        print(f"Found '{match.group()}' in '{filename}' at line {i}:")
                        print(line)

def main():
    search_pattern = input("Enter the regex pattern to search for: ")
    search_directory = input("Enter the directory to search in: ")

    search_string_in_files(search_pattern, search_directory)

if __name__ == "__main__":
    main()

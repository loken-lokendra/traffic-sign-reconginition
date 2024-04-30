import os
import subprocess
import ast

def extract_libraries_from_file(file_path):
    libraries = set()
    with open(file_path, 'r') as f:
        tree = ast.parse(f.read(), filename=file_path)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    libraries.add(alias.name)
            elif isinstance(node, ast.ImportFrom):
                libraries.add(node.module)
    return libraries

def install_libraries(libraries):
    for lib in libraries:
        subprocess.call(['pip', 'install', lib])

if __name__ == "__main__":
    file_path = input("Enter the path to your Python file: ")
    if not os.path.isfile(file_path):
        print("File not found.")
    else:
        required_libraries = extract_libraries_from_file(file_path)
        if required_libraries:
            print("The following libraries will be installed:")
            print(", ".join(required_libraries))
            install_libraries(required_libraries)
            print("Libraries installed successfully.")
        else:
            print("No external libraries found in the file.")

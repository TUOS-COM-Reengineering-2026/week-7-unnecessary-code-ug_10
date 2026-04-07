import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import ast
import re


def read_file(file_path: str) -> list[str]:
    """
    Read the contents of a file.

    :param file_path: The path to the file to read.
    :return: The contents of the file.
    """

    print(f"Read file {file_path}")
    read = False

    if not os.path.isfile(file_path):
        raise ValueError(f"{file_path} is not a file.")

    with open(file_path, 'r') as file:
        # if not read:
        #     print(file.readline())
        #     read = True
        return file.readlines()

# CAN USE THIS IN THE GROUP PROJECT to identify code clones. Use it on Arrow.
def compute_jaccard_similarity(a: str, b: str) -> float:
    """
    Compute the Jaccard similarity between two programs.

    :param a: The first program to compare.
    :param b: The second program to compare.
    :return: The Jaccard similarity between the two programs.
    """

    #Keeping this if you want to test the entire files 
    # (might also need to normalise all of the lines of code though...)

    # a_content = read_file(a)
    # b_content = read_file(b)

    # a_set = set(a_content)
    # b_set = set(b_content)

    a_set = set(map(normalize, a))
    b_set = set(map(normalize, b))

    return len(a_set & b_set)/len(a_set | b_set)

def visualise_dot_plot(a: str, b: str) -> str:
    a_content = read_file(a)
    b_content = read_file(b)

    plot = '-' * 80 + '\n'
    for i in range(len(a_content)):
        plot += f'x{i}: {a_content[i]}'
    plot += '-' * 80 + '\n'

    for j in range(len(b_content)):
        plot += f'y{j}: {b_content[j]}'
    plot += '-' * 80 + '\n'

    plot += '\t'
    for i in range(len(a_content)):
        plot += f"x{i+1}\t"
    plot += '\n'
    for j in range(len(b_content)):
        plot += f"y{j+1}\t"
        for i in range(len(a_content)):
            if a_content[i] == b_content[j]:
                plot += f"*\t"
            else:
                plot += f" \t"
        plot += '\n'

    plot += '-' * 80

    return plot.strip()



def find_method(path_file: str, method_name: str) -> list[str]:

    with open(path_file, "r") as f:
        source = f.read()

    tree = ast.parse(source)
    lines = source.splitlines()

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == method_name:
            start = node.lineno - 1
            end = node.end_lineno
            return lines[start:end]

    return []


def normalize(line: str) -> str:
    line = re.sub(r"#.*", "", line)  # remove comments
    return line.strip()

def draw_graph(file1: str, file2: str, func1: str, func2: str):
    column_content = find_method(file1, func1)
    row_content = find_method(file2, func2)

    xdata = []
    ydata = []

    for j in range(len(row_content)):
        for i in range(len(column_content)):
            if normalize(column_content[i]) == normalize(row_content[j]):
                xdata.append(i + 1)
                ydata.append(j + 1)

    fig, ax = plt.subplots()
    ax.plot(xdata, ydata, 'o')
    ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
    ax.invert_yaxis()

    plt.show()


if __name__ == "__main__":
    path_dir = r"d:\modules25_26\Reengineering\arrow-repo\arrow"

    #Change this absolute path to test the 2 files listed below
    #test_path = "d:\modules25_26\Reengineering\week-7-unnecessary-code-ug_10"
    file = "arrow.py"
    #file2 = "arrow.py"
    

    #is_same_variable_name(line1,line2)

    func1 = "fromordinal"
    func2 = "strptime"

    path_file = os.sep.join([path_dir, file])

    method1 = find_method(path_file, func1)
    method2 = find_method(path_file, func2)

    if not method1:
        print(f"Function {func1} not found in {file}")
    if not method2:
        print(f"Function {func2} not found in {file}")

    similarity = compute_jaccard_similarity(method1, method2)
    print(f"\n Jaccard similarity: {similarity}")
    

    draw_graph(path_file, path_file, func1, func2)



import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np

ASSIGNMENT = '='
BOOLEAN = ['==', '!=','<=','>=','<','>']

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

    a_content = read_file(a)
    b_content = read_file(b)

    a_set = set(a_content)
    b_set = set(b_content)

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




def find_method(path_file, method_name) -> list[str]:
    IDENTIFIER = "def"
    content = read_file(path_file)
    print(len(content))

    method_code = []
    reading_code = False

    for line in content:
        
        if reading_code:
            method_code.append(line)

        if line.startswith(IDENTIFIER):
            if method_name in line and not reading_code:
                method_code.append(line)
                reading_code = True
            else:
                reading_code = False
                
                
    return method_code

def draw_graph(a: str, b: str):
    column_content = find_method(a, "fromordinal(cls, ordinal: int)")
    row_content = find_method(b, "strptime(cls, date_str: str, fmt: str, tzinfo: Optional[TZ_EXPR] = None)")

    xdata = np.array([])
    ydata = np.array([])

    for j in range (len(row_content)):
        #print(f"j: {j}")
        for i in range(len(column_content)):
            #print(f"i: {i}")
            if column_content[i].strip() == row_content[j].strip():
                xdata = np.append(xdata, [i+1])
                ydata = np.append(ydata, [j+1])


    fig, ax = plt.subplots()
    print(xdata)
    ax.plot(xdata, ydata, 'o')
    ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
    ax.invert_yaxis()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    
    plt.show()



if __name__ == "__main__":
    path_dir = r"d:\modules25_26\Reengineering\arrow-repo\arrow"

    #Change this absolute path to test the 2 files listed below
    test_path = "d:\modules25_26\Reengineering\week-7-unnecessary-code-ug_10"
    file = "dead_code.py"
    file2 = "dying_code.py"
    

    line1 = "t = 5"
    line2 = "x = 5"

    #is_same_variable_name(line1,line2)

    path_file = os.sep.join([test_path, file])
    #find_method(path_file, "example_function():")
    # print(path_file1)
    path_file2 = os.sep.join([test_path, file2])

    draw_graph(path_file, path_file2)

    #graph = visualise_dot_plot(path_file, path_file2)
    #print(graph)

    # print("\n")

    # similarity = compute_jaccard_similarity(path_file1, path_file2)

    # print(similarity)



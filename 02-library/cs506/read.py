def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    data = open(csv_file_path, "r")
    lines = data.readlines()
    output = []
    for line in lines:
        output.append([line])
    
    return output

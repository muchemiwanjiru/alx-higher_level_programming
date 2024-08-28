def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div and returns a new matrix with rounded values."""
    
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if each row is of the same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check if all elements in the matrix are integers or floats
    for row in matrix:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if div is a number and not zero
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Divide all elements and round to 2 decimal places
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    
    return new_matrix


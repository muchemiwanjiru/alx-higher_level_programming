#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
  This function divides all elements of a matrix.

  Args:
    matrix: The matrix to be divided.
    div: The divisor.

  Returns:
    The new matrix.
  """

  if not isinstance(matrix, list):
      raise TypeError("matrix must be a list of lists")

  for row in matrix:
      if not isinstance(row, list):
          raise TypeError("matrix must be a list of lists")

    if len(row) != len(matrix[0]):
        raise TypeError("Each row of the matrix must have the same size")

  if not isinstance(div, (int, float)):
      raise TypeError("div must be a number")

  if div == 0:
      raise ZeroDivisionError("division by zero")

  new_matrix = []
  for row in matrix:
      new_row = [round(num / div, 2) for num in row]
    new_matrix.append(new_row)

  return new_matrix

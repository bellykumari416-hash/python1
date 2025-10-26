def print_inverted_right_triangle(rows):
  """
  Prints an inverted right-angle triangle pattern of asterisks.

  Args:
    rows: The number of rows in the triangle.
  """
  for i in range(rows, 0, -1):  # Outer loop for rows, decreasing from 'rows' to 1
    for j in range(i):          # Inner loop for printing stars in each row
      print("*", end="")
    print()  # Move to the next line after each row

# Example usage:
num_rows = 5
print_inverted_right_triangle(num_rows)
def generate_permutations(data):
  """
  Generator function to yield all permutations of a given list.

  Args:
    data: A list of elements.

  Yields:
    All possible permutations of the data as lists.
  """
  if len(data) <= 1:
    yield data
  else:
    for i, element in enumerate(data):
      for permutation in generate_permutations(data[:i] + data[i+1:]):
         yield [element] + permutation

# Example usage
data = [1, 2, 3]
for permutation in generate_permutations(data):
  print(permutation)

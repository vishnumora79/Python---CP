
def generate_permutations(data):

    if len(data) <= 1:
       return data
    else:
       for i, element in enumerate(data):
         for permutation in generate_permutations(data[:i] + data[i+1:]):
           return [element] + permutation
 
data = [1, 2, 3]
for permutation in generate_permutations(data):
   print(permutation)

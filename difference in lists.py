# Get the difference between two lists

list_A = ['One', 'Two', 'Three']
list_B = ['One', 'Two', 'Three', 'Four']

difference = list(set(list_A)-set(list_B))

print(f'The difference: {difference}')
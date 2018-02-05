

# COMPREHENSION


# for loop

h_letters = []
for letter in 'human':
    h_letters.append(letter)
print(h_letters)


# list comprehension

h_letters = [letter for letter in 'human']
print(h_letters)

upper_letters = [letter.upper() for letter in 'human']
print(upper_letters)


# lambda functions

l_letters = list(map(lambda x: x, 'human'))
print(l_letters)


# conditional

number_list = [x for x in range(20) if x%2 == 0]
print(number_list)

num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)

obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)


# loops in comprehension
matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
transposed = []
for i in range(2):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
        transposed.append(transposed_row)
print(transposed)
# prints: [[1, 3, 5, 7], [1, 3, 5, 7], [1, 3, 5, 7], [1, 3, 5, 7], [2, 4, 6, 8], [2, 4, 6, 8], [2, 4, 6, 8], [2, 4, 6, 8]]

transpose = [[row[i] for row in matrix] for i in range(2)]
print(transpose)
# prints: [[1, 3, 5, 7], [2, 4, 6, 8]]
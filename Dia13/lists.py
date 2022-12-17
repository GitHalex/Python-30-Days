number = [-4, -3, -2, -1, 0, 2, 4, 6]
negative = [i for i in number if i <= 0]
print(negative)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
aplanar = [number for row in list_of_lists for number in row]
print(aplanar)


tuplas = [(i, i**i, i**i, i**i, i**i, i**i, i**i) for i in range(11)]
print(tuplas)
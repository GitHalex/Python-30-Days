number = [-4, -3, -2, -1, 0, 2, 4, 6]
negative = [i for i in number if i <= 0]
print(negative)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
aplanar = [number for row in list_of_lists for number in row]
print(aplanar)


tuplas = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(tuplas)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
lista_countries = countries.split(' ')
print(lista_countries)
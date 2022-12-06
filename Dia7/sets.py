# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
empresas = ('Jala','Nearshore','Platzi')
it_companies.update(empresas)
print(it_companies)
eliminado = it_companies.pop()
print(eliminado)
print(it_companies)
print(len(it_companies))

unidos = A.union(B)
print(unidos)

interseccion = A.intersection(B)
print(interseccion)

disjuntos = A.isdisjoint(B)
print(disjuntos)

diferencia_simetrica = A.symmetric_difference(B)
print(diferencia_simetrica)

del it_companies
# print(it_companies)
conjunto_edades = set(age)
print(conjunto_edades)
grande = len(age)>len(conjunto_edades)
print(grande)

palabra = "I am a teacher and I love to inspire and teach people"
lista_palabras = palabra.split()
print(lista_palabras)

palabras_unicas = set(lista_palabras)
print(palabras_unicas)



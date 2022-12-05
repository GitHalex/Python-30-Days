vacia =()
hombres = ('Saul','Abel','Edson')
mujeres = ('Pichon','Erikis','Iniki')
familia = hombres+mujeres
print(familia)

print(f'Tamaño de mi familia {len(familia)}')

familia = list(familia)
print(familia)
familia.append('Pacifico')
familia.append('Claudina')

print(familia)

familia_members = tuple(familia)
print(familia_members)

hermanos, padres = familia_members[:6], familia_members[6:]
print(hermanos)
print(padres)

frutas = ('Manzana','Pera','sandia','papaya')
verduras = ('tomate','zanahoria','lechuga','papa')
prod_animales = ('pollo','higado','panza','chuleta')
food_stuff_tp = frutas+verduras+prod_animales
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

primeros_tres = food_stuff_lt[:3]
ultimos_tres = food_stuff_lt[-3:]
print(primeros_tres)
print(ultimos_tres)

del food_stuff_tp
print('Manzana' in food_stuff_lt)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Sweden'in nordic_countries)
print('Iceland'in nordic_countries)
""" edad = int(input("Introduzca su edad: "))
if edad >= 18:
   print('You are old enough to learn to drive.')
else:
   edad = 18-edad
   print(f'You need {edad} more years to learn to drive') """

""" my_age = int(input('introduzca mi edad: '))
your_age = int(input('introduzca tu edad: ')) """

""" if my_age > your_age:
   my_age = my_age-your_age
   print(f'I am {my_age} years older than you ')
elif your_age > my_age:
   your_age = your_age-my_age
   print(f'You are {your_age} years older than me')
else:
   print(f'{my_age} == {your_age} misma edad') """

""" number_one = int(input('Enter number one: '))
number_two = int(input('Enter number two: ')) """

""" if number_two > number_one:
   print(f'{number_two} is greater than {number_one}')
elif number_one > number_two:
   print(f'{number_one} is greater than {number_two}')
else:
   print(f'{number_one} is similitud than {number_two}') """

""" score = int(input('Score student: '))
if score >= 90 and score <= 100:
   print(f'{score} - A')
elif score >= 70 and score <= 89:
   print(f'{score} - B')
elif score >= 60 and score <= 69:
   print(f'{score} - C')
elif score >= 50 and score <= 59:
   print(f'{score} - D')
elif score >= 0 and score <= 49:
   print(f'{score} - F')
else:
   print(f'{score} valor no valido') """

""" mes = input('ingrese un mes: ')
valor = mes.lower()
if valor == 'septiembre' or valor == 'octubre' or valor == 'noviembre':
   print('OTOÑO')
elif valor == 'diciembre' or valor == 'enero' or valor == 'febrero':
   print('INVIERNO')
elif valor == 'marzo' or valor == 'abril' or valor == 'mayo':
   print('PRIMAVERA')
elif valor == 'junio' or valor == 'julio' or valor == 'agosto':
   print('VERANO')
else:
   print(f'{valor} dato incorrecto') """

""" fruits = ['banana', 'orange', 'mango', 'lemon']
fruta = input('ingrese una fruta: ')
if fruta in fruits:
   print('Esa fruta ya existe en la lista')
else:
   fruits.append(fruta)
   print(fruits)
 """

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
""" if 'skills' in person:
   print(person['skills'][2])
else:
   print('La persona no tiene skills') """

""" existe = person.get('skills')
print(existe)
for skill in existe:
   if skill == 'Python':
      print(f'Existe {skill} in habilidades')
      break
   else:
      continue """

""" habilidades = person.get('skills')
if 'JavaScript' in habilidades and 'Python' in habilidades:
   print('He is a front end developer')
elif 'Node' in habilidades and 'Python' in habilidades and 'MongoDB' in habilidades:
   print('He is a backend developer')
elif 'React' in habilidades and 'Node' in habilidades and 'MongoDB' in habilidades:
   print('He is a fullstack developer')
else:
   print('unknown title') """

""" if person['is_married'] == True and person['country'] == 'Finland':
   print(person['first_name'], person['last_name'] + ' lives in ', person['country'], 'He is married' ) """
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
       }
}

""" if 'skills' in person:
   print(person['skills'][2])
else:
   print('no tiene habilidades')

lista_habilidades = person.get('skills')
for habilidades in lista_habilidades:
   if habilidades == 'Python':
      print(f'{habilidades} Si tiene ese skills') """

lista_habilidades = person.get('skills')

flag = True
for skill in lista_habilidades:
   if skill == 'JavaScript':
      flag = True
   elif flag and skill == 'React':
      print('El es un desarrollador Front-end')
   elif skill == 'Node':
      flag == True
   elif flag and skill == 'MongoDB':
      flag = True
   elif flag and skill == 'Python':
      print('Backend')
   else:
      print('No tiene habilidades')


casado = person['is_married']
if casado and person['country'] == 'Finland':
   print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. he is married ")
   



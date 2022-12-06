perro = {}
perro['nombre'] = 'Marrano'
print(perro)
perro['color'] = 'Golden'
perro['patas'] =4
perro['edad'] = 2
print(perro)

students = {'first_name': 'Alex','last_name':'Bernal','sexo':'Masculino','edad':28,'is_married':False,'habilidades':['Python','Javascript','React','java'],'country':{'Potosi':'uyuni','address':'11 de julio'}}
print(students)
print(len(students))

skills = students.get('habilidades')
print(skills)
print(type(skills))

students['habilidades'] = 'MongoDB'
print(students)
students['habilidades'] = 'C++'
print(students)

claves = students.keys()
print(claves)

tupla_dic = students.items()
print(tupla_dic)

del students['is_married']
print(students)

del perro

print(perro)



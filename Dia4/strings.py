espacio = " "
cadena = 'treinta' + espacio + 'Dias' + espacio +  'De' + espacio + 'Python'
cadena2 = 'Codificacion' + espacio + 'Para' + espacio + 'Todos'
print(cadena)
print(cadena2)

empresa = 'Coding For All'
sub_empresa = 'Coding'
print(empresa)
print(len(empresa))
print(empresa.upper())
print(empresa.lower())
print(empresa.capitalize())
print(empresa.title())
print(empresa.swapcase())
print(empresa[0:6])
print(empresa.find(sub_empresa))
print(empresa.index(sub_empresa))
print(empresa.replace('Coding', 'Python'))
separador = empresa.split()
print(separador)

company = 'Facebook, Google, Microsoft, Aplle, IBM, Oracle, Amazon'
print(company.split(','))
print(empresa[0])

last_index = len(empresa) - 1
print(empresa[last_index]) 
print(empresa[9])

python_a = 'Python for Everyone'
print(python_a[0:-1:6])

print(empresa[-6:0:-2])

sub_empresa = 'C'
f_string = 'F'
print(empresa.index(sub_empresa))
print(empresa.index(f_string))

print(empresa.rfind('l'))

porque = 'You cannot end a sentence qith because because because is a conjuntion'
print(porque.index('because'))
print(porque.find('because'))
print(porque.rfind('because'))

print(porque[31:54])
print(porque.find('because'))

print(empresa.startswith('Coding'))

cadena = '  Coding For All  '
cadena2 = cadena.strip('  ')
print(len(cadena2), cadena2)

variable = '30DaysOfPython'
print(variable.isidentifier())
variable2 = 'thirty_days_of_python'
print(variable2.isidentifier())

libraries_of_python = ['Django','Flask', 'Bottle','Pyramid','Falcon']
librerias_cadena = ' '.join(libraries_of_python)
print(type(librerias_cadena), type(librerias_cadena))

print('I am enjoying this challenge\nI just wonder what is next')

palabra = 'Name\tAge\tCoutry\tCity\nAsabeneh\t250\tFinland\tHelsinki'
print(palabra.expandtabs(10))

radius = 10
area = 3.14 * radius **2
print(f'The area of circle with radius {radius} is {int(area)} meters square')

print(f'8+6={8+6}')
print(f'8-6={8-6}')
print(f'8*6={8*6}')
print(f'8/6={round(8/6, 2)}')
print(f'8%6={8%6}')
print(f'8//6={8//6}')
print(f'8**6={8**6}')
list_vacia = []
list_elementos =['perro','frutas',2022,'cuadersno',True]
print(len(list_elementos))
print(list_elementos[::2])

mix_data_types =['Alex',28,1.6,'soltero','uyuni']
it_companies =['Facebok','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(mix_data_types)
print(it_companies)
print(len(it_companies))
print(it_companies[::3])

it_companies[0] = 'Jala'
print(it_companies)

it_companies.append('Facebook')
print(it_companies)

it_companies.insert(4, 'Potosi')
print(it_companies)

it_companies[0] = 'JALA'
print(it_companies)

cadena = '#'
it_companies.extend(cadena)
print(it_companies)

it_companies.sort()
print(it_companies)

it_companies.sort(reverse=True)
print(it_companies)

tres_primeras = it_companies[0:3]
print(tres_primeras)

tres_ultimas = it_companies[-3:]
print(tres_ultimas)

intermedias = it_companies[1:9]
print(intermedias)

it_companies.remove('Oracle')
print(it_companies)

existe_empresa = 'Potosi' in it_companies
print(existe_empresa)

del it_companies[1:8]
print(it_companies)

del it_companies[-1]
print(it_companies)

it_companies.clear()
print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
fullstack = front_end+back_end
print(fullstack)

fullstack.insert(5, 'Python')
print(fullstack)
fullstack.insert(6, 'SQL')
print(fullstack)

numeros = [10,20,30]
print(sum(numeros))
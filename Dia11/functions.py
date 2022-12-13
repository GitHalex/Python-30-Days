
""" def add_two_numbers(num1, num2):
   resultado = num1 + num2
   return resultado
print(add_two_numbers(2, 2)) """

""" def area_of_circle(radio):
   PI = 3.1416
   return PI*radio**2
print(area_of_circle(2)) """

""" def add_all_nums(*nums):
   total = 0
   for i in nums:
      i = str(i)
      if i.isnumeric():
         total += int(i)
      else:
         palabra = i
   return total, palabra
print(add_all_nums(2,3,5,'alex')) """

""" def convert_celsius_to_Fahrenheit(c):
   return (c*(9/5))+32
print(convert_celsius_to_Fahrenheit(3)) """

""" def check_season(mes):
   mes = mes.lower()
   if mes == 'septiembre' or mes == 'octubre' or mes == 'noviembre':
      return 'OTOÑO'
   elif mes == 'diciembre' or mes == 'enero' or mes == 'febrero':
      return 'INVIERNO'
   elif mes == 'marzo' or mes == 'abril' or mes == 'mayo':
      return 'PRIMAVERA'
   elif mes == 'junio' or mes == 'julio' or mes == 'agosto':
      return 'VERANO'
   else:
      return 'Valor incorrecto'
print(check_season('Septiembre')) """


""" def calculated_slope(x1, x2, y1, y2):
   pendiente = (y2-y1)/(x2-x1)
   return pendiente
print(calculated_slope(3,2,3,2)) """

""" def print_list(lista):
   for i in lista:
      print(i)
print(print_list(['hola','como','estas'])) """

""" def reverse_list(lista):
   longitud = len(lista)
   reves = []
   for i in range(longitud, 0, -1):
      reves.append(i)
   return reves
print(reverse_list([1, 2, 3, 4, 5])) """


""" def capitalize_list(lista):
   mayusculas = []
   for i in lista:
      i = i.capitalize()
      mayusculas.append(i)
   return mayusculas
print(capitalize_list(['Alex','calcina'])) """

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
numbers = [2,3,7,9]

""" def add_item(food_staff, palabra):
   food_staff.append(palabra)
   return food_staff
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
print(add_item(numbers, 5))   """

""" def remove_item(food_staff, a):
   food_staff.remove(a)
   return food_staff
print(remove_item(food_staff, 'Mango'))
print(remove_item(numbers, 3)) """

def sum_of_numbers(n):
   suma = 0
   for i in range(n+1):
      suma += i

   return suma
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050


def sum_of_odds(numero):
   suma_impares = 0
   for i in range(numero+1):
      if i%2 !=0:
         suma_impares += i
   return suma_impares

numero = int(input('ingrese un numero: '))
print(sum_of_odds(numero))

def sum_of_even(numero):
   suma_pares = 0
   for i in range(numero+1):
      if i%2 ==0:
         suma_pares += i
   return suma_pares

print(sum_of_even(numero))

def evens_and_odds(num):
   pares = 0
   impares = 0
   for i in range(num+1):
      if i%2 == 0:
         pares += 1
      else:
         impares +=1

   return f'the number of odds are {impares} \nthe numbers of evens are {pares}'
print(evens_and_odds(100))

def factorial(parametro):
   res = 1
   for i in range(res, parametro+1):
      res = res * i
   return res 
print(factorial(3))

def is_empty(vacio):
   vacio = str(vacio)
   if len(vacio) == 0:
      return 'Completamente vacio'
   else:
      return f'{vacio} su contenido del parametro'
print(is_empty(3))

def is_prime(num):
   es_Primo = True
   for i in range(2, num):
      if numero%i == 0:
         es_Primo = False
   return es_Primo

print(is_prime(3))



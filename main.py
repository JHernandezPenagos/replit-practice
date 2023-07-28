lista_numeros = []
continuar = True

while continuar == True:
    numero_insertado = input("Ingresa un numero para añadir a la lista: ")
    if (numero_insertado == ""):
        continuar = False
    else: 
        lista_numeros.append(int(numero_insertado))

def listar_primos(lista):
  lista_primos = []
  
  for numero in lista:
    es_primo = True
    if numero >= 2:
      for iterador in range(2, (numero+1)):
          if ((numero / iterador != 1) and (numero % iterador == 0)):
            es_primo = False
      if es_primo == True:
        lista_primos.append(numero)

  return lista_primos

print(lista_numeros)
print(listar_primos(lista_numeros))
  
  
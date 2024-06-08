#Arreglos (Lista)
numero = [1,2,3,4,5]
#Imprimir
print("Lista de númeos", numero)
#imprimir números individuales
print("Lista de númeos", numero[2])
print("Lista de númeos", numero[-1])

#agregar un elemento al final de la lista
numero.append(6)
print("Lista de númeos", numero)
#logitud de la lista
print("Lista de númeos", len(numero))
#eleminar elemento
numero.remove(2)
print("Lista de númeos", numero)

#recorer una lista con for
for numeros in numero:
    print ("Número de la lista", numero)

#recorer una lista con while
i = 0
while i <= len(numero):
    print ("Número de la lista(while) ", numero)
    i += 1
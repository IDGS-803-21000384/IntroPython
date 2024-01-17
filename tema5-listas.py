'''
Una lista es una secuencia de elementos de diferente tipo
[]
'''

lisa1=["Roberto",22,3.5,True,"Vargas",20,8]

print(lisa1)
print(type(lisa1))
print(lisa1[:])
print(lisa1[2])
print(lisa1[-1])
print(lisa1[1])
print(lisa1[0:3])
print(lisa1[3:])

lisa1.append("Cardiel")
print(lisa1)

lisa1.insert(2,"NAdia")
print(lisa1)

lisa1.extend(["uno",1.1,False])
print(lisa1)

lisa1.remove(22)
print(lisa1)

lisa1.pop()
print(lisa1)

lista2=["tres", "cuatro"]
lista3=lisa1+lista2
print(lista3)

print(lista2*4)

lista4=[2,1,5,4,3]
print(lista4)

lista4.sort()
print(lista4)

del lista4[0]
print(lista4)

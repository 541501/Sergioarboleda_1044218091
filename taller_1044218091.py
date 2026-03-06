edad=16
if edad>=18 :
    print("eres mayor de edad")
else: 
    print ("eres menor de edad")

#bucle 

for i in range (5):
    print("vete de acá")

 #bucle while

contador = 1
while contador <= 5:
    print("numero: "  + str(contador))
    contador = contador + 1
    
  #while  
for i in range (5): 
    print("numero: " + str(i))
    
for i in range (1, 6): 
    print("numero: " + str(i))
    
for i in range (0, 12, 3): 
    print("numero: " + str(i))
    
  #bandera (flag)
  
encontrado = False
numero = (1, 3, 5, 7, 9)
numerobuscado = 7
for numero in numero:
    if numero == numerobuscado:
        encontrado = True
        break
print("numero", numerobuscado, "encontrado:", str(encontrado))

 #bucles anidados
for i in range (3):
    for j in range (3):
        print("i:" + str(i) + "j:" + str (j))
    







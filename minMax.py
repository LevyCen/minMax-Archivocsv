
#Abrimos un archivo csv
file = open("fichero_salida_2015918.csv","r")

linea = file.readline()
contador = 1

for linea in file.readlines():
    print linea
    contador = contador + 1

print contador


#Cerramos el archivo
file.close()


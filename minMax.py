from string import *
from os import listdir

#Variables necesariamente globales
diccAP = {} #diccionario vacio
#Variables para conocer la fecha del registro
columnaAnio =  0
columnaMes =  0
columnaDia =  0
columnaHora =  0

#Se buscan todos los archivos csv del directorio
for directoryFile in listdir("."):
    fileTypeNecessary = 'csv'

    #se descarta los archivos que no sean csv
    nameFile = split(directoryFile,'.')
    if not nameFile[1]==fileTypeNecessary:
        continue
    nameFileCSV=directoryFile
    diccAP.clear()
    #Se abre el archivo csv
    #f = open("fichero_salida_2015938.csv")
    f = open(nameFileCSV)

    #Se extrae linea por linea del archivo csv
    for lineaDeCSV in f:
        lineaLeidaCSV = split(lineaDeCSV,',')
        
        columnaAnio =  strip(lineaLeidaCSV[8])
        columnaMes =  strip(lineaLeidaCSV[7])
        columnaDia =  strip(lineaLeidaCSV[6])
        columnaHora =  strip(lineaLeidaCSV[9])
        columMinuto = strip(lineaLeidaCSV[10])

        posicionNombreAP=int(4)

        if not diccAP.has_key(lineaLeidaCSV[posicionNombreAP]):
            diccAP.update( {lineaLeidaCSV[posicionNombreAP]: {columMinuto: 0}})  # diccionario con AP como clave
        else:
            if not diccAP[lineaLeidaCSV[posicionNombreAP]].has_key(columMinuto):
                diccAP[lineaLeidaCSV[posicionNombreAP]].update( {columMinuto: 0} )
        diccAP[lineaLeidaCSV[posicionNombreAP]][columMinuto] = int(diccAP[lineaLeidaCSV[posicionNombreAP]][columMinuto]) + 1

        #print diccAP[lineaLeidaCSV[posicionNombreAP]][strip(lineaLeidaCSV[10])]

    #print diccAP
    print ("Total de AP: ",len(diccAP))

    for AP in diccAP:

        #reinicializamos variables
        mini=100
        maximo=0
        totalDispEnHora=0
        numeroLectura = 0

        #Calculo de minimo, maximo y total
        for nDev in diccAP[AP].values():
            
            if nDev<mini:
                mini=nDev
            if nDev>maximo:
                maximo=nDev
            totalDispEnHora=totalDispEnHora+nDev

        #Se revisa si el numero de registros en una hora fue de 30
        #Repara el error de cuando en un AP no se registran cero usuarios
        minutosRegistrados = len(diccAP[AP].values())
        minutosRegCompletos = 30
        if minutosRegistrados < minutosRegCompletos:
            mini = 0

        #calculo del promedio
        promedio = int(totalDispEnHora)/int(minutosRegistrados)

        #Nomenclatura de stringResultados:
        # nombre del AP, minimo de conexiones, maximo de conexiones, suma totalDispEnHora de conexiones, numero de conexiones registradas, promedio, anio, mes, dia, hora
        stringResultados = str(AP) +','+ str(mini) +','+ str(maximo) +','+ str(totalDispEnHora) +','+ str(len(diccAP[AP].values())) +','+ str(promedio)+','+ str(columnaAnio) +','+ str(columnaMes) +','+ str(columnaDia) +','+ str(columnaHora)+'\n'


        #nomenclatura del csv de resultados: nombre del archivo_[anio]_[mes].csv
        namefileResult = 'Resultados_'+ str(columnaAnio) +'_'+ str(columnaMes) +'.csv'

        #log de los AP analizados
        print str(AP) + str(columnaAnio) + str(columnaMes)+ str(columnaDia)+ str(columnaHora)

        #Crea y edita el archivo csv con los resultados
        resultados = open(namefileResult,'a+')
        resultados.write(stringResultados)
        resultados.close()
        

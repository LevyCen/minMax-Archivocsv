from string import *
from os import listdir

#Variables necesariamente globales
dic = {} #diccionario vacio
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
    dic.clear()
    #Se abre el archivo csv
    #f = open("fichero_salida_2015938.csv")
    f = open(nameFileCSV)

    #Se extrae linea por linea del archivo csv
    for lineaDeCSV in f:
        tok = split(lineaDeCSV,',')
        #print tok
        columnaAnio =  strip(tok[8])
        columnaMes =  strip(tok[7])
        columnaDia =  strip(tok[6])
        columnaHora =  strip(tok[9])
        minuto = strip(tok[10])

        if not dic.has_key(tok[4]):
            dic.update( {tok[4]: {minuto: 0}})  # diccionario con AP como clave
        else:
            if not dic[tok[4]].has_key(minuto):
                dic[tok[4]].update( {minuto: 0} )
        dic[tok[4]][minuto] = int(dic[tok[4]][minuto]) + 1

        #print dic[tok[4]][strip(tok[10])]

    #print dic
    print ("Total de AP: ",len(dic))

    for AP in dic:

        #reinicializamos variables
        mini=100
        maximo=0
        total=0
        numeroLectura = 0

        for nDev in dic[AP].values():
            #print nDev
            if nDev<mini:
                mini=nDev
            if nDev>maximo:
                maximo=nDev
            total=total+nDev

        #Se revisa si el numero de registros en una hora fue de 30
        #Repara el error de cuando en un AP no se registran cero usuarios
        minutosRegistrados = len(dic[AP].values())
        minutosRegCompletos = 30
        if minutosRegistrados < minutosRegCompletos:
            mini = 0

        #Nomenclatura de stringResultados:
        # nombre del AP, minimo de conexiones, maximo de conexiones, suma total de conexiones, numero de conexiones registradas, ani, mes, dia, hora
        stringResultados = str(AP) +','+ str(mini) +','+ str(maximo) +','+ str(total) +','+ str(len(dic[AP].values())) +','+ str(columnaAnio) +','+ str(columnaMes) +','+ str(columnaDia) +','+ str(columnaHora)+'\n'


        #nomenclatura del csv de resultados: nombre del archivo_[anio]_[mes].csv
        namefileResult = 'Resultados_'+ str(columnaAnio) +'_'+ str(columnaMes) +'.csv'

        #log de los AP analizados
        print str(AP) + str(columnaAnio) + str(columnaMes)+ str(columnaDia)+ str(columnaHora)

        #Crea y edita el archivo csv con los resultados
        resultados = open(namefileResult,'a+')
        resultados.write(stringResultados)
        resultados.close()



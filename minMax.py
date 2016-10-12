from string import *
from os import listdir

#Variables
mini = 100
maximo = 0
total = 0
dic = {} #diccionario vacio
#Variables para conocer la fecha del registro
columnaAnio =  0
columnaMes =  0
columnaDia =  0
columnaHora =  0

#Se buscan todos los archivos csv del directorio
for fileCSV in listdir("."):
    ext = split(fileCSV,'.')
    if not ext[1]=="csv":
        continue

    dic.clear()
    #Se abre el archivo csv
    #f = open("fichero_salida_2015938.csv")
    f = open(fileCSV)

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
    print dic
    for AP in dic:
        print AP
        numeroLectura = 0
        for nDev in dic[AP].values():
            #print nDev
            if nDev<mini:
                mini=nDev
            if nDev>maximo:
                maximo=nDev
            total=total+nDev

        minutosRegistrados = len(dic[AP].values())
        minutosRegCompletos = 30
        if minutosRegistrados < minutosRegCompletos:
            mini = 0

        """
        print(AP)
        print ("Minimo de dispositivos: ",mini)
        print ("Maximo de dispositivos: ",maximo)
        print ("Total en la hr: ",total)
        print ("total minutos registrados: ", len(dic[AP].values()) )
        """
        #resultados se compone por:
        # nombre del AP, minimo de conexiones, maximo de conexiones, suma total de conexiones, numero de conexiones registradas, ani, mes, dia, hora
        stringResultados = '' + str(AP) +','+ str(mini) +','+ str(maximo) +','+ str(total) +','+ str(len(dic[AP].values())) +','+ str(columnaAnio) +','+ str(columnaMes) +','+ str(columnaDia) +','+ str(columnaHora)+'\n'
        #print stringResultados
        namefileResult = 'Resultados_'+ str(columnaAnio) +'_'+ str(columnaMes) +'_'+ str(columnaDia) +'.csv'
        print namefileResult

        #Creamos el archivo
        resultados = open(namefileResult,'a+')
        resultados.write(stringResultados)
        resultados.close()

        mini=100
        maximo=0
        total=0

from string import *
from os import listdir

#Variables
mini = 100
maximo = 0
total = 0
dic = {} #diccionario vacio

#Se busca los archivos csv para trabajar
for fileCSV in listdir("."):
    ext = split(fileCSV,'.')
    if not ext[1]=="csv":
        continue

    dic.clear()

    f = open("fichero_salida_2015938.csv")
    #f = open(fileCSV)

    for lineaDeCSV in f:
        tok = split(lineaDeCSV,',')
        #print tok
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
        #print AP
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
        stringResultados = '' + str(AP) +','+ str(mini) +','+ str(maximo) +','+ str(total) +','+ str(len(dic[AP].values()))
        print stringResultados

        mini=100
        maximo=0
        total=0



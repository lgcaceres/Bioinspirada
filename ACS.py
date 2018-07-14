import random 
import math
import time

#Valores Iniciales
p = 0.99
alfa = 1
beta = 1
Q = 1.0
qo = 0.7
fi = 0.05
feromona_Ini = 0.1
n_hormigas = 3
iteraciones = 350
abecedario = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U']
#abecedario =['0','1','2','3','4','5','6','7','8','9','10',11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
partida = 'A'#'A'

#('Mejor Hormiga Global:', 'AUJLKBCDMISENTRGFPHOQ', ' - Costo:', 9.252)
#Mejor Hormiga Global:', 'AUJLBKIMDCTENSFGRQPHO', ' - Costo:', 9.232999999999999
#'Mejor Hormiga Global:', 'AMILJUKBCDSENTQRGFPHO', ' - Costo:', 9.158999999999999
#Mejor Hormiga Global:', 'ABKJULIMDCTNESRFGQPHO', ' - Costo:', 8.886999999999999)----150
#Mejor Hormiga Global:', 'AUJKBCDMLISENTRGFPHOQ', ' - Costo:', 8.786)----200
#Mejor Hormiga Global:', 'AUJKBCDMILSENTGFRQPHO', ' - Costo:', 8.35)---250
#Mejor Hormiga Global:', 'AJUKBCDMILSENTRQGFPHO', ' - Costo:', 8.297)---300
#Mejor Hormiga Global:', 'AUJKBCDMILSENTQRGFPHO', ' - Costo:', 8.192)---350


mapa = {('A','A'):10000,('A','B'):1.522,('A','C'):1.836,('A','D'):1.658,('A','E'):2.056,('A','F'):2.734,('A','G'):2.766,('A','H'):3.522,('A','I'):1.330,('A','J'):0.663,('A','K'):0.823,('A','L'):1.199,('A','M'):1.557,('A','N'):2.036,('A','O'):3.915, ('A','P'):3.194,('A','Q'):2.632,('A','R'):2.539,('A','S'):1.916,('A','T'):2.116,('A','U'):0.551,
        ('B','A'):1.522,('B','B'):10000,('B','C'):0.752,('B','D'):0.955,('B','E'):1.351,('B','F'):1.956,('B','G'):2.077,('B','H'):2.834,('B','I'):1.053,('B','J'):1.169,('B','K'):0.701,('B','L'):1.288,('B','M'):1.215,('B','N'):1.313,('B','O'):3.276, ('B','P'):2.417,('B','Q'):2.179,('B','R'):1.899,('B','S'):1.344,('B','T'):1.290,('B','U'):1.340,
        ('C','A'):1.836,('C','B'):0.752,('C','C'):10000,('C','D'):0.380,('C','E'):0.631,('C','F'):1.204,('C','G'):1.327,('C','H'):2.082,('C','I'):0.724,('C','J'):1.252,('C','K'):1.106,('C','L'):1.025,('C','M'):0.726,('C','N'):0.591,('C','O'):2.524, ('C','P'):1.668,('C','Q'):1.459,('C','R'):1.157,('C','S'):0.676,('C','T'):0.545,('C','U'):1.435,
        ('D','A'):1.658,('D','B'):0.955,('D','C'):0.380,('D','D'):10000,('D','E'):0.449,('D','F'):1.133,('D','G'):1.213,('D','H'):1.993,('D','I'):0.389,('D','J'):1.019,('D','K'):1.053,('D','L'):0.678,('D','M'):0.346,('D','N'):0.417,('D','O'):2.423, ('D','P'):1.610,('D','Q'):1.242,('D','R'):1.005,('D','S'):0.394,('D','T'):0.466,('D','U'):1.187,
        ('E','A'):2.056,('E','B'):1.351,('E','C'):0.631,('E','D'):0.449,('E','E'):10000,('E','F'):0.690,('E','G'):0.764,('E','H'):1.544,('E','I'):0.727,('E','J'):1.397,('E','K'):1.500,('E','L'):0.937,('E','M'):0.526,('E','N'):0.039,('E','O'):1.974, ('E','P'):1.165,('E','Q'):0.831,('E','R'):0.559,('E','S'):0.176,('E','T'):0.154,('E','U'):1.547,
        ('F','A'):2.734,('F','B'):1.956,('F','C'):1.204,('F','D'):1.133,('F','E'):0.690,('F','F'):10000,('F','G'):0.176,('F','H'):0.878,('F','I'):1.405,('F','J'):2.072,('F','K'):2.186,('F','L'):1.572,('F','M'):1.179,('F','N'):0.718,('F','O'):1.320, ('F','P'):0.477,('F','Q'):0.554,('F','R'):0.267,('F','S'):0.817,('F','T'):0.684,('F','U'):2.211,
        ('G','A'):2.766,('G','B'):2.077,('G','C'):1.327,('G','D'):1.213,('G','E'):0.764,('G','F'):0.176,('G','G'):10000,('G','H'):0.780,('G','I'):1.447,('G','J'):2.104,('G','K'):2.262,('G','L'):1.583,('G','M'):1.210,('G','N'):0.797,('G','O'):1.212, ('G','P'):0.432,('G','Q'):0.401,('G','R'):0.228,('G','S'):0.862,('G','T'):0.790,('G','U'):2.232,
        ('H','A'):3.522,('H','B'):2.834,('H','C'):2.082,('H','D'):1.993,('H','E'):1.544,('H','F'):0.878,('H','G'):0.780,('H','H'):10000,('H','I'):2.216,('H','J'):2.862,('H','K'):3.041,('H','L'):2.326,('H','M'):1.975,('H','N'):1.576,('H','O'):0.443, ('H','P'):0.430,('H','Q'):0.921,('H','R'):0.997,('H','S'):1.638,('H','T'):1.559,('H','U'):2.979,
        ('I','A'):1.330,('I','B'):1.053,('I','C'):0.724,('I','D'):0.389,('I','E'):0.727,('I','F'):1.405,('I','G'):1.447,('I','H'):2.216,('I','I'):10000,('I','J'):0.670,('I','K'):0.876,('I','L'):0.300,('I','M'):0.246,('I','N'):0.710,('I','O'):2.627, ('I','P'):1.870,('I','Q'):1.372,('I','R'):1.221,('I','S'):0.588,('I','T'):0.803,('I','U'):0.823,
        ('J','A'):0.663,('J','B'):1.169,('J','C'):1.252,('J','D'):1.019,('J','E'):1.397,('J','F'):2.072,('J','G'):2.104,('J','H'):2.862,('J','I'):0.670,('J','J'):10000,('J','K'):0.573,('J','L'):0.553,('J','M'):0.895,('J','N'):1.380,('J','O'):3.260, ('J','P'):2.532,('J','Q'):1.982,('J','R'):1.876,('J','S'):1.255,('J','T'):1.466,('J','U'):0.185,
        ('K','A'):0.823,('K','B'):0.701,('K','C'):1.106,('K','D'):1.053,('K','E'):1.500,('K','F'):2.186,('K','G'):2.262,('K','H'):3.041,('K','I'):0.876,('K','J'):0.573,('K','K'):10000,('K','L'):0.952,('K','M'):1.118,('K','N'):1.470,('K','O'):3.467, ('K','P'):2.663,('K','Q'):2.237,('K','R'):2.047,('K','S'):1.409,('K','T'):1.511,('K','U'):0.705,
        ('L','A'):1.199,('L','B'):1.288,('L','C'):1.025,('L','D'):0.678,('L','E'):0.937,('L','F'):1.572,('L','G'):1.583,('L','H'):2.326,('L','I'):0.300,('L','J'):0.553,('L','K'):0.952,('L','L'):10000,('L','M'):0.412,('L','N'):0.929,('L','O'):2.716, ('L','P'):2.015,('L','Q'):1.434,('L','R'):1.355,('L','S'):0.772,('L','T'):1.041,('L','U'):0.653,
        ('M','A'):1.557,('M','B'):1.215,('M','C'):0.726,('M','D'):0.346,('M','E'):0.526,('M','F'):1.179,('M','G'):1.210,('M','H'):1.975,('M','I'):0.246,('M','J'):0.895,('M','K'):1.118,('M','L'):0.412,('M','M'):10000,('M','N'):0.518,('M','O'):2.383, ('M','P'):1.637,('M','Q'):1.125,('M','R'):0.983,('M','S'):0.365,('M','T'):0.631,('M','U'):1.032,
        ('N','A'):2.036,('N','B'):1.313,('N','C'):0.591,('N','D'):0.417,('N','E'):0.039,('N','F'):0.718,('N','G'):0.797,('N','H'):1.576,('N','I'):0.710,('N','J'):1.380,('N','K'):1.470,('N','L'):0.929,('N','M'):0.518,('N','N'):10000,('N','O'):2.008, ('N','P'):1.194,('N','Q'):0.870,('N','R'):0.595,('N','S'):0.185,('N','T'):0.133,('N','U'):1.532,
        ('O','A'):3.915,('O','B'):3.276,('O','C'):2.524,('O','D'):2.423,('O','E'):1.974,('O','F'):1.320,('O','G'):1.212,('O','H'):0.443,('O','I'):2.627,('O','J'):3.260,('O','K'):3.467,('O','L'):2.716,('O','M'):2.383,('O','N'):2.008,('O','O'):10000, ('O','P'):0.870,('O','Q'):1.284,('O','R'):1.420,('O','S'):2.058,('O','T'):1.997,('O','U'):3.367,
        ('P','A'):3.194,('P','B'):2.417,('P','C'):1.668,('P','D'):1.610,('P','E'):1.165,('P','F'):0.477,('P','G'):0.432,('P','H'):0.430,('P','I'):1.870,('P','J'):2.532,('P','K'):2.663,('P','L'):2.015,('P','M'):1.637,('P','N'):1.194,('P','O'):0.870, ('P','P'):10000,('P','Q'):0.730,('P','R'):0.660,('P','S'):1.282,('P','T'):1.160,('P','U'):2.663,
        ('Q','A'):2.632,('Q','B'):2.179,('Q','C'):1.459,('Q','D'):1.242,('Q','E'):0.831,('Q','F'):0.554,('Q','G'):0.401,('Q','H'):0.921,('Q','I'):1.372,('Q','J'):1.982,('Q','K'):2.237,('Q','L'):1.434,('Q','M'):1.125,('Q','N'):0.870,('Q','O'):1.284, ('Q','P'):0.730,('Q','Q'):10000,('Q','R'):0.360,('Q','S'):0.849,('Q','T'):0.924,('Q','U'):2.084,
        ('R','A'):2.539,('R','B'):1.899,('R','C'):1.157,('R','D'):1.005,('R','E'):0.559,('R','F'):0.267,('R','G'):0.228,('R','H'):0.997,('R','I'):1.221,('R','J'):1.876,('R','K'):2.047,('R','L'):1.355,('R','M'):0.983,('R','N'):0.595,('R','O'):1.420, ('R','P'):0.660,('R','Q'):0.360,('R','R'):10000,('R','S'):0.641,('R','T'):0.612,('R','U'):2.004,
        ('S','A'):1.916,('S','B'):1.344,('S','C'):0.676,('S','D'):0.394,('S','E'):0.176,('S','F'):0.817,('S','G'):0.862,('S','H'):1.638,('S','I'):0.588,('S','J'):1.255,('S','K'):1.409,('S','L'):0.772,('S','M'):0.365,('S','N'):0.185,('S','O'):2.058, ('S','P'):1.282,('S','Q'):0.849,('S','R'):0.641,('S','S'):10000,('S','T'):0.317,('S','U'):1.397,
        ('T','A'):2.116,('T','B'):1.290,('T','C'):0.545,('T','D'):0.466,('T','E'):0.154,('T','F'):0.684,('T','G'):0.790,('T','H'):1.559,('T','I'):0.803,('T','J'):1.466,('T','K'):1.511,('T','L'):1.041,('T','M'):0.631,('T','N'):0.133,('T','O'):1.997, ('T','P'):1.160,('T','Q'):0.924,('T','R'):0.612,('T','S'):0.317,('T','T'):10000,('T','U'):1.626,
        ('U','A'):0.551,('U','B'):1.340,('U','C'):1.435,('U','D'):1.187,('U','E'):1.547,('U','F'):2.211,('U','G'):2.232,('U','H'):2.979,('U','I'):0.823,('U','J'):0.185,('U','K'):0.705,('U','L'):0.653,('U','M'):1.032,('U','N'):1.532,('U','O'):3.367, ('U','P'):2.663,('U','Q'):2.084,('U','R'):2.004,('U','S'):1.397,('U','T'):1.626,('U','U'):10000}




visibilidad = {}
for hit in mapa:
    if(mapa[hit]==10000):
        visibilidad[hit] = 0.0
    else:
        visibilidad[hit] = 1.0/mapa[hit]

feromonas = {}
for hit in mapa:
    if(mapa[hit]==10000):
        feromonas[hit] = 0.0
    else:
        feromonas[hit] = feromona_Ini

def get_ciudad_intens(ciudad_actual,camino):
    dict_tn = {}
    for hit in abecedario:
        if hit not in camino:
            tn = feromonas[(ciudad_actual, hit)]*visibilidad[(ciudad_actual,hit)]
            dict_tn[tn] = hit
            print (ciudad_actual,"-",hit,": t =",feromonas[(ciudad_actual,hit)],"n =",visibilidad[(ciudad_actual,hit)],"t*n =",tn)
    return dict_tn[max(dict_tn.keys())]
    
def get_ciudad_divers(ciudad_actual,camino):
    dict_tn = {}
    dict_prob = {}
    suma = 0
    for hit in abecedario:
        if hit not in camino:
            tn = feromonas[(ciudad_actual, hit)]*visibilidad[(ciudad_actual,hit)]
            dict_tn[hit] = tn
            suma = suma + tn
            print (ciudad_actual,"-",hit,": t =",feromonas[(ciudad_actual,hit)],"n =",visibilidad[(ciudad_actual,hit)],"t*n =",tn)
    print ("Suma:",suma)
    for hit in dict_tn:
        print (ciudad_actual,"-",hit,": prob =",dict_tn[hit]/suma)
    aleatorio = random.uniform(0,1)
    print ("Numero aleatorio para la probabilidad:",aleatorio)
    n = 0
    for hit in dict_tn:
        n = n + dict_tn[hit]/suma
        if (n>=aleatorio):
            return hit

def actualizar_arco(actual,siguiente,feromonas):
    num = ((1-fi)*feromonas[(actual,siguiente)]) + (fi*feromona_Ini)
    feromonas[(actual,siguiente)] = num
    feromonas[(siguiente,actual)] = num
    
    
def fitness(cadena):
    resultado = 0
    for i in range(0,len(abecedario)-1):
        resultado = resultado + mapa[(cadena[i],cadena[i+1])]
    return resultado

def actualizar_feromonas(camino_minimo):
    new_feromonas = {}
    for hit in feromonas:
        if(feromonas[hit]==0.0):
            new_feromonas[hit] = 0.0
        else:
            n_feromona = p*feromonas[hit]
            cadena_print = ": Feromona ="+str(n_feromona)
            if(hit[0]+hit[1] in camino_minimo[0] or hit[1]+hit[0] in camino_minimo[0]):
                n_feromona = n_feromona + ((1-p)*Q/camino_minimo[1])
                cadena_print = cadena_print + " + " + str(((1-p)*Q/camino_minimo[1]))
            else:
                cadena_print = cadena_print + " + 0.0"
            print (hit[0],"-",hit[1],cadena_print,"=",n_feromona)
            new_feromonas[hit] = n_feromona
    return new_feromonas

# main
start_time = time.time()
minimo_global = (partida,100000)
for t in range (0,iteraciones):
    vector_caminos = []
    for k in range (0,n_hormigas):
        print ("Hormiga:",k+1)
        print ("Ciudad Inicial:",partida)
        camino = partida
        for i in range (0,len(abecedario)-1):
            q = random.uniform(0,1)
            print ("Valor de q:",q)
            siguiente = partida
            if (q<=qo):
                #intensificacion
                print ("Recorrido por Intensificacion")
                siguiente = get_ciudad_intens(camino[-1:],camino)
            else:
                #diversificacion
                print ("Recorrido por Diversificacion")
                siguiente = get_ciudad_divers(camino[-1:],camino)
            print ("Ciudad Siguiente:",siguiente)
            print ("Actualizamos el arco",camino[-1:],"-",siguiente,"(v): ( 1 -",fi,") *",feromonas[(camino[-1:],siguiente)],"+",fi,"*",feromona_Ini,"=",((1-fi)*feromonas[(camino[-1:],siguiente)]) + (fi*feromona_Ini))
            actualizar_arco(camino[-1:],siguiente,feromonas)
            camino = camino + siguiente
        print ("Hormiga",k+1,":",camino)
        vector_caminos.append((camino,fitness(camino)))
    for k in range (0,n_hormigas):
        print ("Hormiga",k+1,"(",vector_caminos[k][0],") - Costo:",vector_caminos[k][1])
    minimo = min(vector_caminos,key = lambda t: t[1])
    print ("Mejor Hormiga Local:",minimo[0]," - Costo:",minimo[1])
    if (minimo[1] < minimo_global[1]):
        minimo_global = minimo
    print ("Mejor Hormiga Global:",minimo_global[0]," - Costo:",minimo_global[1])
    feromonas = actualizar_feromonas(minimo)
print("----%s seconds--" %(time.time()-start_time))



    




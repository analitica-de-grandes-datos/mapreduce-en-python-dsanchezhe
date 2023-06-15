#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    listaTuplas = []
    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        key, fecha, numero = line.split("\t")
        numero = int(numero)
        tupla = key, fecha, numero
        listaTuplas.append(tupla)
        
    #ordernar el diccionario
    tuplaOrdenada = sorted(listaTuplas, key=lambda x: (x[0],x[2]))

    #imprimir el diccionario
    for tupla in tuplaOrdenada:
        sys.stdout.write("{}   {}   {}\n".format(tupla[0], tupla[1], tupla[2]))
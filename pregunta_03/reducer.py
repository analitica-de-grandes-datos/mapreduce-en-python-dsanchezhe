import sys

#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    diccionario = {}

    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        key, val = line.split("\t")
        val = int(val)

        diccionario[key] = val

    #ordernar el diccionario
    diccionario = sorted(diccionario.items(), key=lambda x: x[1])

    #imprimir el diccionario
    for key, val in diccionario:
        sys.stdout.write("{},{}\n".format(key, val))
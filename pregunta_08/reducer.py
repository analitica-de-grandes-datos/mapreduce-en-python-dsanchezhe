#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
from audioop import avg
import sys

if __name__ == '__main__':

    curkey = None
    listaElementos = []
    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)
        
        if key == curkey:
            #
            # No se ha cambiado de clave. Aca se acumulan los valores para la misma
            # clave.
            #
            listaElementos.append(val)
        else:
            #
            # Se cambio de clave. Se reinicia el acumulador.
            #
            if curkey is not None:
                #
                # una vez se han reducido todos los elementos
                # con la misma clave se imprime el resultado en
                # el flujo de salida
                #
                suma = sum(listaElementos)
                prom = suma / len(listaElementos)
                listaElementos.clear()                

                sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, prom))

            curkey = key
            listaElementos.append(val)               

    suma = sum(listaElementos)
    prom = suma / len(listaElementos)
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, prom))
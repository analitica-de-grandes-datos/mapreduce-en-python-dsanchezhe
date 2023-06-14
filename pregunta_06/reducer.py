#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':

    curkey = None
    min = 0
    max = 0

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
            if max > val:
                max = max
            else:
                max = val
            if min < val:
                min = min
            else:
                min = val
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
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, max, min))

            curkey = key
            min = val
            max = val

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, max, min))
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import bisect
#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    curkey = None
    keys=[]
    tot=[]
    tot2=[]
    tot3=[]
    tot4=''
    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:
        key, val = line.split("\t")
        val = int(val)
        if key == curkey:
            #
            # No se ha cambiado de clave. Aca se acumulan los valores para la misma
            # clave.
            #
            tot.append(val)
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
                for num in tot:
                    bisect.insort(tot2,num)
                tot3=[str(x) for x in tot2]
                tot4 = ','.join(tot3)
                sys.stdout.write("{}\t{}\n".format(curkey, tot4))
                # inicializamos
                tot=[]
                tot2=[]
                tot3=[]
                tot4 = ''

            curkey = key
            tot.append(val)
                        
    for num in tot:
                    bisect.insort(tot2,num)
    tot3=[str(x) for x in tot2]
    tot4 = ','.join(tot3)
                
    sys.stdout.write("{}\t{}\n".format(curkey, tot4))
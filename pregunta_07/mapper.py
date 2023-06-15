#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    for line in sys.stdin:
        fields = line.strip().split('   ',3)
        letra=fields[0]
        fecha=fields[1]
        numero=fields[2]
        
        sys.stdout.write("{}\t{}\t{}\n".format(letra,fecha,numero))

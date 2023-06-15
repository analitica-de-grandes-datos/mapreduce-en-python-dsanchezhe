#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    for line in sys.stdin:
        fields = line.strip().split('   ',3)
        fecha = fields[1]
        fechaSeparada = fecha.split('-')
        mes=fechaSeparada[1]

        sys.stdout.write("{}\t1\n".format(mes))

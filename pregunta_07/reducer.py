#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    for line in sys.stdin:

        sys.stdout.write("{}   {}   {}\n".format(str(line.split('   ')[0]), line.split('   ')[2].strip() , int(line.split('   ')[1])))
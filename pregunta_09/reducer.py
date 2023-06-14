#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    count = 0
    for line in sys.stdin:
        sys.stdout.write("{}   {}   {}\n".format(line.split('   ')[1], line.split('   ')[2].strip() , int(line.split('   ')[0])))
        if count >= 5: break;
        count = count +1
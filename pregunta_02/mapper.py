#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

    my_iterator = iter(sys.stdin.readline, "")
    next(my_iterator)

    for line in my_iterator:
        fields = line.strip().split(',',5)
        purpose =  fields[3]
        amount = fields[4]

        sys.stdout.write("{}\t{}\n".format(purpose, amount))

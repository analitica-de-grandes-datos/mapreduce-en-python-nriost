import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys 
if __name__ == "__main__":

    ##
    ## itera sobre cada linea de codigo recibida
    ## a traves del flujo de entrada
    ##
 for line in sys.stdin:
       fields=line [0:].split('   ') 
       sys.stdout.write("{}\t1\n".format(fields[0])) 

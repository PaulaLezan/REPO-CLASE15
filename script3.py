#realizar un script que imprima hola 5 veces
import sys

if len (sys.argv)!=3:
    print ("error, necesito 2 arguentos")
else:
    for i in range (int(sys.argv[2])) :
        print(sys.argv[1])
        
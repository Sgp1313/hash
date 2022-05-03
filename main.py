
#Que es un hash?
#Hash es un algoritmo matematico que convierte un grupo de datos (como un nombre o una palabra) 
# y lo con vierte en una serie de caracteres que siempre va ateneer el mismo numero de digitos. 

#Que es un hash SHA-1?

#Es una funcion de hash que combina letras y numeros para llegar a un total de 40 cifras 
# por ejemplo: sebastian = 2281f348b9e7743a22560fb3977756573c447081


#Como abrir un archivo en python?
 
with open("hash_progra.txt","r") as archivo:
    for linea in archivo:
        print(linea)


import hashlib

file = "hash_progra.txt" 
BLOCK_SIZE = 65536 

file_hash = hashlib.sha1()
with open(file, 'rb') as f: 
    fb = f.read(BLOCK_SIZE) 
    while len(fb) > 0: 
        file_hash.update(fb) 
        fb = f.read(BLOCK_SIZE) 

print (file_hash.hexdigest()) 


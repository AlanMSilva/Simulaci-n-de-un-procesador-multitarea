from ListaCircular import ListaCircular
from random import randint
lista = ListaCircular()

lista.AgregarInicio(randint(4, 9))
for i in range(0, 300):
    if (randint(1, 100) <= 25):
        print(f'se creo un nuevo trabajo en el ciclo {i}')
        lista.Recorrer()
        lista.AgregarFinal(randint(4, 9))
        print('Se termino el trabajo ' + str(i))

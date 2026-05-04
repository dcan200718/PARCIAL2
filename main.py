from main import ListaCircular
from main import ListaSimple

if __name__ == "__main__":

    print("===== Punto 1 =====")
    lista_c = ListaCircular()
    lista_c.crear_lista(7)
    lista_c.mostrar()

    sobreviviente = lista_c.josephus_modificado(3)
    print("Sobreviviente:", sobreviviente)


    print("\n===== Punto 2 =====")
    lista_s = ListaSimple()

    for x in [1, 2, 3, 4, 5, 6]:
        lista_s.insertar_final(x)

    lista_s.mostrar()

    lista_s.partir_voltear_intercalar()
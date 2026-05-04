class NodoCircular:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class ListaCircular:
    def __init__(self):
        self.head = None

    def insertar_final(self, dato):
        nuevo = NodoCircular(dato)

        if not self.head:
            self.head = nuevo
            nuevo.next = self.head
            return

            actual = self.head
        while actual.next != self.head:
            actual = actual.next

        actual.next = nuevo
        nuevo.next = self.head

    def crear_lista(self, n):
        for i in range(1, n + 1):
            self.insertar_final(i)

    def mostrar(self):
        if not self.head:
            print("Lista vacía")
            return

        resultado = []
        actual = self.head

        while True:
            resultado.append(str(actual.dato))
            actual = actual.next
            if actual == self.head:
                break

        print(" -> ".join(resultado) + " -> (ciclo)")

def josephus_modificado(self, m):
  actual = self.head
  anterior = None
  while actual.next!= None and actual!= None:
      for i in range(m-1):
          anterior = actual
          actual = actual.next

  eliminado = actual.data
  if self.head == None:
     actual = actual.next
  anterior.next = actual.next
  actual.next = anterior
  if eliminado % 5 == 0:
      anterior = actual
      actual = actual.next

  return actual





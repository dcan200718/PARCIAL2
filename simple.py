class NodoSimple:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class ListaSimple:
    def __init__(self):
        self.head = None

    def insertar_final(self, dato):
        nuevo = NodoSimple(dato)

        if not self.head:
            self.head = nuevo
            return

        actual = self.head
        while actual.next:
            actual = actual.next

            actual.next = nuevo

    def mostrar(self):
        if not self.head:
            print("Lista vacía")
            return

        actual = self.head
        resultado = []

        while actual:
            resultado.append(str(actual.dato))
            actual = actual.next

        print(" -> ".join(resultado) + " -> None")

    def partir_voltear_intercalar(self):
      lento = self.head
      rapido = self.head
      while rapido.next!= None and rapido.next.next!= None:
          lento = rapido.next
          rapido = rapido.next.next
      inicioMitad = lento.next
      lento.next = None
      actual = lento.next
      anterior = None
      while actual.next!= None and actual!= None:
          siguiente = actual.next
          actual.next = anterior
          anterior = actual
          actual = siguiente
    def intercalar(h1,h2):
        p1=h1
        p2=h2
        cont = 0
        temp = head
        while temp!= None:
            temp = temp.next
            cont+=1
        
        while p1 is not p2:
            for i in range(cont):
                if p1.next != None:
                    p1=p1.next
                else:
                    p1 = h2
                if p2.next != None:
                    p2=p2.next
                else:
                    p2=h1
                 
        
        
      
      
      
      
      
      
    

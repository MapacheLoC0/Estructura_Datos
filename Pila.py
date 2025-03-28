class Nodo:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.items = []  # Lista para almacenar los elementos de la pila
        
    def push(self, value):
        new_nodo = Nodo(value)
        new_nodo.next = self.head
        self.head = new_nodo
        self.items.append(value)  # Agregar el valor a la lista

    def pop(self):
        if self.head is None:
            print("Stack vacía, no se puede eliminar")
            return None
        value = self.head.value
        self.head = self.head.next
        self.items.pop()  # Eliminar el último elemento de la lista
        return value

    def get_items(self):
        return self.items  # Método para obtener los elementos de la lista


pila = Stack()
pila.push(1)
pila.push(2)
pila.push(3)

print(pila.get_items())  # Imprime [1, 2, 3]
print(pila.pop())        # Imprime 3
print(pila.get_items())  # Imprime [1, 2]

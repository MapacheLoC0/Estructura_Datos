class Nodo:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.items = []
        
    def push(self, value):
        new_nodo = Nodo(value)
        new_nodo.next = self.head
        self.head = new_nodo
        self.items.append(value)

    def pop(self):
        if self.head is None:
            print("Stack vacía, no se puede eliminar")
            return None
        value = self.head.value
        self.head = self.head.next
        self.items.pop()
        return value

    def get_items(self):
        return self.items


pila = Stack()
pila.push(1)
pila.push(2)
pila.push(3)

print(pila.get_items())
print(pila.pop())
print(pila.get_items())

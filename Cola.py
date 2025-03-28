class Nodo:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.items = []
        
    def enqueue(self, value):
        new_nodo = Nodo(value)
        if self.tail is None:
            self.head = new_nodo
            self.tail = new_nodo
        else:
            self.tail.next = new_nodo
            self.tail = new_nodo
        self.items.append(value)

    def dequeue(self):
        if self.head is None:
            print("Cola vacía, no se puede eliminar")
            return None
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.items.pop(0)
        return value

    def get_items(self):
        return self.items


cola = Queue()
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)

print(cola.get_items())
print(cola.dequeue()) 
print(cola.get_items())
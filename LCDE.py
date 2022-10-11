from ast import And


class Node:
    def __init__(self, valor):
        self.valor = valor
        self.next = None
        self.prev = None

class ListaCircularDuplamenteEncadeada:
    def __init__(self):
        self.head = None
        self.tail = None

    def PrintLista(self):
        if self.head == None:
            print("Não existe essa lista")
        else:
            atual = self.head
            while atual:
                print(atual.valor, end=" ")
                if atual == self.tail:
                    break
                atual = atual.next
            print("")
    
    def PrintRevLista(self):
        if self.head == None:
            print("Não existe essa lista")
        else:
            atual = self.tail
            while atual:
                print(atual.valor, end=" ")
                if atual == self.head:
                    break
                atual = atual.prev
            print("")

    def Cont(self):
        if self.head == None:
            print("Não existe essa lista")
        else:
            cont = 1
            atual = self.head
            while atual:
                if atual == self.tail:
                    break
                atual = atual.next
                cont += 1
            return(cont)

    def add(self, valor):
        new_node = Node(valor)
        self.head = new_node
        self.tail = new_node

    def addBegin(self, valor):
        if self.head is None:
            self.add(valor)
        else:
            new_node = Node(valor)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
            self.head.prev = self.tail

    def addEnd(self, valor):
        if self.head is None:
            self.add(valor)
        else:
            new_node = Node(valor)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = self.head
            self.head.prev = self.tail

    def addPos(self, valor, posi):
        atual = self.head
        if posi == 0:
            self.addBegin(valor)
        elif posi < 0:
            print("Não tem posição negativa")
        elif (posi > 0) and (self.head == None):
            print("Não existe essa lista")
        else:
            add = True
            for i in range(posi):   
                atual = atual.next
                if atual == self.tail.next:
                    add = False
            if (add == False):
                print("Não tem essa posição")
            else:
                new_node = Node(valor)
                ant = atual.prev
                prox = atual
                ant.next = new_node
                new_node.prev = ant
                prox.prev = new_node
                new_node.next = prox
                atual = new_node
        

lista = ListaCircularDuplamenteEncadeada()
lista.addPos(20, 1)
lista.PrintLista()
lista.addPos(20, 0)
lista.PrintLista()
lista.addBegin(10)
lista.addBegin(40)
lista.addBegin(30)
lista.PrintLista()
print(lista.Cont())
lista.addEnd(50)
lista.addEnd(20)
lista.addEnd(77)
lista.addBegin(5)
lista.PrintLista()
print(lista.Cont())
lista.addPos(35, 6)
lista.addPos(1, 0)
lista.addPos(100, 15)
lista.addPos(80, -1)
lista.addPos(45, 5)
lista.PrintLista()
lista.PrintRevLista()
x = lista.Cont()
print('Tem', x, 'elementos na lista.')

                


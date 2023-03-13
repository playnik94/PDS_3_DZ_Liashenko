class HashTable:

    def __init__(self):
        self.size = int(input("Размер таблицы : "))
        self.max_element = 0
        self.element = list()

    def capacity(self):
        if self.size == self.max_element:
            return True
        else:
            return False

    def added_element(self, add_element):
        self.add_element = add_element
        if self.capacity():
            print("нет места")
        else:
            self.element.append(self.add_element)
            self.max_element += 1
            print(f"Добавлен{self.add_element}")

    def search(self, elements):
        self.elements = elements
        if self.elements in self.element:
            print(f"{self.elements} Есть такой элемент")
            return self.element
        else:
            print(f"{self.elements} Такого элемента нет")

    def delete_element(self, d_element):
        self.d_element = d_element
        if self.d_element in self.element:
            print(f"Элемент {self.d_element} удален из списка")
        else:
            print(f"Элемент {self.d_element} нет в списке")

    def print_scrin(self):
        print(self.element)

root = HashTable()
root.capacity()
root.added_element({"Artem": 29})
root.added_element({"Artur": 36})
root.added_element({"Misha": 27})
root.added_element({"Sergei": 33})
root.added_element({"Pavel": 19})
root.added_element({"Anna": 44})
root.added_element({"Vova": 31})
root.added_element({"Volodimir": 45})
root.print_scrin()
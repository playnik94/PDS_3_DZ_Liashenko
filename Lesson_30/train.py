class HashTable:

    def __init__(self):

        self.size = int(input("Size of capacity : "))
        self.max_element = 0
        self.element = dict()

    def capacity(self):
        if self.size == self.max_element:
            return True
        else:
            return False

    def added_element(self, k, v):

        if self.capacity():
            print("Not capacity")
        else:
            self.element[k] = v
            self.max_element += 1
            print(f" add: {k}:{v} ")

    def search(self, *ser):

        for i in ser:
            if i in self.element.keys():
                print(f'Element is found {i}:{self.element.get(i)}')
            else:
                print(f' Element is not found: {ser}')

    def delete_element(self, *d_element):

        for i in d_element:
            if i in self.element.keys():
                self.element.pop(i)
                print(f"Element {i} deleted")
            else:
                print(f"Element {d_element} is not found")

    def __dict__(self):
        return self.element


# root = HashTable()
# root.capacity()
# root.added_element("Artem", 22)
# root.added_element("Artur", 23)
# root.added_element("Arci", 29)
# root.search("Arci", 'Artur')
# root.delete_element('Arci')


from hash_distribution import plot, distribute
from string import printable

plot(distribute(printable, num_containers=2))

plot(distribute(printable, num_containers=5))



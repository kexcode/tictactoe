class Cell:
    def __init__(self, position = 1):
        self.position = position
        self.value = None

    def is_filled(self):
        return self.value != None

class Board:
    def __init__(self, dimention = 3):
        self.dimention = dimention
        self.max_size = dimention ** 2
        self.occupied_cells = 0
        self.cell_dict = {}
        for cell in range(1, self.max_size + 1):
            self.cell_dict[cell] = ''

    def state(self):
        print('Indexing:\t\t\tCurrent board:')
        list_to_print = []
        dimention = self.dimention
        for cell in self.cell_dict:
            list_to_print.append(self.cell_dict[cell])
        for index in range(dimention):
            index_list = [str(x + 1) for x in range(dimention * index, dimention * (index + 1))]
            print('[', ' | '.join(index_list), ']\t\t\t[', ' | '.join(list_to_print[dimention * index : dimention * (index + 1)]),']')

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
        print('Current board:\n')
        for cell in self.cell_dict:
            print('{} | '.format(self.cell_dict[cell]))

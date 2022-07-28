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
        self.turn_count = 0
        self.cell_dict = {}
        for cell in range(1, self.max_size + 1):
            self.cell_dict[cell] = ' '

    def state(self):
        print('Indexing:\t\t\tCurrent board:')
        list_to_print = []
        dimention = self.dimention
        for cell in self.cell_dict:
            list_to_print.append(self.cell_dict[cell])
        for index in range(dimention):
            index_list = [str(x + 1) for x in range(dimention * index, dimention * (index + 1))]
            print('[', ' | '.join(index_list), ']\t\t\t[', ' | '.join(list_to_print[dimention * index : dimention * (index + 1)]),']')

    def has_space(self):
        return self.turn_count < self.max_size

    def play_at_position(self, position):
        if not self.has_space():
            return print('Game over!')

        if position in self.cell_dict.keys():
            self.cell_dict[position] = 'X' if self.turn_count % 2 == 0 else 'O'
            self.turn_count += 1
        else:
            return print('Error: invalid position, please try again.')

        print('position = {}'.format(position))
        print('symbol = {}'.format(self.cell_dict[position]))
        print(self.cell_dict)
        self.state()

    
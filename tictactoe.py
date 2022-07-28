class Cell:
    def __init__(self, position = 1):
        self.position = position
        self.value = ' '

    def is_filled(self):
        return self.value != ' '

class Board:
    def __init__(self, dimention = 3):
        self.dimention = dimention
        self.max_size = dimention ** 2
        self.turn_count = 0
        self.cell_dict = {}
        for index in range(1, self.max_size + 1):
            self.cell_dict[index] = Cell(index)

    def state(self):
        # print(self.cell_dict)
        print('turns = ', self.turn_count)
        print('Indexing:\t\t\tCurrent board:')
        list_to_print = []
        dimention = self.dimention
        for cell in self.cell_dict:
            list_to_print.append(self.cell_dict[cell].value)
        for index in range(dimention):
            index_list = [str(x + 1) for x in range(dimention * index, dimention * (index + 1))]
            print('[', ' | '.join(index_list), ']\t\t\t[', ' | '.join(list_to_print[dimention * index : dimention * (index + 1)]),']')
        

    def has_space(self):
        return self.turn_count < self.max_size
    
    def is_winning(self):
        player = 'O' if self.turn_count % 2 == 0 else 'X'
        pos_diag_score = 0
        neg_diag_score = 0
        for index1 in range(self.dimention):
            col_score = 0
            row_score = 0

            # check diagonal cases
            if self.cell_dict[index1 * self.dimention + index1 + 1].value == player:
                pos_diag_score += 1
            if self.cell_dict[index1 * self.dimention + self.dimention - index1].value == player:
                neg_diag_score += 1
                        
            for index2 in range(self.dimention):
                # check current cell for horizontal lines: index2 = columns, index1 = rows
                if self.cell_dict[index1 * self.dimention + index2 + 1].value == player:
                    row_score += 1
                # check current cell for vertical lines: index1 = columns, index2 = rows
                if self.cell_dict[index2 * self.dimention + index1 + 1].value == player:
                    col_score += 1
            if col_score == self.dimention or row_score == self.dimention:
                return True
        if pos_diag_score == self.dimention or neg_diag_score == self.dimention:
            return True
        
        return False

    def play_at_position(self, position):
        if not self.has_space():
            return print('Game over!')

        if position in self.cell_dict.keys():
            if self.cell_dict[position].is_filled():
                return print('The selected cell is busy, please try again.')
            
            self.cell_dict[position].value = 'X' if self.turn_count % 2 == 0 else 'O'
            self.turn_count += 1
            self.state()
            # check if winning or no more moves
            if self.is_winning():
                
                return print('Congrats! You win!')

            if not self.has_space():
                return print('Game over!')           

            

        else:
            return print('Error: invalid position, please try again.')

        # print('position = {}'.format(position))
        # print('symbol = {}'.format(self.cell_dict[position]))

        self.state()

    